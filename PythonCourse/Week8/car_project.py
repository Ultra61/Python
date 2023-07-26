# Fun-O-Rama Garage Program
class Vehicle: # create Vehicle class

    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
        self.optionList = ["Bluetooth", "Cruise Control", "Backup Camera"]

    #create required methods and other methods to complete objectives
    def getMake(self):
        return self.make 

    def getModel(self): 
        return self.model
    
    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        return self.options

    def getOptionList(self):
        return self.optionList

    def setOptionList(self, optionList):
        self.optionList = optionList

class Car(Vehicle):

    def __init__(self, make, model, color, fuelType, options):
        super().__init__(make, model, color, fuelType, options)
        self.engineSize = 0
        self.numDoors = 0

    #create required methods and other methods to complete objectives
    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

    def setEngineSize(self, engineSize):
        self.engineSize = engineSize

    def setEngineSize(self, engineSize):
        self.engineSize = engineSize

    def setNumDoors(self, numDoors):
        self.numDoors = numDoors
        

class Pickup(Vehicle):

    def __init__(self, make, model, color, fuelType, options):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = 0
        self.bedLength = 0

    #create required methods and other methods to complete objectives
    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

    def setCabStyle(self, cabStyle):
        self.cabStyle = cabStyle

    def setBedLength(self, bedLength):
        self.bedLength = bedLength


def menu():
    
    car_list = []
    c_count = -1
    car_var = " "

    pickup_list = []
    p_count = -1
    pickup_var = " "

    menu = True
    while(menu):
        answer = input("Would you like a Car or a Pickup? C for Car/P for Pickup: ")
        if answer == "C":
            print("Creating Car...")
            # find some way to dynamically create variables and put them into a list so can use to create class objects
            c_count += 1
            car_var = ("car" + str(c_count))
            car_list.append(car_var)
            make = input("input the make: ")
            model =  input("input the model: ")
            color = input("input the color: ")
            fuelType = input("input fuel type: ")
            options = input("input options: Y for options/N for no options: ")
            # car_list[c_count] is the current car object being modified
            car_list[c_count] = Car(str(make), str(model), str(color), str(fuelType), str(options))
            # ask for options and put them into a list
            if options == "Y":
                options = []
                optionList = car_list[c_count].getOptionList()
                ans = input("would you like to add " + str(optionList[0]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[0]))
                ans = input("would you like to add " + str(optionList[1]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[1]))
                ans = input("would you like to add " + str(optionList[2]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[2]))
                car_list[c_count].setOptionList(options)
            # if no options wanted make the options list empty
            else:
                options = []
                car_list[c_count].setOptionList(options)
            engineSize = input("input the engine size: ")
            car_list[c_count].setEngineSize(engineSize)
            numDoors = input("input the amount of doors: ")
            car_list[c_count].setNumDoors(numDoors)
        elif answer == "P":
            print("Creating Pickup")
            p_count += 1
            pickup_var = ("pickup" + str(p_count))
            pickup_list.append(pickup_var)
            make = input("input the make: ")
            model =  input("input the model: ")
            color = input("input the color: ")
            fuelType = input("input fuel type: ")
            options = input("input options: Y for options/N for no options: ")
            # pickup_list[p_count] is the current Pickup object being modified
            pickup_list[p_count] = Pickup(str(make), str(model), str(color), str(fuelType), str(options))
            # ask for options and put them in a list
            if options == "Y":
                options = []
                optionList = pickup_list[p_count].getOptionList()
                ans = input("would you like to add " + str(optionList[0]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[0]))
                ans = input("would you like to add " + str(optionList[1]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[1]))
                ans = input("would you like to add " + str(optionList[2]) + "Y/N: ")
                if ans == "Y":
                    options.append(str(optionList[2]))
                pickup_list[c_count].setOptionList(options)
            # if not options wanted make the options list empty
            else:
                options = []
                pickup_list[c_count].setOptionList(options)
            cabStyle = input("input the cab style: ")
            pickup_list[p_count].setCabStyle(cabStyle)
            bedLength = input("input the bed length: ")
            pickup_list[p_count].setBedLength(bedLength)
        # if the user inputs an invalid option as to whether they want to add a Car or Pickup
        else:
            print("Error")
        more = input("Would you like to add another Vehicle? Y for Yes/N for No: ")
        if more == "Y":
            print("Get ready to add another Vehicle...")
        # when the user is done entering Vehicles
        else:
            menu = False
            # if there was a Car added to the car list
            if c_count > -1:
                car_number = c_count + 1
                # loop is used to loop through every Car object in the list
                loop = 0
                # loop_count is used to identify current Car object in the list
                loop_count = 1
                # collect and print out Car specifications
                while loop < car_number:
                    make = car_list[loop].getMake()
                    model = car_list[loop].getModel()
                    color = car_list[loop].getColor()
                    fuelType = car_list[loop].getFuelType()
                    options = car_list[loop].getOptions()
                    engineSize = car_list[loop].getEngineSize()
                    numDoors = car_list[loop].getNumDoors()
                    print("The specifications on car number " + str(loop_count) + " are " + str(make) + " "
                    + str(model) + " " + str(color) + " " + str(fuelType) + " " + str(options) + " " + str(engineSize) + " " + str(numDoors))
                    print("The options are...")
                    optionList = car_list[loop].getOptionList()
                    for x in range(len(optionList)):
                        print(optionList[x])
                    loop += 1
                    loop_count += 1
            # if there was a Pickup added to the list
            if p_count > -1:
                pickup_number = p_count + 1
                # loop is used to loop through every Pickup object in the list
                loop = 0
                # loop count is used to identify every Pickup in the list
                loop_count = 1
                # collect and print out Pickup specifications
                while loop < pickup_number:
                    make = pickup_list[loop].getMake()
                    model = pickup_list[loop].getModel()
                    color = pickup_list[loop].getColor()
                    fuelType = pickup_list[loop].getFuelType()
                    options = pickup_list[loop].getOptions()
                    cabStyle = pickup_list[loop].getCabStyle()
                    bedLength = pickup_list[loop].getBedLength()
                    print("The specifications on pickup number " + str(loop_count) + " are " + str(make) + " " 
                    + str(model) + " " + str(color) + " " + str(fuelType) + " " + str(options) + " " + str(cabStyle) + " " + str(bedLength))
                    print("The options are...")
                    for x in range(len(optionList)):
                        print(optionList[x])
                    loop += 1
                    loop_count += 1

# run the menu function
menu()


