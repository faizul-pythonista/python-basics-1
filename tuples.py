can = (1, 'ltr', 'green', 10.50, '20x6', 'cm')
print(can)

(capacity, unit, color, price, size, dimSize) = can
print("Capacity %s" % capacity)
print("can unit %s" % unit)
print("color %s " % color)
print("price %d " % price)
print("size %s" %size)
print("dimention unit %s"%dimSize)

print("can propertise count %d"%can.count('cm'))

print(type(can))

for prop in can:
    print(prop)