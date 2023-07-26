"""
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
"""

#Create a function that will take a HEX number and returns the binary equivalent (as a string)

def to_binary(hex):
    hex = hex[2:]
    l = len(hex)
    binary = ""
    counter = 0
    while counter < l:
        if hex[counter] == '0':
            binary = binary + '0000'
        if hex[counter] == '1':
            binary = binary + '0001'
        if hex[counter] == '2':
            binary = binary + '0010'
        if hex[counter] == '3':
            binary = binary + '0011'
        if hex[counter] == '4':
            binary = binary + '0100'
        if hex[counter] == '5':
            binary = binary + '0101'
        if hex[counter] == '6':
            binary = binary + '0110'
        if hex[counter] == '7':
            binary = binary + '0111'
        if hex[counter] == '8':
            binary = binary + '1000'
        if hex[counter] == '9':
            binary = binary + '1001'
        if hex[counter] == 'A':
            binary = binary + '1010'
        if hex[counter] == 'B':
            binary = binary + '1011'
        if hex[counter] == 'C':
            binary = binary + '1100'
        if hex[counter] == 'D':
            binary = binary + '1101'
        if hex[counter] == 'E':
            binary = binary + '1110'
        if hex[counter] == 'F':
            binary = binary + '1111'
        binary += " "
        counter += 1
    return binary

print(to_binary("0x1F"))
print(to_binary("0xFF"))
print(to_binary("0xAA"))
print(to_binary("0xC46E"))
