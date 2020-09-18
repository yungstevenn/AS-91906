from tkinter import *
from tkinter import ttk
import random

# Create the book class
class book:
  """The book class stores the details of each book and has methods to restock, sell and calculate progress towards the Super Dude goal"""
  def __init__(self, name, stock, sold):
    self.name = name
    self.stock = stock
    self.sold = sold
    book_list.append(self)
  
  # Restock function adds stock on top of stock
  def restock(self, amount):
    if amount > 0:
      self.stock += amount
      return True
    else:
      return False
  
  # Sell function subtracts stock from stock
  def sell(self, amount):
    if amount > 0 and amount <= self.stock:
      self.stock -= amount
      self.sold += amount
      return True
    else:
      return False

# Create a function for list of books
def create_name_list():
  name_list = []
  for book in book_list:
    name_list.append(book.name)
  return name_list

# Function for updating the stock.
def update_stock():
  total_sold = 0
  stock_string = ""
  
  # Append each books stock to the label
  for book in book_list:
    stock_string += "{}: {}\n".format(book.name, book.stock)
    total_sold += book.sold
  stock_string += "\nTotal Stock Sold: {}".format(total_sold)
  book_details.set(stock_string)

# Create the restock function
def restock_stock(book):
  if book.restock(amount.get()):
    message_text.set(restock_message)
    action_feedback.set("Success! Total of {} restocked into {}".format(amount.get(), book.name))
    
  else:
    action_feedback.set("Please enter a positive number")

# Create the sell function
def sell_stock(book):
  if book.sell(amount.get()):
    message_text.set(sell_message)
    action_feedback.set("Success! Total of {} sold from {}".format(amount.get(), book.name))
    
  else:
    action_feedback.set("Not enough stock in {} or not a valid amount".format(book.name))

# Create the manage action function
def manage_action():
  try:
    for book in book_list:
      if chosen_book.get() == book.name:
        if chosen_action.get() == "Restock":
            restock_stock(book)
        else:
            sell_stock(book)
            
    # Update the GUI
    update_stock()
    amount.set("")
  
  # Add an exception for text input
  except ValueError:
    action_feedback.set("Please enter a valid number")
    
# Set up Lists
book_list = []
restock_message = ("Restock complete")
sell_message = ("Sale made")


# Create instances of the class
Comic1 = book("Super Dude", 8, 0)
Comic2 = book("Lizard Man", 12, 0)
Comic3 = book("Water Woman", 3, 0)
book_names = create_name_list()

#GUI code
root = Tk()
root.title("Comic book store")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Book Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can restock, sell stock, and view the total stock here:")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and set the book details variable
book_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=book_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the book combobox
book_label = ttk.Label(bottom_frame, text="Comic Book: ")
book_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the book Combobox
chosen_book = StringVar()
chosen_book.set(book_names[0])

# Create a Combobox to select the book
book_box = ttk.Combobox(bottom_frame, textvariable=chosen_book, state="readonly")
book_box['values'] = book_names
book_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Restock", "Sell"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=15, pady=8, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback.set("")
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_stock()
root.mainloop()
