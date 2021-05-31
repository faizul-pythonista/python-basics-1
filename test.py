Laptop = {
    'brand': 'HP',
    'model': 'ThinkPad',
    'price': 60000
}

print("HP Laptop " , Laptop)

Dell = Laptop.copy()

Dell.update({'brand': 'Dell', 'model': 'Lattidute', 'price': 80000, 'inStock': 40})

del Dell['inStock']

print("Dell Laptop" , Dell)

print('Dell price ', Dell['price'])

print('List of tupes ', list(Dell.items()))

print('List of keys ', Dell.keys())

# for m in range(1, 4):
#     print("mth value ", m)


n=5
for i in range(0, 5):
    for j in range(0,n-i):
        print("*", end=' ')
    print("--")

print("completed")



