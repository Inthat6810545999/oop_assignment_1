from library_procedural import (
    add_book,
    add_member,
    find_book,
    find_member,
    borrow_book,
    return_book,
    display_available_books,
    display_member_books,
    members,
    borrowed_books,
)

# Demo script to verify the full functionality of the procedural library system
def run_library_demo():
    """Run a detailed demonstration of all library management features"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - FUNCTIONAL DEMO")
    print("=" * 60)
    
    # Step 1: Add initial book collection
    print("\n--- STEP 1: Adding Books to Inventory ---")
    add_book(1, "Python Crash Course", "Eric Matthes", 3)
    add_book(2, "Clean Code", "Robert Martin", 2)
    add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    add_book(4, "Design Patterns", "Gang of Four", 2)
    
    # Step 2: Register library users
    print("\n--- STEP 2: Registering Members ---")
    add_member(101, "Alice Smith", "alice@email.com")
    add_member(102, "Bob Jones", "bob@email.com")
    add_member(103, "Carol White", "carol@email.com")
    
    # Step 3: Display all available books
    print("\n--- STEP 3: Current Available Books ---")
    display_available_books()
    
    # Step 4: Successful borrowing actions
    print("\n--- STEP 4: Borrowing Books (Successful Cases) ---")
    borrow_book(101, 1)  # Alice borrows Python Crash Course
    borrow_book(101, 2)  # Alice borrows Clean Code
    borrow_book(102, 1)  # Bob borrows Python Crash Course
    
    # Step 5: Check each member’s borrowed books
    print("\n--- STEP 5: Checking Borrowed Books per Member ---")
    display_member_books(101)  # Alice's borrowed list
    display_member_books(102)  # Bob's borrowed list
    display_member_books(103)  # Carol's borrowed list (none yet)
    
    # Step 6: Show remaining available copies
    print("\n--- STEP 6: Books Available After Borrowing ---")
    display_available_books()
    
    # Step 7: Borrowing the last remaining copy of a title
    print("\n--- STEP 7: Borrowing the Last Copy of a Book ---")
    borrow_book(103, 3)  # Carol borrows Pragmatic Programmer
    display_available_books()
    
    # Step 8: Attempt to borrow a book that’s unavailable
    print("\n--- STEP 8: Trying to Borrow Unavailable Book ---")
    borrow_book(102, 3)  # Bob tries to borrow unavailable title
    
    # Step 9: Test borrowing limit (max 3 books per user)
    print("\n--- STEP 9: Testing Borrowing Limit (3 Max) ---")
    borrow_book(101, 4)  # Alice borrows her 3rd book
    display_member_books(101)
    borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    
    # Step 10: Returning borrowed books
    print("\n--- STEP 10: Returning Borrowed Books ---")
    return_book(101, 1)  # Alice returns Python Crash Course
    return_book(102, 1)  # Bob returns Python Crash Course
    display_member_books(101)
    display_available_books()
    
    # Step 11: Invalid return attempt
    print("\n--- STEP 11: Invalid Return Attempt ---")
    return_book(102, 2)  # Bob tries to return a book he never borrowed
    
    # Step 12: Returning and re-borrowing sequence
    print("\n--- STEP 12: Returning Then Borrowing Again ---")
    return_book(103, 3)  # Carol returns Pragmatic Programmer
    borrow_book(102, 3)  # Bob borrows it
    display_member_books(102)
    
    # Step 13: Handling invalid member/book IDs
    print("\n--- STEP 13: Testing Error Handling (Invalid IDs) ---")
    borrow_book(999, 1)  # Non-existent member
    borrow_book(101, 999)  # Non-existent book
    return_book(999, 1)  # Invalid member return
    display_member_books(999)  # Invalid member view
    
    # Step 14: Display final library snapshot
    print("\n--- STEP 14: Final Library Summary ---")
    print("\nBorrowed Books Summary:")
    for record in borrowed_books:
        print(f"  {record['member_name']} has '{record['book_title']}'")
    
    print("\nMembers and Their Borrowed Titles:")
    for member in members:
        print(f"\n{member['name']} (ID: {member['id']}):")
        if member['borrowed_books']:
            for book_id in member['borrowed_books']:
                book = find_book(book_id)
                print(f"  - {book['title']}")
        else:
            print("  (No books borrowed)")
    
    display_available_books()
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)


# Execute demo when run directly
if __name__ == "__main__":
    run_library_demo()
