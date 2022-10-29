from helpers import getTheUsersIntrests

# greetings to the user
# maybe add asking for username
print("Welcome to TrueNews")

# get the users intrests
print("What are you you interested in? (enter q to quit)")
intrestedIn = getTheUsersIntrests()
print(*intrestedIn, sep=",")

# get waht the user would rather not see
print("What would you rather not see?")
ratherNotSee = getTheUsersIntrests()
print(*ratherNotSee, sep=",")



print("----------------------------------END-------------------------------------")