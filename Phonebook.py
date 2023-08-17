"""
    TrieNode Data Structure
"""
class TrieNode :
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.contactList = []


class Trie :
    def __init__(self):
        self.phoneBookCrawl = TrieNode()

    def insert(self, inputString, contact):
         
        phoneBookCrawl = self.phoneBookCrawl
        inputString = inputString.lower()
        
        for char in inputString:
            if not phoneBookCrawl.children.get(char):
                phoneBookCrawl.children[char] = TrieNode()
            phoneBookCrawl = phoneBookCrawl.children[char]
 
        phoneBookCrawl.isEndOfWord = True
        phoneBookCrawl.contactList.append(contact)

    def search(self, inputString, isPrefix):
        inputString = inputString.lower()
        phoneBookCrawl = self.phoneBookCrawl
        contactList = []
        for char in inputString:
            if not phoneBookCrawl.children.get(char):
                return []
            phoneBookCrawl = phoneBookCrawl.children[char]
 
        if(phoneBookCrawl.isEndOfWord):
            contactList.extend(phoneBookCrawl.contactList)
        
        if(isPrefix == 0):
            return contactList
        
        self.prefixSearchUtilityFunc(phoneBookCrawl, contactList)

        return contactList


    def prefixSearchUtilityFunc(self, phoneBookCrawl, contactList):   
        if(phoneBookCrawl == None):
            return

        for child in phoneBookCrawl.children:
            self.prefixSearchUtilityFunc(phoneBookCrawl.children[child], contactList)
            if( phoneBookCrawl.children[child] ):
                if( phoneBookCrawl.children[child].isEndOfWord ):
                    contactList.extend(phoneBookCrawl.children[child].contactList)

class ContactManager:
    
    firstNameTree = Trie()
    lastNameTree = Trie()
    phoneNumberTree = Trie()
    
    directory = {}  # key = phoneNumber, value = Object
    
    def __init__(self):
        pass

    def addContact(self, firstName, lastName, phoneNumber):
        
       self.firstNameTree.insert(firstName, phoneNumber)
       self.lastNameTree.insert(lastName, phoneNumber)
       self.phoneNumberTree.insert(phoneNumber, phoneNumber)
       
       nodeObject = ContactNode(firstName, lastName, phoneNumber)
        
       self.directory[phoneNumber] = nodeObject
       

    def printMatchingEntries(self, contacts):
        count = 1
        print('Total Count : ' + str(len(contacts)))
        for number in contacts:
            print(count, end=' ')
            self.directory[number].printNode()
            count += 1
    
    def searchField(self, inputString, type, isPrefix = 0):   
        contacts =[]
        
        if type == 1:
            contacts = self.firstNameTree.search(inputString, isPrefix)
                
        if type == 2:
            contacts = self.lastNameTree.search(inputString, isPrefix)
                
        if type == 3:
            contacts = self.phoneNumberTree.search(inputString, isPrefix)
                
        self.printMatchingEntries(contacts)
        
        

class ContactNode: 
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName   
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        
    def printNode(self):
        print(self.firstName, ' ', self.lastName, ' : ', self.phoneNumber)
        