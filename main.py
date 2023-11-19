from webscraper import webScrape

products = webScrape("apple+watch+ultra+2")

for brand in products:
    print(brand)
    print(products[brand][0]['title'])
    print()