import requests
from bs4 import BeautifulSoup

class PriceComparisonApp:
    def __init__(self):
        self.product_name = ""
        self.product_prices = {}

    def get_user_input(self):
        self.product_name = input("Enter the product you want to compare: ")

    def scrape_amazon(self):
        # Example: Amazon scraper
        url = f"https://www.amazon.com/s?k={self.product_name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extracting product prices from Amazon
        prices = soup.select(".a-price .a-offscreen")
        if prices:
            self.product_prices["Amazon"] = float(prices[0].get_text().replace("$", ""))

    def scrape_walmart(self):
        # Example: Walmart scraper
        url = f"https://www.walmart.com/search/?query={self.product_name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extracting product prices from Walmart
        prices = soup.select(".price .visuallyhidden")
        if prices:
            self.product_prices["Walmart"] = float(prices[0].get_text().replace("$", ""))

    def compare_prices(self):
        if not self.product_prices:
            print("No prices found. Please check your input or try again later.")
            return

        lowest_price_provider = min(self.product_prices, key=self.product_prices.get)
        lowest_price = self.product_prices[lowest_price_provider]

        print("\nPrice Comparison:")
        for provider, price in self.product_prices.items():
            print(f"{provider}: ${price}")

        print(f"\nLowest Price: {lowest_price_provider} - ${lowest_price}")

    def run(self):
        print("Welcome to the Price Comparison App!")
        self.get_user_input()

        # Scraping prices from different websites
        self.scrape_amazon()
        self.scrape_walmart()

        # Comparing and displaying prices
        self.compare_prices()

if __name__ == "__main__":
    app = PriceComparisonApp()
    app.run()
