def next_in_line(lst, num):
    if lst == []:
        return "No list has been selected"
    else:
        lst.append(num)
        lst.pop(0)
        return(lst)
    
print(next_in_line([], 8))
    