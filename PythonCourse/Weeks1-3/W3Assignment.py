print("Welcome to the Program")
companyName = input("Input the company name: ")
fiberOptic = input("Input the number of feet of fiber optic to be installed: ")
totalCost = 0.0
totalCost = float(fiberOptic)*0.87 #had to type cast fiberOptic as a float to get to work
print(f"the name of the company is {companyName} and the total cost is ${totalCost}")

