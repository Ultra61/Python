#create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount
def dis(price, discount):
    discount = discount/100
    amount_saved = price * discount
    final_price = price - amount_saved
    final_price = round(final_price, 2)
    return(final_price)

print(dis(89, 20))