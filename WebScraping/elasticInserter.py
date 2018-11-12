# This Python file uses the following encoding: utf-8
# elasticInserter

import os, base64, re, logging
from elasticsearch import Elasticsearch

# Log transport details (optional):
#logging.basicConfig(level=logging.INFO)

# Parse the auth and host from env:
# bonsai = os.environ['BONSAI_URL']
# bonsai = "https://b2t36zjpm5:5xdwk88pm9@alertador-poc-1532934105.us-west-2.bonsaisearch.net"
# auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
# host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')
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

# es = elasticsearch.Elasticsearch([{'host': 'search-alertador-es4wk3fwnh2p6xl27hmp626k3e.us-west-2.es.amazonaws.com', 'port': 80}]) # use default of localhost, port 9200//
# es = elasticsearch.Elasticsearch([{'host': 'https://b2t36zjpm5:5xdwk88pm9@alertador-poc-1532934105.us-west-2.bonsaisearch.net', 'port': 80}]) # use default of localhost, port 9200//
# es.index(index='posts', doc_type=doctype,id=insertBody["jobID"], body=insertBody)
# pending to check if post exists to avoid duplicated

# import elasticsearch
# es = elasticsearch.Elasticsearch([{'host': 'https://b2t36zjpm5:5xdwk88pm9@alertador-poc-1532934105.us-west-2.bonsaisearch.net', 'port': 80}]) # use default of localhost, port 9200//
#
# def insertES(tweetID, insertBody):
#     # print 'inserting empleosMaquila'
#     # print insertBody
#
#
#
#
#     # Log transport details (optional):
#     logging.basicConfig(level=logging.NONE)
#
#     # Parse the auth and host from env:
#     # bonsai = os.environ['BONSAI_URL']
#     # bonsai = "https://b2t36zjpm5:5xdwk88pm9@alertador-poc-1532934105.us-west-2.bonsaisearch.net"
#     # auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
#     # host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')
#     host = "http://localhost:9200/tweets"
#     # Connect to cluster over SSL using auth for best security:
#     es_header = [{
#         'host': host,
#         'port': 443,
#         'use_ssl': True,
#         'http_auth': (auth[0], auth[1])
#     }]
#
#     # Instantiate the new Elasticsearch connection:
#     es = Elasticsearch(es_header)
#
#     # es = elasticsearch.Elasticsearch([{'host': 'search-alertador-es4wk3fwnh2p6xl27hmp626k3e.us-west-2.es.amazonaws.com', 'port': 80}]) # use default of localhost, port 9200//
#     # es = elasticsearch.Elasticsearch([{'host': 'https://b2t36zjpm5:5xdwk88pm9@alertador-poc-1532934105.us-west-2.bonsaisearch.net', 'port': 80}]) # use default of localhost, port 9200//
#     es.index(index='tweets', doc_type='tweet', id=tweetID, body=insertBody)
#
# # pending to check if post exists to avoid duplicated
