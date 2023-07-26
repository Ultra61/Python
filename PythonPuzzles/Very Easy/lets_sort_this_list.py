"""
Create a function that takes a list of numbers lst, a string s 
and return a list of numbers as per the following rules
    "Asc" returns a sorted list in ascending order.
    "Des" returns a sorted list in descending order.
    "None" returns a list without any modification.
"""
#remember that the .sort() method modifies the original list!
def asc_des_none(lst, s):
    if s == "Asc":
        lst.sort() 
        return lst
    elif s == "Des":
        lst.sort(reverse=True)
        return lst
    else:
        return lst 
        
print(asc_des_none([1, 3, 5], "Asc"))
print(asc_des_none([1, 3, 5], "Des"))
print(asc_des_none([1, 3, 5], "None"))

