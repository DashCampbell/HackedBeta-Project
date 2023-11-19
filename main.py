from webscraper import webScrape

products = webScrape("apple+watch+ultra+2")

'''for brand in products:
    print(brand)
    print(products[brand][0]['title'])
    print()'''

trustedBrands = ['Apple', 'Amazon CA', 'The Source', 'Walmart.ca']
for brand in products:
    if brand in trustedBrands:
        print(brand)
        print(products[brand][0]['title'])
        print()