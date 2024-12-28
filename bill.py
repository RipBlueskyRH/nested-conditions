#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed.
#Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25.
#If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35.
#If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45.
#And above 200, the cost of the unit is 8.45, and the tax is 75.

a=int (input("how many units have you consumed?"))
if a<50:
    amount=a*2.60
    tax=25
elif a<=100:
    amount=50*2.60+(a-50)*3.25
    tax=35
elif a<=200:
    amount=50*2.60+50*3.25+(a-100)*5.26
    tax=45
else:
    amount=50*2.60+50*3.25+100*5.26+(a-200)*8.45
    tax=75

total_amount=amount+tax
print ("your amount due is", total_amount)