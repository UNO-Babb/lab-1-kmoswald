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
print("Yesterday I was " + verb1 + " on a trail .")
print("The flowers were " + adjective1 + ".") 
print("The flowers were " + verb2 + " in the wind .")
print("A " + noun2 + " is " + verb3 + " overhead .")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()