import elasticInserter
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup
import re,sys,os,datetime


def parsePage(urlToParse):
    try:
        print urlToParse
        req = urllib2.Request(urlToParse, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        seccionDiario = con.read()  # urllib2.urlopen(urlToParse, headers={'User-Agent' : "Magic Browser"})
        soup = BeautifulSoup(seccionDiario, "html.parser")
        tempReturn = soup.findAll("div", {
            "id": "cont_aclasi2"})  # el diario es cholo y no usa el body tag!!! y les vale usar el mismo ID!
        print 'end retreiving html'
        return tempReturn
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print "error to parse jobid"
        pass


page = elasticInserter.es.search(
    index='tweets',
    doc_type='tweet',
    scroll='2m',
    size=1000,
    body={"query": {"match": {"text": "https"}}}
    )
sid = page['_scroll_id']
scroll_size = page['hits']['total']

# Start scrolling
while (scroll_size > 0):
    print "Scrolling..."
    page = elasticInserter.es.scroll(scroll_id=sid, scroll='2m')
    # Update the scroll ID
    sid = page['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(page['hits']['hits'])
    print "scroll size: " + str(scroll_size)
    # Do something with the obtained page
    for pageHit in page['hits']['hits']:
        tweet = pageHit['_source']['text']
        print tweet
        urlToParse = re.search("(?P<url>https?://[^\s]+)", tweet).group("url")
    print "end of page"
