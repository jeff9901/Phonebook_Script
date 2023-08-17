from Phonebook import *
import csv
import time

file = "./data.csv"

Manager = ContactManager()
    
inputFile = csv.DictReader(open(file),fieldnames=('fname', 'lname', 'phone') )
for row in inputFile:
    Manager.addContact(row['fname'], row['lname'], row['phone'])

while(True):
    
    choice = int(input("Enter Contact (1) or Search (2): "))
    if choice == 1:
        firstName, lastName, phoneNumber = input("Enter First-Name Last-Name PhoneNumber: ").split()
        Manager.addContact(firstName, lastName, phoneNumber)
        
    elif choice == 2:
        inputString = input("Enter search string: ")
        prefixSearch = int(input("Prefix search or not?: "))
        type = int(input("Search type (First name (1), Last name (2), phone number (3)): "))
        startTime = time.time()
        Manager.searchField(inputString, type, prefixSearch)
        print("%s second" % (time.time() - startTime))
        
    condition = int(input("Continue? Yes(1) No(0): "))
    if condition == 0:
        break