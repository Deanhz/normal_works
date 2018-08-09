#!/usr/bin/python
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import time
import sys
from os.path import realpath, join, dirname
sys.path.insert(0, join(dirname(realpath(__file__)), '../../src'))
from conf.es_setting import *

ES_USERNAME = 'elastic'
ES_PASSWORD = 'elastic'
INDEX_NAME = 'javatips'
TYPE_NAME = 'javatips'
FILENAME = r'../../../data_dir/javatips/full_data'

time_start = time.time()


def create_mapping(es):
    if es.indices.exists(index=INDEX_NAME):
        return
    index_body = {
        "settings": {
            'number_of_shards': 3,
            'number_of_replicas': 1,
            'analysis': STACKOVERFLOW_ANALYSIS
        },
        "mappings": {
            TYPE_NAME: {
                "properties": {
                    'Title': {
                        'type': 'text',
                        "analyzer": "english",
                    },
                    "Tags": {
                        "type": "text",
                        "analyzer": "english",
                    },
                    "ViewCount": {"type": "integer"},
                    "AnswerCount": {"type": "integer"},
                    "Score": {"type": "integer"},
                    "Id": {"type": "keyword"},
                    "AcceptedAnswerId": {"type": "keyword"},
                    "Body": {"type": "text"},
                    "ParentId": {"type": "keyword"}
                }
            }
        }
    }
    es.indices.create(index=INDEX_NAME, body=index_body)


def insert_data(es, filename):
    actions = []
    f = open(filename)
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


if __name__ == '__main__':
    es = Elasticsearch(http_auth=(ES_USERNAME, ES_PASSWORD), timeout=10)
    create_mapping(es)
    insert_data(es, FILENAME)
