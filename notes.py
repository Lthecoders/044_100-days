# listOfShame = []
# # Creates an empty list.

# while True:
#   # Starts a never ending loop (until we end it)
#   name = input("What is your name? ")
#   age = input("What is your age? ")
#   pref = input("What is your computer platform? ")
#   # Get the user input.

#   row = [name, age, pref]
#   # Assigns the 3 variables into a single row.

#   listOfShame.append(row)
#   # Adds the contents of the row variable at the end of the list

#   exit = input("Exit? y/n ")
#   # Get user choice to quit, yes or no?

#   if (exit.strip().lower()[0] == "y"):
#     # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
#     break  # break ends a loop and jumps to the next line of code that is not part of the loop.

# print()
# print(
#     listOfShame
# )  # Outputs the list. Note this is NOT part of the loop (not indented), it only runs once the loop ends.


# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       # item refers to each item in the column for that row
#       print(f"{item:^10}", end=" | ")
#       # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.

  #   print()

  # print()


"""if we want to delet an element from a 2D list we have to delet the hole row 
with respect to that element in the row.
"""

# listOfShame = []

# while True:
#   menu = input("Add or Remove?"
#                )  # Gives the user a choice prompt and stores their input.

#   if (
#       menu.strip().lower()[0] == "a"
#   ):  # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.

#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")

#     row = [name, age, pref]

#     listOfShame.append(row)
#     # All the 'add' code is now indented, so it's part of the 'add' branch and will only run if the user enters 'a'.

#   else:  # If the user doesn't choose 'a', run this new remove code instead.
#     name = input(
#         "What is the name of the record to delete?")  # Get the input of a name
#     for row in listOfShame:  # Use a loop to extract one row at a time

#       if name in row:  # Check if the name is in the extracted row.
#         listOfShame.remove(row)  # remove the whole row if name is in it

#   prettyPrint()






listOfShame = [] 

def pretyprint():
  print()
  for row in listOfShame:
    for items in row:
      print(f"{items:^10}",end="|") 
      # print() and if we put print() inside the for loop the output will be stright 

    print() # in order to create a verticale colum use print fuction output of the for loop this will ouput sleeping 


# def prettyPrint():
#   print() 
#   for row in listOfShame: 
#     for item in row: 
#       # item refers to each item in the column for that row
#      print(f"{item:^10}", end=" | ") 
#       # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.

#     print() 

  # print()
while True: 
  menu = input("Add or Remove?") 

  if(menu.strip().lower()[0]=="a"): 

    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")

    row = [name, age, pref] 

    listOfShame.append(row) 
    # pretyprint(listOfShame)
    # prettyPrint()
    # pretyprint()

  else: 
    remove_item = input("What is the name of the record to delete?") 

    for rows in listOfShame:
      if remove_item in rows: 
        listOfShame.remove(rows) # remove the whole row if name is in it
  pretyprint()
  # prettyPrint()


