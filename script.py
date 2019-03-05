import pandas as pd

# load csv
inventory = pd.read_csv('inventory.csv')
# print(inventory.head(3))

# get all rows at location Staten Island
staten_island = inventory[inventory.location == 'Staten Island']
# print(staten_island)

# load all product descriptions
product_request = staten_island['product_description']
# print(product_request)

# Show all seeds and planters for in Brooklyn
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')
                         | (inventory.product_type == 'planter') & (inventory.location == 'Brooklyn')]
print(seed_request)

# Add new column 'in_stock' that is either True or False based on the quantity column
inventory['in_stock'] = inventory.apply(lambda x: True if x.quantity > 0 else False, axis=1)
# print(inventory.head(3))

# Add new column 'total_value' that uses an in-line lambda function to multiply quantity by price
inventory['total_value'] = inventory.apply(lambda x: x.quantity * x.price, axis=1)
# print(inventory.head(3))

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

# add new column 'full_description' that uses lambda function to create a full product description
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
# print(inventory.head())
