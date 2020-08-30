"""Gets and prints the Title and Price of Amazon products from Amazon.in

@author : Sreedev S

Parameters
----------
filename : str
    The file location of the urls

Returns
-------
list
    a list of strings representing the Title and Price of Products
"""


import sys

def main(filename):

    import requests
    from bs4 import BeautifulSoup

    #use your user-agent . If you don't know search in Google "My user agent"
    header =  {"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    file1 = open(filename, 'r') 
    urls = file1.readlines() 
    #iterating through the urls provided in the file
    for URL in urls:
        #checking whether URL is valid or not
        if URL == '\n':
            continue
        try:
            page = requests.get(URL, headers=header)
        except:
            print("Unreachable or Invalid URL")
            continue

        
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id="productTitle").get_text()
        #Checking whether price detail is given for the product
        try:
            price = soup.find(id="priceblock_ourprice").get_text()
            price = price[1:]
        except:
            price = "Price Not Found"

        print(title.strip())
        print(price.strip())


if __name__ == "__main__":
    #Checking whether the filename is passed as an argument
    if len(sys.argv[1]) > 1:
       main(sys.argv[1])
    else:
        print("usage: python scrapper.py filename.txt")
