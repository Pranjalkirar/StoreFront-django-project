# 🛍️ StoreFront

A simple Django-based online storefront that displays products with their image, price, and name, along with an **"Add to Cart"** feature.

---

## 📂 Project Structure

```
StoreFront/
├── products/              # Django app for handling products
├── StoreFront/            # Django project configuration
├── static/                # Static files (CSS, JS)
├── templates/             # HTML templates
├── manage.py              # Django's CLI utility
├── db.sqlite3             # SQLite database (local)
├── requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/PranjalKirar/StoreFront.git
cd StoreFront
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Now, open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Features

- 🖼️ Display of products with image, name, and price
- ➕ "Add to Cart" functionality
- 🎨 Clean frontend using Bootstrap

---

## 🛠 Built With

- Python 3.x
- Django
- Bootstrap 5
- SQLite (default DB)

---

## 🙋‍♀️ Author

**Pranjal Kirar**  
[GitHub Profile](https://github.com/PranjalKirar)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
