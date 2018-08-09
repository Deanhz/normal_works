from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os
import sys
import argparse
import time
import json
sys.path.append("..")
from config.data_setting import *
from config.server_setting import *

DATA_NOT_FOUND = 'data not found in data path!'
DATA_UPTODATE = 'data Already up-to-date!'
UPDATE_SUCCESS = 'update data success!'


# timestamp file example:
# {
# "local":"",
# "online": ""
# }


def update_data():
    # timestamp file not exist
    if not os.path.exists(DATA_DIR + TIMESTAMP_FILE):
        update_timestamp(DATA_DIR + TIMESTAMP_FILE)
        ES = Elasticsearch(http_auth=(ES_USERNAME, ES_PASSWORD), timeout=10)
        update_question(ES)
        update_ans(ES)
        return UPDATE_SUCCESS
    # timestamp file read
    f_timestamp = open(DATA_DIR + TIMESTAMP_FILE, 'r')
    str_dict = f_timestamp.read()
    # timestamp file is empty
    if not str_dict:
        ES = Elasticsearch(http_auth=(ES_USERNAME, ES_PASSWORD), timeout=10)
        update_question(ES)
        update_ans(ES)
        update_timestamp(DATA_DIR + TIMESTAMP_FILE)
        return UPDATE_SUCCESS
    # timestamp file is not empty
    timestamp = json.loads(str_dict)
    # elasticsearch datas are up-to-date
    if timestamp['online'] != "" and (timestamp['online'] == timestamp['local']):
        return DATA_UPTODATE
    if not os.path.exists(DATA_DIR + QUESTION_FILE):
        return DATA_NOT_FOUND
    if not os.path.exists(DATA_DIR + ANSWER_FILE):
        return DATA_NOT_FOUND
    # elasticsearch datas need be updated
    print("update begin......")
    ES = Elasticsearch(http_auth=(ES_USERNAME, ES_PASSWORD), timeout=10)
    update_question(ES)
    update_ans(ES)
    update_timestamp(DATA_DIR + TIMESTAMP_FILE)
    return UPDATE_SUCCESS


def update_timestamp(filename):
    dic = {}
    f_timestamp_w = open(filename, 'w')
    dic['local'] = time.strftime("%Y-%m-%d")
    dic['online'] = time.strftime("%Y-%m-%d")
    f_timestamp_w.write(json.dumps(dic))


def update_question(ES):
    INDEX_NAME = 'question'
    TYPE_NAME = 'stackoverflow'
    if not ES.indices.exists(index=INDEX_NAME):
        ES.indices.create(
            index=INDEX_NAME,
            body={
                'settings': {
                    'number_of_shards': 5,
                    'number_of_replicas': 1,
                    "analysis": {
                        "filter": {
                            "english_stop": {
                                "type": "stop",
                                "stopwords": "_english_"
                            },
                            "light_english_stemmer": {
                                "type": "stemmer",
                                "language": "light_english"
                            },
                            "english_possessive_stemmer": {
                                "type": "stemmer",
                                "language": "possessive_english"
                            }
                        },
                        "analyzer": {
                            "english": {
                                "tokenizer": "standard",
                                "filter": [
                                    "english_possessive_stemmer",
                                    "lowercase",
                                    "english_stop",
                                    "light_english_stemmer",
                                    "asciifolding"
                                ]
                            }
                        }
                    }
                },
                'mappings': {
                    TYPE_NAME: {
                        "properties": {
                            'Title': {
                                'boost': 1,
                                'type': 'text',
                                "analyzer": "english",
                                "similarity": "BM25"
                            },
                            'Body': {
                                'boost': 1.0,
                                'type': 'text',
                                "analyzer": "english",
                                "similarity": "BM25"
                            },
                            "Tags": {
                                'boost': 1,
                                "type": "text",
                                "analyzer": "english",
                                "similarity": "BM25"
                            },

                            "LastActivityDate": {"type": "date"},
                            "CreationDate": {"type": "date"},
                            "LastEditDate": {"type": "date"},
                            "ClosedDate": {"type": "date"},
                            'CommunityOwnedDate': {"type": "date"},

                            "CommentCount": {"type": "integer"},
                            "ViewCount": {"type": "integer"},
                            "AnswerCount": {"type": "integer"},
                            "FavoriteCount": {"type": "integer"},
                            "Score": {"type": "integer"},

                            "Id": {"type": "keyword"},
                            "PostTypeId": {"type": "keyword"},
                            "OwnerUserId": {"type": "keyword"},
                            "LastEditorUserId": {"type": "keyword"},
                            "AcceptedAnswerId": {"type": "keyword"},
                            "LastEditorDisplayName": {"type": "keyword"},
                            "OwnerDisplayName": {"type": "keyword"}
                        }
                    }
                }
            },
        )

    # actions = []
    # f = open(DATA_DIR + QUESTION_FILE)
    # i = 0
    # # k = 0
    # time_start = time.time()
    # for line in f:
    #     # k = k + 1
    #     # if k > 541000:
    #     #     break
    #     decode_json = json.loads(line)
    #     action = {
    #         "_index": INDEX_NAME,
    #         "_type": TYPE_NAME,
    #         "_id": decode_json['Id'],
    #         "_source": decode_json
    #     }
    #     actions.append(action)
    #     if(len(actions) == 10000):
    #         i = i + 1
    #         time_inter = time.time()
    #         spend_time = time_inter - time_start
    #         time_start = time_inter
    #         print(i * 10000, "  ", 10000 / spend_time)
    #         helpers.bulk(ES, actions)
    #         del actions[0:len(actions)]
    # if (len(actions) > 0):
    #     helpers.bulk(ES, actions)
    # f.close()


def update_ans(ES):
    INDEX_NAME = 'answer'
    TYPE_NAME = 'stackoverflow'
    if not ES.indices.exists(index=INDEX_NAME):
        index_body = {
            'settings': {
                'number_of_shards': 5,
                'number_of_replicas': 1,
            },
            "mappings": {
                TYPE_NAME: {
                    "properties": {
                        'Id': {
                            'type': 'keyword'
                        },
                        "ParentId": {
                            "type": "keyword",
                        },
                        'Body': {
                            'index': False,
                            'type': 'text',
                        },
                        "LastActivityDate": {
                            "type": "date",
                            'index': False,
                        },
                        "CommentCount": {
                            "type": "integer",
                            'index': False,
                        },
                        "Score": {
                            "type": "integer",
                            'index': False,
                        },
                        "PostTypeId": {
                            "type": "keyword",
                            'index': False,
                        },
                        "OwnerUserId": {
                            "type": "keyword",
                            'index': False,
                        },
                        "LastEditorUserId": {
                            "type": "keyword",
                            'index': False,
                        },
                        "LastEditorDisplayName": {
                            "type": "keyword",
                            'index': False,
                        }
                    }
                }
            }
        }
        ES.indices.create(index=INDEX_NAME, body=index_body)

    # actions = []
    # f = open(DATA_DIR + ANSWER_FILE)
    # i = 0
    # # k = 0
    # time_start = time.time()
    # for line in f:
    #     # k = k + 1
    #     # if k > 541000:
    #     #     break
    #     decode_json = json.loads(line)
    #     action = {
    #         "_index": INDEX_NAME,
    #         "_type": TYPE_NAME,
    #         "_id": decode_json['Id'],
    #         "_source": decode_json
    #     }
    #     actions.append(action)
    #     if(len(actions) == 10000):
    #         i = i + 1
    #         time_inter = time.time()
    #         spend_time = time_inter - time_start
    #         time_start = time_inter
    #         print(i * 10000, "  ", 10000 / spend_time)
    #         helpers.bulk(ES, actions)
    #         del actions[0:len(actions)]
    # if (len(actions) > 0):
    #     helpers.bulk(ES, actions)
    # f.close()


def main():
    return update_data()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='insert data into ES',
        usage='''
        ./update_data.py -i data_dir
        ''', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', type=str, help='data path', default=DATA_DIR)
    args = parser.parse_args()
    DATA_DIR = args.i
    message = main()
    print(message)
