#Create a function that takes an integer n and returns the factorial of factorials
def fact_of_fact(num):
    if num == 1:
        return 1
    fact_fact = []
    while num > 1:
        fact_fact.append(num)
        num -= 1
    length = len(fact_fact)
    fact_store = []
    while length > 0:
        num = fact_fact[length - 1]
        counter = num - 1
        while counter > 1:
            num *= counter
            counter -= 1
        fact_store.append(num)
        length -= 1
    fact_x_fact = 1
    length = len(fact_store)
    while length > 0:
        fact_x_fact *= fact_store[length - 1]
        length -= 1
    return(fact_x_fact)

print(fact_of_fact(7))


# this was used to test multiplying numbers in an array
def m_test():
    fact_store = [2, 6, 24]
    fact_x_fact = 1
    length = len(fact_store)
    while length > 0:
        fact_x_fact *= fact_store[length - 1]
        length -= 1
    return(fact_x_fact)
#print(m_test())

#this is the original factorial function
def factorial(num):
    counter = num - 1
    while counter > 1:
        num *= counter
        counter -= 1
    return num 
#print(factorial(2))

#there is also the easy method...
import math
print(math.factorial(4))
#but this would have made the problem too easy
#also edabit may not accept this

