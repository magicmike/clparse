__author__ = 'dirk'

from datetime import datetime
import requests
import subprocess
import time
from bs4 import BeautifulSoup
import sys
import gmailsend

url = "http://ithaca.craigslist.org/rea"
filename = "houselistings.html"

def save_listings(contents):
    output = open(filename, "w")
    output.write(contents)
    output.close()
def get_page(url):
    return requests.get(url)
def extract_listings(request):
    soup = BeautifulSoup(request.text)
    links = []
    # tag = soup.span
    # tag['id'] = 'timestamp'
    # print(tag.text[:20])
    print(soup.title.string)
    for link in soup('a'):
        links.append(link)
    # for row in soup.find_all("p",class_="row"):
    #     rSoup = BeautifulSoup(row)
        # print(row_soup.find_all("span","price"))
    #prices = soup.find_all("span","price")
    first_link = soup.find("p",class_="row")
    print(first_link)
    results = first_link.find_next_siblings("p")
    for listing in results:
        rowsoup = BeautifulSoup(str(listing))
        prices = str(rowsoup("span","price"))[22:-8]
        print(prices)
        #print(listing)
    print(len(listing))



    #print(rows)
        


def main(argv):
    global url
    if len(argv) >= 2:
        url = argv[1]
    page = get_page(url)
    extract_listings(page)



if __name__ == "__main__":
    main(sys.argv)
