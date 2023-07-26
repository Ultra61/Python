print("Welcome to the Program")
companyName = input("Input the company name: ")
fiberOptic = input("Input the number of feet of fiber optic to be installed: ")
totalCost = 0.0
if (float(fiberOptic) > 0) & (float(fiberOptic) <= 100):
    totalCost = float(fiberOptic)*0.87
elif (float(fiberOptic) > 100) & (float(fiberOptic) <= 250):
    totalCost = float(fiberOptic)*0.80
elif (float(fiberOptic) > 250) & (float(fiberOptic) <= 500):
    totalCost = float(fiberOptic)*.70
elif (float(fiberOptic) > 500):
    totalCost = float(fiberOptic)*.50
else:
    print("error: please insert a valid number and try again")
print(f"the name of the company is {companyName} and the total cost is ${totalCost}")

