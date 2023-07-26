# Tylor Underwood
# Introduction to Programming
# Class Project Rough Draft
# October 31, 2021
# This more serves as an Outline than a Rough Draft for now
# API key = b8c52ffcc220b011c5cb3b0f9c4fe74d

from pip._vendor import requests # import requests library
import math

api_key = "b8c52ffcc220b011c5cb3b0f9c4fe74d"

def get_forecast_city(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    print("getting city forecast...")
    answer = requests.get(url).json()
    print(answer)

def get_forecast_zipcode(api_key, zipcode):
    country_code = "us" # make it so zipcodes only work in the U.S for simplicity
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country_code}&appid={api_key}"
    print("getting zipcode forecast")
    answer = requests.get(url).json()
    print(answer)

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
        if user_choice != "2": # defaults to the first option if invalid input
            city_name = input("Enter the name of the City: ")
            get_forecast_city(api_key, city_name) # option 1
        else:
            zipcode = input("Enter the Zipcode: ")
            get_forecast_zipcode(api_key, zipcode) # option 2
        go = keep_going()

main()
thank_user()
    
