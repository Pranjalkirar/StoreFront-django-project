# StoreFront 🛍️

**StoreFront** is a simple and clean e-commerce web application built using Django. It allows users to register, log in, browse products, add them to a shopping cart, and manage quantities — all within a responsive Bootstrap-powered interface.

---

## 🔧 Features

- ✅ User registration, login, and logout using Django’s authentication system  
- ✅ Product listing with name, price, and image  
- ✅ "Add to Cart" functionality with session-based storage  
- ✅ View cart with product quantity, subtotal, and total amount  
- ✅ Remove items or update quantities in the cart  
- ✅ Responsive UI using Bootstrap 4  

---

## 📁 Project Structure

```

storefront/
├── users/                        # Handles user authentication
│   ├── templates/users/
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── register.html
│
├── products/                     # Core app for products and cart
│   ├── models.py                 # Product model
│   ├── views.py                  # Product display and cart logic
│   ├── urls.py                   # Routes for products app
│   ├── templates/products/
│   │   ├── index.html            # Product listing page
│   │   └── cart.html             # Shopping cart page
│
├── templates/
│   └── base.html                 # Shared base layout
│
└── manage.py

````

---

## 💡 How It Works

1. Users register or log in to access the platform.  
2. Products are displayed using Bootstrap cards.  
3. Clicking “Add to Cart” stores items in session data.  
4. Cart shows all added items with quantity and subtotal.  
5. Users can remove items or change quantity as needed.  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or above  
- pip  

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/storefront.git
   cd storefront
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠️ Tech Stack

* **Backend:** Django 5.2+
* **Frontend:** HTML, CSS, Bootstrap 4
* **Cart Storage:** Django sessions (no database cart)

---

## 👩‍💻 Author

**Pranjal Kirar**
B.Tech, Biosciences and Bioengineering, IIT Guwahati
GitHub: [github.com/Pranjalkirar](https://github.com/Pranjalkirar)

---

## 📌 Notes

* This is a beginner-friendly e-commerce app.
* Does not include checkout or payment integration to keep things simple.
* Can be extended with features like user profiles, order history, or “Buy Now” checkout.

---

## 📜 License

MIT License – free to use, modify, and distribute.
