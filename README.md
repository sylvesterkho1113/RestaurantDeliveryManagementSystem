# 🍽️ Restaurant Delivery Management System

## 📖 Project Description
The Restaurant Delivery Management System is a Python-based console application designed to manage restaurant operations including customer registration, login, ordering system, menu management, order tracking, and administrative control.

The system uses simple text files for data storage, making it lightweight and easy to run without any database setup.

---

## 👨‍💻 Group Members
- 1211207735 - See Chwan Kai  
- 1211211485 - Kho Wei Cong  
- 1211211733 - Kerk Ming Da  
- 1211110456 - Yap Meng Yoon  

---

## 🗂️ Data Files Used
The system stores all data in plain text files:
- `login.txt` → Stores user registration and login information  
- `order.txt` → Stores all customer orders  
- `menu.txt` → Stores menu items (food name, price, description)  
- `hour.txt` → Stores branch information and operating hours  

---

## 🔐 Admin Credentials
```bash
Username: admin
Password: admin123
```

---

## 🚀 Features

### 👤 User Features
- Register and login system
- Place new food orders
- View order history
- Search orders by status
- Cancel pending orders
- Update delivery address
- View personal profile
- View restaurant branch information and operating hours
- Contact support section
- Logout system

---

### 🛠️ Admin Features
- View all customer orders
- Edit order status (Order Placed, Preparing, Delivered, etc.)
- Delete orders
- Search customer information
- Add new menu items
- Display menu items
- Edit menu item price
- Delete menu items
- Add new restaurant branches
- View and manage branch information
- Update operating hours

---

## ⚙️ System Requirements
- Python 3.x
- Works on Windows / Linux / macOS terminal
- No external libraries required

---

## ▶️ How to Run
1.Clone this repository to your local machine.
2. Make sure all `.txt` files are in the same directory as the Python script:
   - `login.txt`
   - `order.txt`
   - `menu.txt`
   - `hour.txt`

3. Run the program:
```bash
python Restaurant_Delivery_Management_System.py
```
