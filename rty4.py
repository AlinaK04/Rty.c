import urllib
import urllib.request
import os
import re
import sys
import string
import unicodedata
import getopt
from xml.dom import minidom

def usage():
    print("Usage:\npython script.py [-uh] <search-regexp>")

try:
    opts, args = getopt.getopt(sys.argv[1:], "uh", ["urls", "help"])
except getopt.GetoptError as e:
    print(str(err))
    usage()
    sys.exit(2)
    
include_urls = False
for o, a in opts:
    if o == "-u":
        include_urls = True
    elif o in ("-h", "--help"):
        usage()
        sys.exit()
    else:
        assert False, "unhandled option"

searcher = re.compile(args[0], re.IGNORECASE)
for url in os.environ["RSS_FEED"].split():
    feed = urllib.request.urlopen(url)
    try:
        dom = minidom.parse(feed)
        forecasts = []
        for node in dom.getElementsByTagName('title'):
            txt = node.firstChild.wholeText
            if searcher.search(txt):
                #txt = unicodedata.normalize('NFKD', txt).encode('ascii', 'ignore')
                print(txt)
                if include_urls:
                    p = node.parentNode
                    link = p.getElementsByTagName('link')[0].firstChild.wholeText
                    print("\t%s" % link)
    except:
        sys.exit(1)
