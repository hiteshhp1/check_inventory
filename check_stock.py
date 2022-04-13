import requests
from bs4 import BeautifulSoup


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    print("\n")
    return page.content


def tesco_check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.find(class_="product-info-message with-warning-background")
    print("Tesco\n")
    print(out_of_stock_divs)


def asda_check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.find(class_="asda-pill asda-pill--warning unavailable-banner__product-status")
    #out_of_stock_divs = soup.findAll("div", {"class": "pdp-main-details__actions-cntr"})
    print("ASDA\n")
    print(out_of_stock_divs)
    

def check_inventory():
    
    
    url = "https://groceries.asda.com/product/cooking-oil/asda-sunflower-oil/1000314748695" 
    page_html = get_page_html(url)
    asda_check_item_in_stock(page_html)

    url = "https://www.tesco.com/groceries/en-GB/products/271168790" 
    page_html = get_page_html(url)
    tesco_check_item_in_stock(page_html)


    


    

check_inventory()