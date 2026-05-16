# 🍽️ Restaurant Delivery Management System

A comprehensive Python-based console application designed to streamline restaurant operations, manage customer orders, and handle administrative tasks. This system is built with a focus on simplicity, using local text files for data persistence, making it lightweight and easy to deploy without complex database setups.

---

## 👥 Group Members (Group 03)
- **1211207735** - See Chwan Kai
- **1211211485** - Kho Wei Cong
- **1211211733** - Kerk Ming Da
- **1211110456** - Yap Meng Yoon

---

## 🚀 Key Features

### 👤 Customer Module
- **Account Management**: Register new accounts and secure login system.
- **Ordering System**: Browse the menu and place orders with real-time total calculation (including delivery fees).
- **Order Tracking**: 
  - View complete order history.
  - Search orders by status (Placed, Preparing, Cancelled, Out for Delivery, Delivered).
  - Cancel pending orders (only available for orders in "Order placed" status).
- **Profile Management**: View personal details and update delivery addresses.
- **Information Hub**: View restaurant branch locations, contact details, and operating hours.
- **Support**: Quick access to customer support contact information.

### 🛠️ Administrative Module
- **Order Management**:
  - Monitor all customer orders in the system.
  - Update order statuses to keep customers informed.
  - Delete obsolete or incorrect orders.
- **Inventory & Menu Control**:
  - Add, edit, or remove food items from the menu.
  - Manage item prices and descriptions.
- **Branch Management**:
  - Add and manage multiple restaurant branches.
  - Update operating hours and branch contact information.
- **Customer Insights**: Search and view detailed customer information by contact number.

---

## 🔐 Admin Credentials
Access the administrative dashboard using the following credentials:
- **Username**: `admin`
- **Password**: `admin123`

---

## 📂 Data Architecture
The system utilizes a flat-file database approach for simplicity and portability:
- `login.txt`: Stores user credentials and profile information.
- `order.txt`: Tracks all transaction records and order statuses.
- `menu.txt`: Contains the catalog of food items, prices, and descriptions.
- `hour.txt`: Manages branch-specific data and operating hours.

---

## ⚙️ System Requirements
- **Runtime**: Python 3.x
- **Environment**: Windows / Linux / macOS Terminal
- **Dependencies**: None (Uses standard Python libraries only)

---

## ▶️ Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sylvesterkho1113/RestaurantDeliveryManagementSystem.git
   ```

2. **Verify Data Files**:
   Ensure the following `.txt` files are present in the root directory:
   - `login.txt`
   - `order.txt`
   - `menu.txt`
   - `hour.txt`

3. **Run the Application**:
   ```bash
   python "Group03_Restaurant Delivery Management System.py"
   ```

---

## 🎨 Visual Experience
The application utilizes ANSI escape codes to provide a colorful and intuitive terminal interface, enhancing the user experience for both customers and administrators.

---
*Developed as part of the DPL5211 Fundamental of Programming Language project.*
