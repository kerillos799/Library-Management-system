-- Insert sample data into the authors table
INSERT INTO authors (fname, lname, date_of_birth) VALUES 
('J.K.', 'Rowling', '1965-07-31'),
('George', 'Orwell', '1903-06-25'),
('J.R.R.', 'Tolkien', '1892-01-03'),
('Agatha', 'Christie', '1890-09-15'),
('Isaac', 'Asimov', '1920-01-02');

-- Insert sample data into the book table
INSERT INTO book (name, isbn, published_year, author_id) VALUES
('Harry Potter and the Philosophers Stone', '9780747532699', 1997, 1),
('1984', '9780451524935', 1949, 2),
('The Hobbit', '9780547928227', 1937, 3),
('Murder on the Orient Express', '9780007119318', 1934, 4),
('Foundation', '9780553293357', 1951, 5);

-- Insert sample data into the members table
INSERT INTO members (fname, lname, tele_num, membership_date) VALUES
('Alice', 'Johnson', '1234567890', '2020-05-10'),
('Bob', 'Smith', '9876543210', '2021-03-15'),
('Cathy', 'Brown', '5555555555', '2022-01-20'),
('David', 'Wilson', '4444444444', '2023-06-10'),
('Eve', 'Taylor', '3333333333', '2021-09-01');

-- Insert sample data into the borrow table
INSERT INTO borrow (loan_date, return_date, member_id, book_id) VALUES
('2024-01-01', '2024-01-15', 1, 1),
('2024-02-10', '2024-02-25', 2, 2),
('2024-03-05', NULL, 3, 3),
('2024-04-12', '2024-04-25', 4, 4),
('2024-05-20', NULL, 5, 5);
