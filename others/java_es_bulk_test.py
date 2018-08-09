from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import time
INDEX_NAME = 'question2'
TYPE_NAME = 'java'
FILENAME = r'java_data'  # json source file

time_start = time.time()
# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'), timeout=10)  # user/passwd
index_mappings = {
    "mappings": {
        "java": {
            "properties": {
                "Title": {
                    "type": "text",
                    "analyzer": "english",
                },
                "LastEditorDisplayName": {
                    "type": "text",
                    "index": "false"
                },
                "Id": {
                    "type": "keyword"
                },
                "PostTypeId": {
                    "type": "keyword",
		    "index": "false"
                },
                "AcceptedAnswerId": {
                    "type": "keyword"
                },
                "CreationDate": {
                    "type": "date"
                },
                "Score": {
                    "type": "float"
                },
                "Body": {
                    "type": "text",
                    "analyzer": "english",
                },
                "LastEditorUserId": {
                    "type": "keyword",
		    "index": "false"
                },
                "OwnerUserId": {
                    "type": "keyword",
		    "index": "false"
                },
                "FavoriteCount": {
                    "type": "keyword",
                },
                "LastEditDate": {
                    "type": "date",
		    "index": "false"
                },
                "LastActivityDate": {
                    "type": "date",
	            "index": "false"
                },
                "Tags": {
                    "type": "text",
                    "analyzer": "english",
                },
                "AnswerCount": {
                    "type": "integer"
                },
                "CommentCount": {
                    "type": "integer",
                },
                "OwnerDisplayName": {
                    "type": "text",
                    "index": "false"
                },
                "ViewCount": {
                    "type": "integer",
		    "index": "false"
                }
            }
        }
    }
}

if es.indices.exists(index=INDEX_NAME) is not True:
    es.indices.create(index=INDEX_NAME, body=index_mappings)

actions = []
f = open(FILENAME)
i = 0
for line in f:
    i = i + 1
    line_dict = json.loads(line)
    _index = INDEX_NAME
    _type = TYPE_NAME
    _id = line_dict['Id']
    action = {
        "_index": _index,
        "_type": _type,
        "_id": _id,
        "_source": line_dict

    }
    actions.append(action)
    if(len(actions) == 10000):
        time_1 = time.time()
        helpers.bulk(es, actions)
        del actions[0:len(actions)]
        time_2 = time.time()
        print(str(i) + ' ' + str(10000 / (time_2 - time_1)))


if len(actions) > 0:
    helpers.bulk(es, actions)

time_end = time.time()
print("time:%s", time_end - time_start)
