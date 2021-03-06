from elasticsearch import Elasticsearch

INDEX_NAME = 'economy'
TYPE_NAME = 'realestate'
FILENAME = r'realestate'  # json source file

# ES connection http_auth=(user,passwd)
es = Elasticsearch(http_auth=('elastic', 'elastic'))  # user/passwd
index_mappings = {
    "mappings": {
        "realestate": {
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
                        },
                        "image_url": {
                            "type": "keyword"
                        },
                        "price": {
                            "type": "float"
                        },
                        "addr": {
                            "type": "text",
                            "analyzer": "ik_max_word"
                        },
                        "is_new": {
                            "type": "keyword",
                        },
                        "Developer": {
                            "type": "text",
                            "analyzer": "ik_max_word",
                            "fields": {
                                "raw": {
                                    "type": "keyword"
                                }
                            }
                        }

                    }
                }

            }
        }
    }
}

if es.indices.exists(index=INDEX_NAME) is not True:
    es.indices.create(index=INDEX_NAME, body=index_mappings)

with open(FILENAME, 'r') as f:
    for line in f.readlines():
        list_line = line.split('\t')
        _index = INDEX_NAME
        _type = TYPE_NAME
        _id = list_line[1]
        _label = list_line[0]
        try:
            _attr = eval(list_line[2])
            _attr['price'] = eval(_attr['price'])
        except Exception as e:
            continue
        else:
            data = {"label": _label, "id": _id, "attr": _attr}
            es.create(index=_index, doc_type=_type, id=_id,
                      body=data)
