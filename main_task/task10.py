def calculate_stock(x):
    total_stock = 0
    for i in x: 
      stock = int(i[2])
      total_stock+= stock
    return total_stock
      
    

prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45kshs","359"], ["coffee","5kshs","79"],["millet", "100kshs", "1000"]]
# total_stock=0

# for i in prods:
#    stock = int(i[2])
#    total_stock+=stock
total_stock = calculate_stock(prods)
print(total_stock)

