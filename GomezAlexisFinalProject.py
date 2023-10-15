
# This program allows the user to create orders for a restaurant by collecting customer name, items ordered, and price

import tkinter as tk
from tkinter import PhotoImage, messagebox

# Function to open the order summary window
def openOrderSummary():
    """
    Open a new window displaying the order summary.
    This function retrieves order details, creates a summary, and displays it in a new window.
    """
    summaryWindow = tk.Toplevel(root)
    summaryWindow.title("Order Summary")

    # Retrieve order details from the main window
    customerName = customerNameEntry.get()
    
    # Create a summary of ordered items
    summaryText = f"Customer Name: {customerName}\n\nOrdered Items:\n"
    for item, quantity in orderedItems.items():
        itemPrice = itemPrices[item]
        totalPriceForItem = quantity * itemPrice
        summaryText += f"{item}: {quantity} x ${itemPrice} = ${totalPriceForItem}\n"
    
    totalPrice = sum(quantity * itemPrices[item] for item, quantity in orderedItems.items())

    # Display order summary
    summaryLabel = tk.Label(summaryWindow, text="Order Summary")
    summaryLabel.pack()

    summaryLabel = tk.Label(summaryWindow, text=summaryText)
    summaryLabel.pack()

    totalPriceLabel = tk.Label(summaryWindow, text=f"Total Price: ${totalPrice}")
    totalPriceLabel.pack()

    # Load and display a placeholder image for the summary window
    summaryImage = PhotoImage(file="order.png")  # Path to order.png
    summaryImageLabel = tk.Label(summaryWindow, image=summaryImage)
    summaryImageLabel.image = summaryImage  # Keep a reference to the image to avoid garbage collection
    summaryImageLabel.pack()

# Function to add the selected item to the order
def addToOrder():
    """
    Add the selected item to the order and update the display.
    This function retrieves the selected item and quantity, adds them to the order, and updates the order display.
    """
    selectedItem = itemVar.get()  # Selected item from the dropdown
    quantity = quantityEntry.get()  # Quantity of the selected item
    
    try:
        quantity = int(quantity)
        if selectedItem in orderedItems:
            orderedItems[selectedItem] += quantity
        else:
            orderedItems[selectedItem] = quantity
        messagebox.showinfo("Item Added", f"{quantity} {selectedItem}(s) added to the order.")
        updateOrderDisplay()  # Update the display of ordered items
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")

# Function to update the order display
def updateOrderDisplay():
    """
    Update the order display with the list of ordered items and their prices.
    """
    orderDisplayText.set("Ordered Items:\n")
    for item, quantity in orderedItems.items():
        itemPrice = itemPrices[item]
        totalPriceForItem = quantity * itemPrice
        orderDisplayText.set(orderDisplayText.get() + f"{item}: {quantity} x ${itemPrice} = ${totalPriceForItem}\n")

# Function to update the price label based on the selected item
def updatePriceLabel(*args):
    """
    Update the price label when the selected item changes.
    """
    selectedItem = itemVar.get()  # Selected item from the dropdown
    priceLabel.config(text=f"Price: ${itemPrices[selectedItem]}")  # Update the price label

# Function to reset the order
def resetOrder():
    """
    Reset the order and clear all order-related data.
    """
    customerNameEntry.delete(0, tk.END)  # Clear the customer name entry
    itemVar.set(items[0])  # Reset item selection
    quantityEntry.delete(0, tk.END)  # Clear quantity entry
    orderedItems.clear()  # Clear the ordered items dictionary
    updateOrderDisplay()  # Clear the order display
    messagebox.showinfo("Order Reset", "Order has been reset.")

# Create the main order window
root = tk.Tk()
root.title("Ordering System")
root.geometry("600x600")  # Resize main window

# Load and display an image placeholder for the main window
image = PhotoImage(file="menu.png")  # Path to menu.png
image = image.subsample(2)  # Resize the image by a factor of 2 
imageLabel = tk.Label(root, image=image)  # Label to display the image
imageLabel.pack()

# Customer Name
customerNameLabel = tk.Label(root, text="Customer Name:")  # Label for customer name entry
customerNameLabel.pack()
customerNameEntry = tk.Entry(root)  # Entry for customer name
customerNameEntry.pack()

# Dropdown menu for item selection
items = ["Fries", "Burger", "Soda", "Pizza", "Ice Cream"]  # List of available items
itemVar = tk.StringVar(root)  # Variable to store the selected item
itemVar.set(items[0])  # Default selection
itemVar.trace("w", updatePriceLabel)  # Update price label when the item changes
itemLabel = tk.Label(root, text="Select Item:")  # Label for item selection
itemLabel.pack()
itemDropdown = tk.OptionMenu(root, itemVar, *items)  # Dropdown menu for item selection
itemDropdown.pack()

# Price label to display the selected item's price
itemPrices = {
    "Fries": 5,
    "Burger": 10,
    "Soda": 2,
    "Pizza": 12,
    "Ice Cream": 4
}
priceLabel = tk.Label(root, text=f"Price: ${itemPrices[items[0]]}")  # Label to display the item's price
priceLabel.pack()

# Quantity
quantityLabel = tk.Label(root, text="Quantity:")  # Label for quantity entry
quantityLabel.pack()
quantityEntry = tk.Entry(root)  # Entry for quantity
quantityEntry.pack()

# Add to Order Button
addToOrderButton = tk.Button(root, text="Add to Order", command=addToOrder)  # Button to add an item to the order
addToOrderButton.pack()

# Order display
orderDisplayText = tk.StringVar()  # Variable to store the order display text
orderDisplayLabel = tk.Label(root, textvariable=orderDisplayText)  # Label to display the order
orderDisplayLabel.pack()

# Submit Order Button
submitButton = tk.Button(root, text="Submit Order", command=openOrderSummary)  # Button to submit the order
submitButton.pack()

# Reset Order Button
resetOrderButton = tk.Button(root, text="Reset Order", command=resetOrder)  # Button to reset the order
resetOrderButton.pack()

# Dictionary to store ordered items and quantities
orderedItems = {}

# Start the tkinter main loop
root.mainloop()
