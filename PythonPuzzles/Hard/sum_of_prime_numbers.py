#Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

#Create a function that determines if a number is prime
def prime_seek(num):
    if num == 1:
        return "num is not a prime number"
    max_test = round(num/2)
    counter = 2
    while counter <= max_test:
        if num%counter == 0:
            return "num is not a prime number"
        counter += 1
    return "num is a prime number"

#print(prime_seek(4))

#now make the function that adds...
def sum_primes(lst):
    sum = 0
    #sum_save = 0 //used for testing errors, good for seeing how program works
    if not lst:
        return ('None')
    for x in lst:
        if x == 1:
            sum += 0
        else:
            add = 1
            max_test = round(x/2)
            #print("max test is: " + str(max_test)) //used for testing errors, good for seeing how program works
            counter = 2
            while counter <= max_test:
                if x%counter == 0:
                    sum += 0
                    add = 0
                counter = counter + 1
            if add == 1:
                #sum_save = sum //used for testing errors, good for seeing how program works
                sum += x
                #print(str(sum_save) + " plus " + str(x) + " = " + str(sum)) //used for testing errors, good for seeing how program works
    return sum


print(sum_primes([1,2,3,4,5,6,7,8,9,10]))
print(sum_primes([2,3,4,11,20,50,71]))
print(sum_primes([19,21,24,27,30,37]))
print(sum_primes([69,79,87,97,101]))
print(sum_primes([53,59,28,50,45,33,61]))
print(sum_primes([11,11,11,11,11,22,22,22]))
print(sum_primes([67,24,58,28,71,73,99]))
print(sum_primes([]))