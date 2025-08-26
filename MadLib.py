#MadLib.py
#Name:Kaitlyn Oswald
#Date:8/26/25
#Assignment:Lab 1

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
verb2 = input("Enter a verb: ")
noun2 = input("Enter a noun: ")
verb3 = input("Enter a verb: ")
  #Print the story with the user supplied words.
print("I like to ride a " + noun1 + ".")
print("Yesterday I was " + verb1 + ".")
print("The flowers are " + adjective1 + ".") 
print("The flowers " + verb2 + " in the wind .")
print("The " + noun2 + " is " + verb3 + " with their blocks .")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()