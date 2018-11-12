import elasticInserter
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup
import re,sys,os,datetime


def insertES(tweetID, insertBody):
    try:
        # print insertBody
        elasticInserter.es.index(index='notas', doc_type='nota', id=int(tweetID), body=insertBody)
    except Exception as e:
        print(e)
        print "error to insert to ES"
        pass



#mydivs = soup.findAll("div", {"class": "stylelistrow"})
#diario,class="texto_nota clearfix", header h1
#la polaka, class="td-post-header", class="td-post-content"
#net noticias, class="nt-nota mtop", header h1


def getNotaClass(screen_name):
    switcher = {
        "@netnoticiasmx": "nt-nota mtop",
        "@diariodejuarez": "texto_nota",
        "@lapolaka": "td-post-content",
    }

    return switcher.get(screen_name, "nothing")


def getNotaHeader(screen_name, soup):
    if screen_name == "@netnoticiasmx" or screen_name == "@diariodejuarez":
        soupHeader = soup.find("h1")
    if screen_name == "@lapolaka":
        soupHeader = soup.find("div", {
            "class": "td-post-header"})
    return soupHeader.getText()


def parsePage(urlToParse, screen_name, tweet_id):
    try:
        req = urllib2.Request(urlToParse, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        pageData = con.read()  # urllib2.urlopen(urlToParse, headers={'User-Agent' : "Magic Browser"})
        soup = BeautifulSoup(pageData, "html.parser")

        notaBody = soup.find("div", {
            "class":  getNotaClass(screen_name)})
        notaHeader = getNotaHeader(screen_name, soup)
        nota = {
            "notaBody": notaBody.getText(),
            "notaHeader": notaHeader,
            "tweet_id": tweet_id,
            "screen_name": screen_name
        }


        return nota
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
        tweet_id = pageHit['_id']
        screen_name = pageHit['_source']['screen_name']
        urlToParse = re.search("(?P<url>https?://[^\s]+)", tweet).group("url")
        insertBody = parsePage(urlToParse, screen_name, tweet_id)
        insertES(tweet_id, insertBody)
    print "end of page"
