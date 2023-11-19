trustedBrands = ['Apple', 'Amazon CA', 'The Source', 'Walmart.ca', 'Best Buy Canada']

def filterProducts(products):
    filteredItems = {}
    for brand in products:
        if brand in trustedBrands:
            filteredItems[brand] = products[brand]
    return filteredItems