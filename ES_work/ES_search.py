from elasticsearch import Elasticsearch

INDEX_NAME = 'economy'
TYPE_NAME = 'realestate'

# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'))

_query_all = {
    "query": {
        "match_all": {}
    }
}

_search_label = {
    "query": {
        "match": {
            "label": "沈阳",
            "analyzer": "ik_smart"
        }
    }
}

_search_term_label = {
    "query": {
        "term": {
            "label.raw": {
                "value": "沈阳新天地"
            }
        }
    }
}

_search_addr = {
    "query": {
        "match": {
            "attr.addr": "沈阳",
            "analyzer": "ik_smart"
        }
    }
}

_search_label_addr = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "attr.addr": "沈阳",
                        "analyzer": "ik_smart"
                    }
                },
                {
                    "match": {
                        "label": "花园",
                        "analyzer": "ik_smart"
                    }
                }
            ]
        }
    }
}

_search_new_filter_price = {
    "query": {
        "bool": {
            "filter": {
                "term": {
                    "attr.is_new": "在售"
                }
            },
            "must": [
                {
                    "range": {
                        "attr.price": {
                            "gte": 5000,
                            "lte": 10000
                        }
                    }
                }
            ]
        }
    }
}

_searched = es.search(index=INDEX_NAME, doc_type=TYPE_NAME,
                      body=_search_term_label)

# print search result
for hit in _searched['hits']['hits']:
    print(hit['_source'], flush=True)
    print('\n')
