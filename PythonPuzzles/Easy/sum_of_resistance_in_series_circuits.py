#sum of resistance in a series circuits
"""
When resistors are connected together in series, the same current passes through
each resistor in the chain and the total resistance, 
RT, of the circuit must be equal to the sum of all the individual resistors added together
"""

def series_resistance(lst):
    counter = 0 
    resistance = 0
    while counter < len(lst):
        resistance += lst[counter] 
        counter += 1
    if resistance <= 1:
        concat = " ohm"
    else:
        concat = " ohms"
    resistance = str(resistance)
    output = resistance + concat 
    return output
    
print(series_resistance([1, 5, 6]))
    
