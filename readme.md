#Inthat Niramarn 6810545999
# 📚 Library Management System (Procedural Python)

A simple **Library Management System** implemented using **procedural programming** in Python.  
This project demonstrates how a library can manage books, members, and borrowing/returning transactions using functions and in-memory data structures.

---

## 🧠 Overview

This system allows a user to:
- Register new books and library members  
- Borrow and return books  
- View available books  
- View books borrowed by a specific member  

It uses **lists** and **dictionaries** to manage data instead of classes or databases.

---

## ⚙️ Features

### 📘 Book Management
- Add new books to the library  
- Track total and available copies  
- Display currently available books  

### 👤 Member Management
- Register new members  
- Track each member’s borrowed books  
- Enforce a borrowing limit (max 3 books per member)  

### 🔁 Borrowing & Returning
- Borrow books if available  
- Return books and update stock  
- Prevent invalid operations (e.g., returning a book not borrowed)

---

## 🧩 Data Structures

| Variable | Type | Purpose |
|-----------|------|----------|
| `library_books` | `list` of `dict` | Stores all book details |
| `registered_members` | `list` of `dict` | Stores member profiles |
| `loan_records` | `list` of `dict` | Tracks borrowing transactions |

Each **book** and **member** is stored as a dictionary for easy access and update.

Example:
```python
book = {
    'id': 1,
    'title': 'Clean Code',
    'author': 'Robert C. Martin',
    'available_copies': 2,
    'total_copies': 2
}
