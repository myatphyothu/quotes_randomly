
import os,sys,datetime
from requests import get
from bs4 import BeautifulSoup
from warnings import warn


MAIN_URL = 'http://quotes.toscrape.com/page/'
HEADERS = {"Accept-Language": "en-US, en;q=0.5"}
container_class = "quote"

CONFIG = {
    "URL": 'http://quotes.toscrape.com/page/',
    "FIND WHAT?": "div",
    "CLASS": "quote"
}


def show_quotes(quotes):
    for i,quote in enumerate(quotes):
        print("[%d] %s" % (i, quote))
        
def run():
    REQs = 1
    more_pages = True
    quotes = []
    while more_pages:
        
        url = os.path.join(CONFIG["URL"], "%d"%REQs)
        response = get(url, headers=HEADERS)
        rc = response.status_code

        if rc != 200:
            warn("request{}: status{}".format(REQs, rc))
        else:
            print ("crawinling page %d..." % REQs)
            page_html = BeautifulSoup(response.text, "html.parser")
            containers = page_html.find_all(CONFIG["FIND WHAT?"], class_=CONFIG["CLASS"])
            # content based flow
            if len(containers) > 0:
                quotes.extend([container.span.text for container in containers])
                REQs += 1
            else:
                more_pages = False
            
            
    show_quotes(quotes)
    print("final page is", REQs-1)


if __name__ == "__main__":
    run()