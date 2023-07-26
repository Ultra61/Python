#write a function that reverses a string. Make your function recursive
#all that this does is takes the first letter and moves it to the end everytime it goes through

def reverse(s):
    if s == "":
        return s 
    else:
        #[1:] is everything after and including [1] 
        #[0] is the first element of the string 
        return reverse(s[1:]) + s[0] #put the end of the string back through the reverse() function 

x = reverse("something")
print(x)
        
