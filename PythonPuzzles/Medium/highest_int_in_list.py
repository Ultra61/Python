#Create a function that finds the highest integer in the list using recursion
def find_highest(lst):
    l = (len(lst) - 1)
    if l == 0:
        return lst[0]
    save = lst[l]
    while l > 0:
        l = l -1
        if lst[l] > save:
            save = lst[l]
    return save

print(find_highest([1, 2]))
print(find_highest([1]))
print(find_highest([-34, 8, 17, -98, 6, 45, -5]))