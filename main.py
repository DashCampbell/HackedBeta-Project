
# Get data from user input
# data is [price, product name, product link]

from bs4 import BeautifulSoup as BS
from requests_html import AsyncHTMLSession
from requests_html import HTMLSession

URL = "https://www.walmart.ca/en/search?q=iphone"
url2 = "https://www.bestbuy.ca/en-ca/search?search=iphone"

session = HTMLSession()
asession = AsyncHTMLSession()

async def get_walmart():
    r = await asession.get(url2)
    e = r.html.find("#__next")
    print(r.html)
    return r
    
result = asession.run(get_walmart)

