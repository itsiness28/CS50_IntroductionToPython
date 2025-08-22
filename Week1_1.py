# PYTHON_Exercise 1. This program asks the user for their name and says hello. 
name= input ("What's you name? ").strip().title()
    #this up here is to remove accidental spaces and to capitalize. "name= name.capitalize()" . This works just for the first letter of the sentece. The next line works for the first letter of each word.
    #spliting between last nmame and first name
first, last= name.split(" ")

print ("Hello,", last) #will work with either first and last. 

              