#!/usr/bin/env python3
import sys
try:
    salary=int(sys.argv[1])
except ValueError:
    print("Parameter Error")
    sys.exit()
income_tax=salary-5000
tax=0
if income_tax<=3000:
    tax=income_tax*0.03-0
    print("{:.2f}".format(tax))
elif income_tax>3000 and income_tax<=12000:
    tax=income_tax*0.10-210
    print("{:.2f}".format(tax))
elif income_tax>12000 and income_tax <=25000:
    tax=income_tax*0.20-1410
    print("{:.2f}".format(tax))
elif income_tax>25000 and income_tax <= 35000:
    tax=income_tax*0.25-2660
    print("{:.2f}".format(tax))
elif income_tax>35000 and income_tax <=55000:
    tax=income_tax*0.30-4410
    print("{:.2f}".format(tax))
elif income_tax>55000 and income_tax <=80000:
    tax=income_tax*0.35-7160
    print("{:.2f}".format(tax))
else:
    tax=income_tax*0.45-15160
    print("{:.2f}".format(tax))

