from elasticsearch import Elasticsearch
from elasticsearch import helpers

INDEX_NAME = 'entertainment'
TYPE_NAME = 'qq_movie'
FILENAME = r'qq_movie'  # json source file

# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'))  # user/passwd
index_mappings = {
    "settings": {
        "number_of_shards": 1
    },
    "mappings": {
        "qq_movie": {
            "properties": {
                "label": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "id": {
                    "type": "keyword"
                },
                "attr": {
                    "properties": {
                        "url": {
                            "type": "keyword"
                        }
                    }
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
for line in f.readlines():
    list_line = line.strip().split('\t')
    _index = INDEX_NAME
    _type = TYPE_NAME
    _id = list_line[1]
    _label = list_line[0]
    _attr = eval(list_line[2])
    action = {
        "_index": _index,
        "_type": _type,
        "_id": _id,
        "_source": {
            "label": _label,
            "id": _id,
            "attr": _attr
        }
    }
    i = i + 1
    actions.append(action)
    if(len(actions) == 5000):
        helpers.bulk(es, actions)
        del actions[0:len(actions)]
if len(actions) > 0:
    helpers.bulk(es, actions)
