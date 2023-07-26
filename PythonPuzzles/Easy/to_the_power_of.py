
#create a function that takes a base number and an exponent number and returns the calculation
def calculate_exponent(num, exp):
    counter = exp
    result = num
    while counter > 1:
        result = result * num 
        counter = counter - 1
    return result

test = calculate_exponent(3, 3)
print(test)