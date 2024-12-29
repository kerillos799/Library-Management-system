import sys
from PyQt5.QtWidgets import *
import pyodbc as odbc 

class LibraryAdminGUI(QWidget):
    def __init__(self):
        super().__init__()
        con = self.create_connection()
        self.curs = con.cursor()
        self.members = []
        self.books = []    
        self.initUI()
        

    def create_connection(self):
        DRIVER_NAME = 'SQL SERVER'
        SERVER_NAME = 'DESKTOP-IVUHOT8'
        DATABASE_NAME = 'Library'
        dn = f""" 
            DRIVER= {{{DRIVER_NAME}}};
            SERVER={SERVER_NAME};
            DATABASE={DATABASE_NAME};
            Trust_Connection = yes;
        """
        con = odbc.connect(dn)
        return con

    def initUI(self):
        self.setWindowTitle('Library Management System')

        # Create tabs
        self.tabs = QTabWidget()

        # Create tab widgets
        self.tab_view_members = QWidget()
        self.tab_add_member= QWidget()
        self.tab_remove_members = QWidget()
        self.tab_view_books = QWidget()
        self.tab_add_books = QWidget()
        self.tab_remove_books = QWidget()
        self.tab_borrow_book = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab_view_members, 'View Members')#tamam
        self.tabs.addTab(self.tab_add_member, 'Add Members')#dn
        self.tabs.addTab(self.tab_remove_members, 'Remove Members')#tamam
        self.tabs.addTab(self.tab_view_books, 'View Books')#dn
        self.tabs.addTab(self.tab_add_books, 'Add Books') #dn
        self.tabs.addTab(self.tab_remove_books, 'Remove Books')
        self.tabs.addTab(self.tab_borrow_book, 'Borrow a Book')

        # Setup each tab
        self.setupTabViewMembers()
        self.setupTabAddMembers()
        self.setupTabRemoveMembers()
        self.setupTabViewBooks()
        self.setupTabAddBooks()
        self.setupTabRemoveBooks()
        self.setupTabBorrowBook()

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tabs)

        self.setLayout(mainLayout)
        self.resize(800, 600)

    # Tab 1: View Members
    def setupTabViewMembers(self):
        layout = QVBoxLayout()
        
        self.memberTableView = QTableWidget()
        self.memberTableView.setColumnCount(5)
        self.memberTableView.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name' , 'Tele-Num', 'Membership date'])
        self.updateMemberTable()
        layout.addWidget(self.memberTableView)
        self.tab_view_members.setLayout(layout)

    def setupTabAddMembers(self):
        layout = QVBoxLayout()

        #input data
        inputLayout = QHBoxLayout()
        self.memberfName = QLineEdit()
        self.memberfName.setPlaceholderText('Member First Name')
        self.memberlName = QLineEdit()
        self.memberlName.setPlaceholderText('Member Last Name')
        self.membertele = QLineEdit()
        self.membertele.setPlaceholderText('Member Telephone number')
        inputLayout.addWidget(self.memberfName)
        inputLayout.addWidget(self.memberlName)
        inputLayout.addWidget(self.membertele)
        layout.addLayout(inputLayout)
        #button
        button = QHBoxLayout()
        addButton = QPushButton('add Member')
        addButton.clicked.connect(self.addMember)
        button.addWidget(addButton)
        layout.addLayout(button)

        self.tab_add_member.setLayout(layout)

    # Tab 3: Remove Members
    def setupTabRemoveMembers(self):
        layout = QVBoxLayout()

        # Input fields
        inputLayout = QHBoxLayout()
        self.memberIdInput = QLineEdit()
        self.memberIdInput.setPlaceholderText('Member ID')
        inputLayout.addWidget(self.memberIdInput)

        # Buttons
        buttonLayout = QHBoxLayout()
        removeButton = QPushButton('Remove Selected Member')
        removeButton.clicked.connect(self.removeMember)
        buttonLayout.addWidget(removeButton)

        layout.addLayout(inputLayout, 0)
        layout.addLayout(buttonLayout, 1)

        self.tab_remove_members.setLayout(layout)

    # Tab 3: View Books
    def setupTabViewBooks(self):
        layout = QVBoxLayout()
        
        self.bookTableView = QTableWidget()
        self.bookTableView.setColumnCount(5)
        self.bookTableView.setHorizontalHeaderLabels(['ID', 'Name', 'isbn' , 'Published year', 'author id'])
        self.updateBookTable()
        layout.addWidget(self.bookTableView)
        self.tab_view_books.setLayout(layout)
    

    # Tab 4: Add Books
    def setupTabAddBooks(self):
        layout = QVBoxLayout()

        # Input fields
        inputLayout = QHBoxLayout()
        self.bookName = QLineEdit()
        self.bookName.setPlaceholderText('Book Name')
        self.bookIsbn = QLineEdit()
        self.bookIsbn.setPlaceholderText('ISBN')
        self.year = QLineEdit()
        self.year.setPlaceholderText('Published year')
        self.author = QLineEdit()
        self.author.setPlaceholderText('Author ID')
        inputLayout.addWidget(self.bookName)
        inputLayout.addWidget(self.bookIsbn)
        inputLayout.addWidget(self.year)
        inputLayout.addWidget(self.author)


        # Buttons
        buttonLayout = QHBoxLayout()
        addButton = QPushButton('Add Book')
        addButton.clicked.connect(self.addBook)
        buttonLayout.addWidget(addButton)

        layout.addLayout(inputLayout)
        layout.addLayout(buttonLayout)
        self.tab_add_books.setLayout(layout)

    def setupTabRemoveBooks(self):
        layout = QVBoxLayout()

        # Input fields
        inputLayout = QHBoxLayout()
        self.bookID = QLineEdit()
        self.bookID.setPlaceholderText('Book ID')
        inputLayout.addWidget(self.bookID)

        buttonLayout = QHBoxLayout()
        removeButton = QPushButton('Remove Book')
        removeButton.clicked.connect(self.removeBook)
        buttonLayout.addWidget(removeButton)
        layout.addLayout(inputLayout)
        layout.addLayout(buttonLayout)
        self.tab_remove_books.setLayout(layout)

    # Tab 5: Borrow a Book
    def setupTabBorrowBook(self):
        layout = QVBoxLayout()
 
        formLayout = QGridLayout()

        # Member selection
        memberLabel = QLabel('Select Member:')
        self.memberComboBox = QComboBox()
        self.updateMemberComboBox()

        # Book selection
        bookLabel = QLabel('Select Book:')
        self.bookComboBox = QComboBox()
        self.updateBookComboBox()

        # Borrow button
        borrowButton = QPushButton('Borrow Book')
        borrowButton.clicked.connect(self.borrowBook)

        # Layout arrangement
        formLayout.addWidget(memberLabel, 0, 0)
        formLayout.addWidget(self.memberComboBox, 0, 1)
        formLayout.addWidget(bookLabel, 1, 0)
        formLayout.addWidget(self.bookComboBox, 1, 1)
        formLayout.addWidget(borrowButton, 2, 0, 1, 2)

        # Borrowed books display
        self.borrowedBooksList = QTableWidget()
        self.borrowedBooksList.setColumnCount(5)
        self.borrowedBooksList.setHorizontalHeaderLabels(['ID', 'Loan Date', 'Return Date' , 'Member ID', 'Book ID'])
        self.updateBorrowedBooksList()

        layout.addLayout(formLayout)
        layout.addWidget(QLabel('Borrowed Books:'))
        layout.addWidget(self.borrowedBooksList)

        self.tab_borrow_book.setLayout(layout)

    # Member management methods
    def addMember(self):
        name = self.memberfName.text()
        name2 = self.memberlName.text()
        telen = self.membertele.text()
        if name:
            self.curs.execute(
            "insert into members (fname, lname, tele_num, membership_date) VALUES (?, ?, ?, cast(getdate() as date))",
            (name, name2, telen)
            )
            self.updateMemberTable()
            self.updateMemberComboBox()
            QMessageBox.information(self, "Done", "Succesfully added the user")
        else:
            QMessageBox.warning(self, 'Input Error', 'Please enter a member first name.')

    def removeMember(self):
        id = self.memberIdInput.text()
        if self.memberIdInput:
            self.curs.execute(f"select * from members where id = {str(id)}")
            out = self.curs.fetchall()
            if(len(out) == 0):
                QMessageBox.warning(self, 'Selection Error', 'No member with such ID.')
            else:
                self.curs.execute(f"delete from borrow where member_id = {str(id)}")
                self.curs.execute(f"delete from members where id = {str(id)}")
                self.updateMemberTable()
                self.updateMemberComboBox()
                self.updateBorrowedBooksList()
                QMessageBox.information(self, "Done", f"Succesfully deleted user with the id = {str(id)}")
        else:
            QMessageBox.warning(self, 'Selection Error', 'Please select a member to remove.')

    def updateMemberTable(self):
        command = """
            select * from members
        """
        self.curs.execute(command)
        con = self.curs.fetchall()

        self.memberTableView.setRowCount(len(con))

        for row_num, member in enumerate(con):
            self.memberTableView.setItem(row_num, 0, QTableWidgetItem(str(member[0])))
            self.memberTableView.setItem(row_num, 1, QTableWidgetItem(member[1] or ''))
            self.memberTableView.setItem(row_num, 2, QTableWidgetItem(member[2] or ''))
            self.memberTableView.setItem(row_num, 3, QTableWidgetItem(member[3] or ''))
            self.memberTableView.setItem(row_num, 4, QTableWidgetItem(member[4] or ''))

    def updateMemberComboBox(self):
        self.memberComboBox.clear()
        self.members.clear()
        self.curs.execute("select id from members")
        x = self.curs.fetchall()
        for member in x:
            self.members.append(str(member[0]))
        self.memberComboBox.addItems(self.members)

    # Book management methods
    def addBook(self):
        title = self.bookName.text()
        isbn = self.bookIsbn.text()
        y = self.year.text()
        auth = self.author.text()
        if title:
            if isbn:
                if auth:
                    self.curs.execute(
                        "insert into book (name, isbn, published_year, author_id) values (? , ?, ?, ?)" , 
                        (title, isbn, y, auth)
                    )
                    self.updateBookTable()
                    self.updateBookComboBox()
                    QMessageBox.information(self, "Done", "Successfully added a book")
                else:
                    QMessageBox.warning(self, 'Input Error', 'Please enter Author ID.')
            else:
                QMessageBox.warning(self, 'Input Error', 'Please enter ISBN.')
        else:
            QMessageBox.warning(self, 'Input Error', 'Please enter a book title.')

    def removeBook(self):
        book = self.bookID.text()
        if book:
            self.curs.execute(f"delete from borrow where book_id = {book}")
            self.curs.execute(f"delete from book where id = {book}")
            self.updateBookTable()
            self.updateBookComboBox()
            self.updateBorrowedBooksList()
            QMessageBox.information(self, "Done", f"Successfully removed the book with id = {book}")
        else:
            QMessageBox.warning(self, 'Selection Error', 'Please select a book to remove.')

    def updateBookTable(self):
        self.curs.execute("select * from book")
        con = self.curs.fetchall()

        self.bookTableView.setRowCount(len(con))

        for row_num, book in enumerate(con):
            self.bookTableView.setItem(row_num, 0, QTableWidgetItem(str(book[0])))
            self.bookTableView.setItem(row_num, 1, QTableWidgetItem(book[1] or ''))
            self.bookTableView.setItem(row_num, 2, QTableWidgetItem(book[2] or ''))
            self.bookTableView.setItem(row_num, 3, QTableWidgetItem(str(book[3]) or ''))
            self.bookTableView.setItem(row_num, 4, QTableWidgetItem(str(book[4])))

    def updateBookComboBox(self):
        self.bookComboBox.clear()
        self.books.clear()
        self.curs.execute("select id from book")
        x = self.curs.fetchall()
        for book in x:
            self.books.append(str(book[0]))
        self.bookComboBox.addItems(self.books)

    # Borrow book methods
    def borrowBook(self):
        member = self.memberComboBox.currentText()
        book = self.bookComboBox.currentText()

        if member and book:
            self.curs.execute("insert into borrow (loan_date , member_id, book_id) values (cast(getdate() as date) , ?, ?)" , (member, book))
            self.updateBorrowedBooksList()
            QMessageBox.information(self, 'Success', f'book with id = {book} has been borrowed by member:{member}.')
        else:
            QMessageBox.warning(self, 'Selection Error', 'Please select both a member and a book.')

    def updateBorrowedBooksList(self):
        self.curs.execute("select * from borrow")
        books = self.curs.fetchall()
        self.borrowedBooksList.setRowCount(len(books))

        for row_num, book in enumerate(books):
            self.borrowedBooksList.setItem(row_num, 0, QTableWidgetItem(str(book[0])))
            self.borrowedBooksList.setItem(row_num, 1, QTableWidgetItem(book[1] or ''))
            self.borrowedBooksList.setItem(row_num, 2, QTableWidgetItem(book[2] or ''))
            self.borrowedBooksList.setItem(row_num, 3, QTableWidgetItem(str(book[3]) or ''))
            self.borrowedBooksList.setItem(row_num, 4, QTableWidgetItem(str(book[4])))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = LibraryAdminGUI()
    gui.show()
    sys.exit(app.exec_())