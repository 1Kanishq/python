# library Class student_info Method , get_books (), return_books()
class Library :
    Lname = 'KEC Library'
    Lloc = 'Ghaziabad'
    book_dict ={'python':20,'sql':5,'java':2,'Js':4,'c++':8}
    def __init__(self,name,phno,sid,book=[]):
        self.name = name
        self.phno = phno
        self.sid = sid
        self.book =book

    def student_info(self,sname,srollno,scourse):
        print(f'student name is : {self.sname},student rollno {self.srollno} and the course is {self.scourse}')
    
    def get_books(self):
        wb = int(input("Enter the nuber books to withdraw"))
        self.book.remove(wb)
        self.book

