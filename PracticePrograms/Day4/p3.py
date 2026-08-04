class Library:
    books = []
    borrowed_books = []

    def add_book(self, title: str, author: str, stock: int):
        self.stock = stock
        if self.stock < 0: 
            print(f"No stock for book {title} by {author}.")
            return
        self.title = title
        self.author = author
        Library.books.append([self.title, self.author])
        print(f"Added {self.stock} books of {self.title} by {self.author} to library.")

    def remove_book(self):
        Library.books.remove([self.title, self.author])
        print(f"Removed all {self.stock} book of {self.title} by {self.author} from library.")

    def borrow_book(self):
        if [self.title, self.author] not in Library.books:
            print("Out of stock, sorry.")
        Library.borrowed_books.append([self.title, self.author])
        self.stock -= 1
        if self.stock == 0:
            Library.books.remove([self.title, self.author])
            print(f"{self.title} by {self.author} is now out of stock!")

    def return_book(self):
        if [self.title, self.author] not in Library.borrowed_books:
            print("You can't return a book you never borrowed.")
            return
        Library.borrowed_books.remove([self.title, self.author])

        if [self.title, self.author] not in Library.books:
            Library.books.append([self.title, self.author])
            print(f"{self.title} by {self.author} is now available!")
        self.stock += 1
        print(self.title, self.author, self.stock)

book1 = Library()
book1.add_book('Title1', 'Author1', 40)
book2 = Library()
book2.add_book('Title2', 'Author2', 34)
book3 = Library()
book3.add_book('Title3', 'Author3', 56)
book4 = Library()
book4.add_book('Title4', 'Author4', 10)
book5 = Library()
book5.add_book('Title5', 'Author5', 1)

book5.borrow_book()
book5.return_book()