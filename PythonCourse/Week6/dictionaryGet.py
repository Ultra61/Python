# can use get to access values in dictionaries
# can also use to set something to return if key is not found
# returning something else prevents errors that would otherwise occur
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])
point_value = alien_0.get('speed', 'No point value assigned')
print(point_value)