from elasticsearch import Elasticsearch

INDEX_NAME = 'question2'
TYPE_NAME = 'java'

# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'))


def search_all():
    _search_body = {
        "query": {
            "match_all": {}
        }
    }
    searched = es.search(index=INDEX_NAME, doc_type=TYPE_NAME,
                         body=_search_body, search_type='dfs_query_then_fetch')
    result = search_result(searched)
    print(searched)
    return result


def search_title_body_tags(k):
    _search_body = {
        "query": {
            "bool": {
                # "filter": [
                #     {"range": {
                #         "score": {
                #             "gte": -1
                #         }
                #     }},
                #     {"range": {
                #         "answercount": {
                #             "gte": 1
                #         }
                #     }
                #     }
                # ],
                "should": [
                    {
                        "match": {
                            "Title": {
                                "query": k,
                                "boost": 3
                            }
                        }
                    },
                    {
                        "match": {
                            "Body": {
                                "query": k,
                                "boost": 1,
                            }
                        }
                    },
                    {
                        "match": {
                            "Tags": {
                                "query": k,
                                "boost": 4
                            }
                        }
                    }
                ]
            }
        }

    }
    searched = es.search(index=INDEX_NAME, doc_type=TYPE_NAME,
                         body=_search_body, search_type='dfs_query_then_fetch')
    result = search_result(searched)
    print(searched)
    return result


def search_result(_searched):
    result = []
    for hit in _searched['hits']['hits']:
        result.append(hit['_source'])
    return result


if __name__ == '__main__':
    search_title_body_tags("java")
