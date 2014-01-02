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

def process_results(contents, pricelist, datelist):
    for count, item in enumerate(contents):
        print(contents[count], pricelist[count], datelist[count])

def extract_listings(request):
    soup = BeautifulSoup(request.text)
    results = []
    pricelist = []
    contents = []
    datelist = []
    print(soup.title.string)
    first_link = soup.find("p",class_="row")
    results.append(first_link)
    for item in first_link.find_next_siblings("p"):
        results.append(item)

    for listing in results:
        rowsoup = BeautifulSoup(str(listing))
        prices = str(rowsoup("span","price"))[22:-8]
        dates = str(rowsoup("span", "date"))[20:-8]
        link = str(rowsoup("a")[1].contents)
        contents.append(link)
        pricelist.append(prices)
        datelist.append(dates)
    # for i in range(7):
    #     print(pricelist[i], end=' ')
    #     print(str(contents[i]))
    process_results(contents, pricelist,datelist)

def main(argv):
    global url
    if len(argv) >= 2:
        url = argv[1]
    page = get_page(url)
    extract_listings(page)

if __name__ == "__main__":
    main(sys.argv)
