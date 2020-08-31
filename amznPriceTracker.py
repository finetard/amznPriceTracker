"""Gets and prints the Title and Price of Amazon products from Amazon.in

@author : Sreedev S

Parameters
----------
filename : str
    The file name of the file containing urls

Returns
-------
file : priceDetails.txt
    A file containing Name of the item, category of item, and price
"""


import sys

def main(filename):

    import requests
    from bs4 import BeautifulSoup

    #use your user-agent . If you don't know search in Google "My user agent"
    header =  {"User-Agent":'fill in your user agent'}

    file1 = open(filename, 'r') 
    urls = file1.readlines() 
    file1.close()
    file2 = open('priceDetails.txt','w')
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

        title = soup.find(id="productTitle").get_text().strip()
        #category = soup.find("span", class_="cat-link")
        #if category == None:
        category = soup.find_all('a', class_='a-link-normal a-color-tertiary')
        #Checking whether price detail is given for the product
        try:
            price = soup.find(id="priceblock_ourprice").get_text()
            price = price[1:]
        except:
            price = "Price Not Found"
        file2.writelines(title + '\n')
        for cat in category:
            file2.writelines(cat.get_text().strip() + '\n')
        file2.writelines(price.strip() + '\n') 
    file2.close()
if __name__ == "__main__":  
    #Checking whether the filename is passed as an argument
    if len(sys.argv) > 1:
       main(sys.argv[1])
    else:
        print("usage: python scrapper.py filename.txt")
