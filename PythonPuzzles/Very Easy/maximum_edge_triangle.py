#create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers
def next_edge(side1, side2):
    max_length = (side1 + side2) - 1
    return max_length
print(next_edge(1,3))