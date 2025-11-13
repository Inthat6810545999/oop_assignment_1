# Inthat Niramarn 6810545999  
# Library Management System (Object-Oriented Python)

A simple **Library Management System** implemented using **Object-Oriented Programming (OOP)** in Python.  
This project refactors the original procedural version into an OOP design to demonstrate the use of **classes, objects, encapsulation, and modular structure**.

---

##  Overview

This system allows a user to:
- Register new books and library members  
- Borrow and return books  
- View available books  
- View books borrowed by a specific member  

The system is designed using **three main classes**: `Book`, `Member`, and `Library`.

---

##  Features

###  Book Management (`Book` Class)
- Create book objects with unique IDs, titles, authors, and copy counts  
- Track total and available copies  
- Borrow and return books through class methods  

###  Member Management (`Member` Class)
- Create and manage member profiles  
- Track each member’s borrowed books  
- Limit borrowing to **3 books per member**  
- Allow returning of borrowed books  

###  Library Operations (`Library` Class)
- Manage all books and members in collections  
- Add new books and members  
- Handle borrowing and returning transactions  
- Display available books and borrowed books per member  

---

##  Class Design

| Class | Attributes | Key Methods |
|--------|-------------|-------------|
| **Book** | `id`, `title`, `author`, `total_copies`, `available_copies` | `borrow()`, `return_book()`, `is_available()` |
| **Member** | `id`, `name`, `email`, `borrowed_books` | `borrow_book()`, `return_book()`, `can_borrow()` |
| **Library** | `books`, `members` | `add_book()`, `add_member()`, `borrow_book()`, `return_book()`, `display_available_books()`, `display_member_books()` |

---

##  Testing

The `test_oop.py` file provides a comprehensive test of all library functions, covering both **normal operations** and **edge cases**.

###  Basic Tests
- Add books and members  
- Borrow and return books  
- Display available and borrowed books  

###  Edge Case Tests
- Borrowing unavailable books  
- Borrowing more than 3 books  
- Returning books not borrowed  
- Handling non-existent members or books  

