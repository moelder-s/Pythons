price1 = float(input("Enter price of product1: "))
qnty1 = float(input("Enter qnty of product1: "))

price2 = float(input("Enter price of product2: "))
qnty2 = float(input("Enter qnty of product2: "))

price3 = float(input("Enter price of product3: "))
qnty3 = float(input("Enter qnty of product3: "))

delivery_charge = float(input("Enter delivery charge: "))
dis_per = float(input("Enter Dis per: "))

full_price = (price1 * qnty1) + (price2 * qnty2) + (price3 * qnty3) + delivery_charge
dis_per = (10 / 100)
total = full_price - (full_price * dis_per)

print("Full price is=", full_price)
print("Dis per is=", dis_per)
print("Total is=", total)
