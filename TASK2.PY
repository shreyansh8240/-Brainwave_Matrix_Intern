import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Database Initialization
def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        quantity INTEGER,
                        price REAL)''')
    conn.commit()
    conn.close()

# Authentication Functions
def register_user(username, password):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        messagebox.showinfo("Login Successful", "Welcome!")
        open_inventory_window()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

# Inventory Management Functions
def add_product(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product added successfully!")
    refresh_inventory()

def update_product(product_id, name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?", (name, quantity, price, product_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product updated successfully!")
    refresh_inventory()

def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product deleted successfully!")
    refresh_inventory()

def get_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

# GUI Components
def open_inventory_window():
    inventory_window = tk.Toplevel()
    inventory_window.title("Inventory Management")
    inventory_window.geometry("600x400")
    
    tree = ttk.Treeview(inventory_window, columns=("ID", "Name", "Quantity", "Price"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.pack(fill=tk.BOTH, expand=True)
    
    def refresh_inventory():
        for row in tree.get_children():
            tree.delete(row)
        for product in get_products():
            tree.insert("", tk.END, values=product)
    
    refresh_inventory()

def main():
    init_db()
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")
    
    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    
    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    tk.Button(root, text="Login", command=lambda: login_user(username_entry.get(), password_entry.get())).pack()
    tk.Button(root, text="Register", command=lambda: register_user(username_entry.get(), password_entry.get())).pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()
