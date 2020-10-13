class Library:
  def __init__(self,list_of_books,library_name,*args,**kwargs):
    self.ls_books = list_of_books
    self.lb_name = library_name
    self.lendDict ={}

  def display_books(self):
    print("Book dekh lo: /n")
    for item in self.ls_books:
      print(item)
  
  def lend_book(self,user,book):
    if  book not in self.lendDict.keys():
      self.lendDict.update({book:user})
      print("Le jao khoob padho")
    else:
      print(f"{self.lendDict[book]} kitab ko padh raha hai")
  def addbook (self,book):
    self.ls_books.append(book)
    print("Thanks bhai book ko lib me dene ke liye")
  def return_book(self,book):
    if book in self.lendDict.keys():
      self.lendDict.pop(book)
    else:
      print("Koi book nahi liya bhai")
  
if __name__ == '__main__':
  lib1 = Library(['x','y','z','a','b','c','d','e'],'test_lib')

while True:
  print('Choose one option :')
  print('1. Display book')
  print('2. Lend book')
  print('3. Add book')
  print('4. Return book')
  c =  int(input())
  if c == 1:
    lib1.display_books()
  elif c ==2:
    book = input('kitab ka name' )
    user = input('apna name ')
    lib1.lend_book(user,book)
  elif c ==3:
    book = input('kitab ka name ')
    lib1.addbook(book)
  elif c == 4:
    book = input('Kitab  ka name ')
    lib1.return_book(book)
  else :
    print('kuch to select karo')
         
      
  print("Band karne ke liye 'q' dabao aur continue karne ke liye 'c'" )
  c2 = input()
  if c2== 'q':
    break
  elif c2 == 'c':
    continue