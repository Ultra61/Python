def area_of_country(name, area):
    world_landmass = 148940000
    proportion = (area/world_landmass) * 100
    proportion = round(proportion, 2)
    proportion = str(proportion)
    return name + " is " + proportion + "% of the total world's landmass"

print(area_of_country("USA", 9372610))
print(area_of_country("Russia", 17098242))
print(area_of_country("Iran", 1648195))
print(area_of_country("India", 3287590))
print(area_of_country("China", 9706961))
print(area_of_country("Yemen", 527968))
print(area_of_country("Switzerland", 41284))
