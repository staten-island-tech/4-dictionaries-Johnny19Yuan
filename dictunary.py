microcenter = [{
    "name": "Acer Nitro 15",
    "price": "499.99",
    "specs": "Intel Core i5 13420H, RTX 3050, 15.3 Inch 144Hz IPS display",
},{
    "name": "Acer Nitro 16",
    "price": "749.99",
    "specs": "Ryzen 5 9450, RTX 4050, 16.2 Inch 144Hz IPS display" ,
},{
    "name": "Lenovo Legion Pro 7",
    "price": "1999.99",
    "specs": "Intel Core Ultra 9 275HX, RTX 5070Ti, 16.2 Inch 144Hz OLED display",
},{
    "name": "MSI Titan 18 HX AI",
    "price": "4299.99",
    "specs": "Intel Core Ultra 9 285HX, RTX 5090, 18 Inch UHD+ Mini-LED display", 
},{
    "name": "RTX 5060",
    "price": "349.99",
    "specs": "Nvidia RTX 5060 with raytracing and DLSS upscaling",
},{
    "name": "RTX 5050",
    "price": "299.99",
    "specs": "Nvidia RTX 5050 with raytracing and DLSS upscaling",
},{
    "name": "",
    "price": "349.99",
    "specs": "Nvidia RTX 5060 with raytracing and DLSS upscaling",
}]
total = 0 
cart = []
checkout = "n"
while checkout == "n":
    print("Welcome to Microcenter!")
    for index, item in enumerate(microcenter):
        print(index, ":", item["name"])
    useritem = int(input("What would you like? Please input a number: "))
    cart.append(microcenter[useritem]["name"])
    total += (float(microcenter[useritem]["price"]))
    print(f"Your cart: {cart}") 
    checkout = input("Do you want to check out? y To checkout,  n To contunue shopping, or r to remove item: ")
    if checkout == "r":
        x = -1
        for index in range(len(cart)):
            x = x+1
            print(f"{x} : {cart[x]}")
        remove = int(input("what item do you want to remove: "))
        total = total - float(microcenter[remove]["price"])
        cart.pop(remove)
        checkout = "n"
print("checkout")
print(f"you bought: {cart}")
pay_me_now = round(total, 2)
print(f"Your total is ${pay_me_now}")