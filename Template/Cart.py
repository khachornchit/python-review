from string import Template

def Main():
    carts = []
    carts.append(dict(item='Coke', price=8, qty=2))
    carts.append(dict(item='Cake', price=12, qty=1))
    carts.append(dict(item='Fist', price=32, qty=4))

    template = Template("$item x $qty = $price")
    total = 0
    print("Cart :")
    for data in carts:
        print(template.substitute(data))
        total += data['price']
    print("Total price: " + str(total))

if __name__ == '__main__':
    Main()