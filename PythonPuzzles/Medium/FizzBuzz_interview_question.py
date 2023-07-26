def fizz_buzz(num):
    if num%3 == 0:
        mod3 = 1 #True 
    else:
        mod3 = 0 #False
    if num%5 == 0:
        mod5 = 1 #True 
    else:
        mod5 = 0 #False
#if both true return FizzBuzz
    if (mod3 == 1) and (mod5 == 1):
        return("FizzBuzz")
#if one true find out which and return accordingly
    elif (mod3 == 1) or (mod5 == 1):
        if (mod3 == 1):
            return("Fizz")
        else:
            return("Buzz")
#if it is not divisible by 3 or 5 return the original number as a string 
    else:
        return(str(num))
           
print(fizz_buzz(10))
        
