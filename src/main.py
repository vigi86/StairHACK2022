
import string

print("Welcome to TrueNews")
print("What are you you interested in? (enter q to quit)")

topic = input("Enter a topic:")
topics_list = []
while topic != "q":
        topics_list.append(topic) if topic.isalpha() else print("Input should be alphabetical!")
        topic = input('Enter a topic:')

print("What would you rather not see?")
print("Finished")