alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# adding to dictionary...
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# can start with an empty dictionary...
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
# modifying dictionary values...
alien_0['color'] = 'yellow'
print(alien_0)
# removing key value pairs
del alien_1['points']
print(alien_1)