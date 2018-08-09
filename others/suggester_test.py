#!/usr/bin/python
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import time

ES_USERNAME = 'elastic'
ES_PASSWORD = 'elastic'
INDEX_NAME = 'suggestion'
TYPE_NAME = 'suggestion'
FILENAME = r'../relevance/question'

time_start = time.time()

es = Elasticsearch(http_auth=(ES_USERNAME, ES_PASSWORD),
                   timeout=10)  # user/passwd
index_body = {
    "settings": {
        "index": {
            "number_of_shards": 1,
            "analysis": {
                "analyzer": {
                    "trigram": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["standard", "shingle", "synonym"]
                    },
                    "reverse": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["standard", "reverse"]
                    },
                    "reversePost": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["standard", "reverse", "synonym"]
                    }
                },
                "filter": {
                    "shingle": {
                        "type": "shingle",
                        "min_shingle_size": 2,
                        "max_shingle_size": 3
                    },
                    "synonym": {
                        "type": "synonym",
                        "synonyms_path": "spellCheck/synonym.txt",
                        "tokenizer": "whitespace"
                    }
                }

            }
        }
    },
    "mappings": {
        TYPE_NAME: {
            "properties": {
                "Title": {
                    "type": "text",
                    "fields": {
                        "trigram": {
                            "type": "text",
                            "analyzer": "trigram"
                        },
                        "reverse": {
                            "type": "text",
                            "analyzer": "reverse"
                        }
                    }
                }
            }
        }
    }
}

if es.indices.exists(index=INDEX_NAME) is not True:
    es.indices.create(index=INDEX_NAME, body=index_body)


def insert_data():
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
            "_source": {"Title": line_dict['Title']}

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


def search_Title(q):
    search_body = {
        "suggest": {
            "text": q,
            "simple_phrase": {
                "phrase": {
                    "field": "Title.trigram",
                    "size": 1,
                    "gram_size": 3,
                    "direct_generator": [{
                        "field": "Title.trigram",
                        "suggest_mode": "popular",
                    },
                    {
                        "field": "Title.reverse",
                        "suggest_mode": "popular",
                        "pre_filter": "reverse",
                        "post_filter": "reverse"

                    }
                    ],
                    "highlight": {
                        "pre_tag": "<em>",
                        "post_tag": "</em>"
                    }
                }
            }
        }
    }
    result = es.search(index=INDEX_NAME,
                       doc_type=TYPE_NAME,
                       body=search_body)
    suggest_best = None
    for hit in result['suggest']['simple_phrase']:
        input_text = hit['text']
        options = hit['options']
        print("input:" + '\t' + input_text, flush=True)
        for i, option in enumerate(options):
            print("suggestion {}:".format(i + 1) +
                  '\t' + option['text'], flush=True)
        print('***********************************')

    suggest_list = result['suggest']['simple_phrase'][0]['options']
    if len(suggest_list) != 0:
        suggest_best = suggest_list[0]['text']
    return suggest_best


if __name__ == '__main__':
    insert_data()
    # search_Title('Jeva lib or app convet to xml')
    # search_Title('jeva nul point exseption')
    # search_Title('how to separite interger into digits ')
    # search_Title('waht is premitive ')
    # search_Title('how to set a field use java reflection')
    # search_Title('code examplt dijstra algorithm')
    # search_Title('how to spel check in java')
    # search_Title('how to spel ')
    # search_Title('spelling check implemantation in java ')
