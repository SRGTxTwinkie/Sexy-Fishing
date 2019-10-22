import random as r
import time

def Init():
    print('This is the most intense fishing sim of 2019, be prepared!')
    print("Welcome to the fishing game, press any key to continue ")
    input("Any Key: ")
    Gameplay()

def Gameplay():
    wind = ["Not windy", "Slightly windy", "Very windy"]
    weather = ["Sunny", "Cloudy", "Raining", "Snowing"]
    enviroment = ["Logs", "Rocks", "Lilypads", "Gravely Bottoms", "Muddy Bottoms"]

    windpicker = wind[r.randrange(0,2)]
    weatherpicker = weather[r.randrange(0,3)]
    enviromentpicker = enviroment[r.randrange(0,4)]

    print("The conditions are: \n")
    print("Wind conditions " + windpicker)
    print("It is " + weatherpicker + " out right now")
    print("You are fishing in " + enviromentpicker)
    print()

    bait = BaitPicker()

    print("You cast your line towards the " + enviromentpicker.lower() + " with " + bait.lower())

    time.sleep(r.randrange(1,10))

    print("You feel tension on the line")

    time.sleep(r.randrange(2,4))

    print("Fish on the line!")

    time.sleep(r.randrange(2,4))

    FishGet()

    Ending()

def FishGet():
    x = r.randrange(1,2)
    if x == 1:
        print ("You got the fish!")
        FishLengthSpec()
        return
    else:
        print ("That bitch gone!")
        return

def FishLengthSpec():
    spec = ["Bass", "Bluegill", "Carp", "Dogfish", "Sunfish", "Perch"]
    specpicker = spec[r.randrange(0,5)]
    x = r.randrange(2, 30)
    if x < 10:
        y = r.randrange(1, 3)
    else:
        y = r.randrange(5, 15)
    print("your " + specpicker + " weighed " + str(y) + " pounds  and it was " + str(x) + " inches long")

def Ending():
    answer = input("Would you like to cast again Y/N? ")
    if answer.lower() == 'y':
        Gameplay()

    elif answer.lower() == 'n':
        print("Thank you for playing!")
        abort()

    else:
        print("Invalid entry ")
        Ending()


def BaitPicker():
    print("What Bait would you like?")
    bait = ["Worms","Live Fish","Lure","Bread","Cheese","Hotdog"]
    x = 1
    for i in bait:
        print(x , ":) " + i)
        x += 1
    userBait = input("What bait do you want?: ")
    userBait = bait[int(userBait) - 1]

    return userBait



Init()
