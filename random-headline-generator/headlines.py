# importing random module 
import random
# creating subjects 
subjects = [
    "Prabhas",
    "Allu Arjun",
    "Mahesh Babu",
    "Salar 2",
    "Rebel star",
    "New Action hero"   
]


actions = [
    "is going to be",
    "is planning to be",
    "is going to release as",
    "is expected to be a",
    "is set to be"
]


about = [
    "action movie",
    "thriller",
    "comedy",
    "romantic movie",
    "drama",
    "sci-fi movie"
]
# adding while loop
while True:
    random_subject = random.choice(subjects)
    random_action = random.choice(actions)
    random_about = random.choice(about)

    headline = f"BREAKING NEWS: {random_subject} {random_action} {random_about} "
    print("\n" + headline)

# using strip to remove the space in words, and lower to convert the input to lowercase
    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input =="no":
        break

# saying goodbye tyo the user
print ("\n Thanks for coming to the headline generator.")




