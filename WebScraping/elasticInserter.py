# This Python file uses the following encoding: utf-8
# elasticInserter

import os, base64, re, logging
from elasticsearch import Elasticsearch
 
host = "127.0.0.1"

# Connect to cluster over SSL using auth for best security:
es_header = [{
    'host': host,
    'port': 9200
    # ,
    # 'use_ssl': True,
    # 'http_auth': (auth[0], auth[1])
}]

# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)
#
#
# insertBody = {
#     "text": "Test Insert TW",
#     "created_at": '2018-11-11'
# }
# es.index(index='tweets', doc_type='tweet', id=1, body=insertBody)
#
# print ("test tweet inserted")

# es.ping()
 
