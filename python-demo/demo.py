import sys
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")
            

class Person:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return")
            self.book=input()
            return self.book

def main():            
      library=Library(['The Last Battle - Veny Buzz - 1989','The Screwtape letters - Jadu Badu - 1995','The Great Divorce - Jhon Bow - 2000','Big Wall - Demy Moor - 2000'])
      person=Person()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books (Press 1)
                  2. Request a book              (Press 2)
                  3. Return a book               (Press 3)
                  4. Exit                        (Press 4)
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(person.requestBook())
            elif choice==3:
                        library.addBook(person.returnBook())
            elif choice==4:
                  sys.exit()
                  
main()

