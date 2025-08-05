class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_info(self):
        print(f"Title: {self.title} , Author: {self.author}")
       
class BorrowedBook(Book):
    def __init__(self,title,author,borrower):
        self.borrower=borrower
        super().__init__(title,author)
        # self.borrower=borrower

    def display_info(self):
       super().display_info()
       print(f"Borrowed by:{self.borrower}")
    

book=BorrowedBook("Main calf","Suhail","Rushaid")
book.display_info()