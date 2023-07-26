# Tylor Underwood
# Class Project 
# October 31, 2021
# API key = b8c52ffcc220b011c5cb3b0f9c4fe74d

from pip._vendor import requests # import requests library

api_key = "b8c52ffcc220b011c5cb3b0f9c4fe74d"

def get_forecast_city(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    print("getting city forecast...")
    answer = requests.get(url).json()
    temp = "the temp is: " + str(answer['main']['temp'])
    print(temp)
    temp_max = "the max temp is: " + str(answer['main']['temp_max'])
    print(temp_max)
    temp_min = "the min temp is: " + str(answer['main']['temp_min'])
    print(temp_min)
    pressure = "the pressure is: " + str(answer['main']['pressure'])
    print(pressure)
    humidity = "the humidity is: " + str(answer['main']['humidity'])
    print(humidity)
    wind = "the wind speed is: " + str(answer['wind']['speed'])
    print(wind)
   
def get_forecast_zipcode(api_key, zipcode):
    country_code = "us" # make it so zipcodes only work in the U.S for simplicity
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country_code}&appid={api_key}"
    print("getting zipcode forecast")
    answer = requests.get(url).json()
    print(answer)
    temp = "the temp is: " + str(answer['main']['temp'])
    print(temp)
    temp_max = "the max temp is: " + str(answer['main']['temp_max'])
    print(temp_max)
    temp_min = "the min temp is: " + str(answer['main']['temp_min'])
    print(temp_min)
    pressure = "the pressure is: " + str(answer['main']['pressure'])
    print(pressure)
    humidity = "the humidity is: " + str(answer['main']['humidity'])
    print(humidity)
    wind = "the wind speed is: " + str(answer['wind']['speed'])
    print(wind)

def keep_going(): # used to run program multiple times
    ans = input("Would you like to continue? (Y/N): ")
    if ans == "Y":
        return True
    else:
        return False

def thank_user(): # used to thank user before quitting
    print("Thank you for using the Weather Applicaton")

def main(): # main function
    go = True
    user_choice = "1" 
    while(go == True):
        print("Welcome to the Weather Application")
        user_choice = input("Would you like to use City Information? (Enter 1). Or would you like to use Zipcode Information? (Enter 2): ")
        if user_choice == "1":
            city_name = input("Enter the name of the City: ")
            try:
                get_forecast_city(api_key, city_name) # option 1
                print("connection was successful!")
            except:
                print("error connecting to service...")
        elif user_choice == "2":
            zipcode = input("Enter the Zipcode: ")
            try:
                get_forecast_zipcode(api_key, zipcode) # option 2
                print("connection was successful!")
            except:
                print("error connecting to service...")
        else:
            print("invalid input...") # if invalid input
        go = keep_going()

main()
thank_user()
    
