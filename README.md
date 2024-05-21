# Le Cafe Billing System

Welcome to the **Le Cafe Billing System**, a simple and user-friendly application to manage customer bills for a cafe. This system is built using Python's Tkinter for the GUI and CSV for data storage.

## Features

- **Customer Details Entry**: Enter the customer's name, phone number, and bill number (auto-generated).
- **Menu Items Categorized**:
  - **Mains**: Enter quantities for items like Burger, Tacos, Pizza, Hotdog, Sandwich.
  - **Drinks**: Enter quantities for items like Shakes, Beverages, Juice, Mojito, Coffee.
  - **Sides**: Enter quantities for items like Nachos, Fries, Nuggets, Pasta, Biscuits.
- **Bill Calculation**: Calculate total amounts and taxes.
- **Bill Generation and Display**: Generate and display the bill in the Bill Area.
- **Save Bill Data**: Save bill data to a CSV file.
- **Clear and Reset**: Clear the Bill Area and reset the form.
- **Exit**: Close the application.

## Customer Details Section

- Enter the customer's name, phone number, and bill number (auto-generated).

## Menu Sections

- **Mains**: Enter quantities for items like Burger, Tacos, Pizza, Hotdog, Sandwich.
- **Drinks**: Enter quantities for items like Shakes, Beverages, Juice, Mojito, Coffee.
- **Sides**: Enter quantities for items like Nachos, Fries, Nuggets, Pasta, Biscuits.

## Bill Area

- Displays the generated bill with item details, quantities, and prices.

## Buttons

- **Total**: Calculates the total amounts and taxes.
- **Generate Bill**: Displays the bill in the Bill Area.
- **Clear**: Clears the Bill Area and resets the form.
- **Exit**: Closes the application.
- **Save Data**: Saves the bill details to a CSV file.

## Code Overview

### Importing Required Modules

```python
from tkinter import *
from tkinter import messagebox
from csv import *
import random
