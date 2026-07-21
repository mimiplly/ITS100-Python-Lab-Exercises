#ITS100 Lecture4 Conditional Structure Lab4.5
# 687
amount = int(input("Enter the amount of money you would like to withdraw: "))
print("We may give you:")

amount_500 = amount // 500 # ได้ 1 ใบ 500
amount %= 500 # เอา 687 % 500 → เหลือ 187

amount_100 = amount // 100
amount %= 100

amount_50 = amount // 50
amount %= 50

amount_2 = amount // 2
amount %= 2

amount_1 = amount // 1
amount %= 1

print("%d bill(s) of 500 baht" % amount_500)
print("%d bill(s) of 100 baht" % amount_100)
print("%d bill(s) of 50 baht" % amount_50)
print("%d coin(s) of 2 baht" % amount_2)
print("%d coin(s) of 1 baht" % amount_1)       