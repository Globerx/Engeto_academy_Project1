# 1. Define basic variables
users = {"bob":"123", "ann":"pass123", "mike":"password123" , "liz":"pas123"}
choice_options = ("1","2","3")
upper = 0
lower = 0
title = 0
numeric = 0
sum_numbers = 0
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
 100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
separator = "=" * 40
# 2. Welcome user and asks for input
print("Welcome to the app. Please log in:")
print(separator)
mod = True

while mod == True:
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    print(separator)

# 3. Check if username and password are correct

    if username in users.keys():
        if password == users[username]:
            print("LOGIN SUCCESS")
            mod = False
        else: print("BAD PASSWORD")
    else:print("User does not exist")
    print(separator)

# 4. Select text to be analyzed

mod = True
while mod == True:
    print("We have 3 texts to be analyzed")
    choice = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)
    if choice in choice_options:
        choice = int(choice)
        mod = False
    else: print("your choice is not available")

if choice == 1:
    text_to_be_used = TEXTS[0]
elif choice == 2:
    text_to_be_used = TEXTS[1]
else: text_to_be_used = TEXTS[2]

# 6. Do operations with text

words_count = len(text_to_be_used.split(" "))
words_list = list(text_to_be_used.split(" "))
frequency_dict = {}

while words_list:
    word = words_list.pop()
    if word.istitle():
        title = title + 1
    elif word.isupper():
        upper = upper + 1
    elif word.islower():
        lower = lower + 1
    elif word.isnumeric():
        numeric = numeric + 1
        sum_numbers = sum_numbers + int(word)

    keys = len(word)
    frequency_dict[keys] = frequency_dict.get(keys,0) + 1

print(f"""
There are {words_count} words in the selected text.
There are {title} titlecase words
There are {upper} uppercase words
There are {lower} lowercase words
There are {numeric} numeric strings
""")
print(separator)

# 7. show counts of each word lenght
# print(cetnost)

while frequency_dict:
    minimum = min(frequency_dict)
    vyskyt = frequency_dict.pop(minimum,"nothing")
    print(minimum, "*" * vyskyt, " ", vyskyt)
print(separator)

# Suma vsech cisel v textu
print("If we summed all the numbers in this text we would get: ", sum_numbers)
print(separator)
