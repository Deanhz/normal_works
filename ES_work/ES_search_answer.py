from elasticsearch import Elasticsearch
import sys

INDEX_NAME = 'answer'
TYPE_NAME = 'java'

# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'))


def search_parentid(p_id):
    _search_body = {
        "query": {
            "term": {
                "ParentId": {
                    "value": p_id
                }
            }
        }
    }
    searched = es.search(index=INDEX_NAME, doc_type=TYPE_NAME,
                         body=_search_body)
    result = search_result(searched)
    return result


def search_result(_searched):
    result = []
    for hit in _searched['hits']['hits']:
        result.append(hit['_source'])
        print(hit['_source'], flush=True)
        print('\n')
    return result


if __name__ == '__main__':
    if sys.argv[1:]:
        search_parentid(sys.argv[1])
    else:
        search_parentid('180297')
