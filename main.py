from bs4 import BeautifulSoup
from colorama import Fore
import requests


class scraper:
    def __init__(self) -> None:
        self.URL = "https://www.tgju.org/"
        
        self.RESPONSE = requests.get(self.URL)
        self.RESPONSE_CONTENT = self.RESPONSE.content

        self.SOUP = BeautifulSoup(self.RESPONSE_CONTENT, "html.parser")
        
    def get_dollar_info(self):
        self.Parent_div = self.SOUP.find("div", attrs={'class':'col-12 col-lg-12 col-xl-6 index-tabs-data-col-1'})
        self.Parent_table = self.Parent_div.find("table", attrs={'class':'dataTable index-tabs-table data-table market-section-right market-table mobile-half'})
        self.rows = self.Parent_table.find_all("tr", attrs={'class':'pointer'})
        
        self.DOLLAR_INFO = self.rows[0]
        
        self.DOLLAR_PRICE = self.DOLLAR_INFO.find("td", attrs={'class':'market-price'}).text
        self.DOLLAR_PRICE_LOWEST = self.DOLLAR_INFO.find("td", attrs={'class':'market-low'}).text
        self.DOLLAR_PRICE_HIGHEST = self.DOLLAR_INFO.find("td", attrs={'class':'market-high'}).text

        self.INFO = {
            "Price" : self.DOLLAR_PRICE,
            "Lowest" : self.DOLLAR_PRICE_LOWEST, 
            "Highest" : self.DOLLAR_PRICE_HIGHEST
        }

        return self.INFO


if __name__ == "__main__":
    SCRAPER = scraper()
    DOLLAR_INFO = SCRAPER.get_dollar_info()
    
    DOLLAR_PRICE = DOLLAR_INFO['Price'].replace("\n", "", -1)
    DOLLAR_LOWEST = DOLLAR_INFO['Lowest'].replace("\n", "", -1)
    DOLLAR_HIGHEST = DOLLAR_INFO['Highest'].replace("\n", "", -1)
    
    print(Fore.YELLOW + "Dollar Price : " + Fore.CYAN + DOLLAR_PRICE)
    print(Fore.YELLOW + "Dollar Highest : " + Fore.CYAN + DOLLAR_HIGHEST)
    print(Fore.YELLOW + "Dollar Lowest : " + Fore.CYAN + DOLLAR_LOWEST)