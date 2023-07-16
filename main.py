import json

if __name__ == "__main__":

    # # Task 1+2
    # with open ('products.json') as f:
    #     products = json.load(f)
    #
    # products.sort(key=lambda x : x['price'])
    # print(products)
    #
    # expensiveProducts = []
    # for product in products:
    #     if product['price'] >= 400:
    #         expensiveProducts.append(product)
    # print(expensiveProducts)

    # Task 3

    products = {
        'dresses': 12,
        'shoes': 8,
        'shorts': 10,
        'shirts': 21,
        'hats': 3
    }

    for product in products:
        if products.get(product)<10:
            print("Not enough ", product)



