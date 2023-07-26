def card_hide(card):
    str_card = str(card)
    last_4 = str_card[-4:]
    to_mask = str_card[:-4]
    length_to_mask = len(to_mask)
    mask = '*' * length_to_mask #apparently this is a thing
    return(mask+last_4)

print(card_hide(1234123456785678))
print(card_hide(8754456321113213))
print(card_hide(35123413355523))
    


