items = [{
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
},
{
    "name": "TCL 60\" 4K UHD TV",
    "price": 607.99,
    "department": "Televisions",
    "description": "60-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}]

print (items[0]["description"])

for index, item in enumerate(items):
    print(index, ":", item["name"])