Le Cafe Billing System
Welcome to the Le Cafe Billing System, a simple and user-friendly application to manage customer bills for a cafe. This system is built using Python's Tkinter for the GUI and CSV for data storage.

Features
Customer details entry (name, phone number, bill number)
Menu items categorized into Mains, Drinks, and Sides
Calculation of total amounts and taxes
Bill generation and display
Save bill data to a CSV file
Clear bill area and reset form
Exit the application

Customer Details Section: Enter the customer's name, phone number, and bill number (auto-generated).
Menu Sections:
Mains: Enter quantities for items like Burger, Tacos, Pizza, Hotdog, Sandwich.
Drinks: Enter quantities for items like Shakes, Beverages, Juice, Mojito, Coffee.
Sides: Enter quantities for items like Nachos, Fries, Nuggets, Pasta, Biscuits.
Bill Area: Displays the generated bill with item details, quantities, and prices.
Buttons:
Total: Calculates the total amounts and taxes.
Generate Bill: Displays the bill in the Bill Area.
Clear: Clears the Bill Area and resets the form.
Exit: Closes the application.
Save Data: Saves the bill details to a CSV file.

Code Overview
Importing Required Modules
python
Copy code
from tkinter import *
from tkinter import messagebox
from csv import *
import random
Bill_App Class
The main class Bill_App contains the initialization of the GUI components and the methods to handle various functionalities.

The saved CSV file will have the following columns:
Customer name
Customer Phone number
Bill number
Mains amount
Drinks amount
Sides amount
Total amount
