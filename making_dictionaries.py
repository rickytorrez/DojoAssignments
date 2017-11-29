## Making Dictionaries ##
# Create a function that takes in two lists and creates a single dictionary. #

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict(name,favorite_animal):                 

    new_dict = {}                                   ## create a new string

    new_dict = zip(name,favorite_animal)            ## zip combines two lists into one dictionary ##

    print new_dict

makeDict(name, favorite_animal)

print makeDict

# def making_dictionaires(name, favorite_animal):
#     the_dict = {}
#     for i in range(0, len(name)):
#         the_dict[name[i]] = favorite_animal[i]
#     return the_dict

# print making_dictionaires