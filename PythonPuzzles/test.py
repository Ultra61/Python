def next_in_line(lst, num):
    lst.append(num)
    print(lst)
    lst.pop(0)
    print(lst)
    
next_in_line([1,4,5,6], 8)
    