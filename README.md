# 🛒 Smart Inventory Management System

A **portfolio-ready grocery store inventory system** built with **Python, FastAPI, PostgreSQL, Streamlit, and Docker**.  
This project demonstrates skills in **backend development, data modeling, analytics, and DevOps** — all in one.

## 🚀 Features
- 📦 **Inventory Tracking**: View stock levels (`on_hand`, `on_order`, `reserved`) for grocery items.  
- 🖥️ **Web Dashboard (Streamlit)**: Clean UI to explore grocery products.  
- ⚡ **REST API (FastAPI)**: Auto-documented endpoints with OpenAPI/Swagger.  
- 🛠️ **Database (PostgreSQL)**: Structured schema with products, stores, and inventory.  
- 🧪 **Automated Tests**: Basic unit test coverage with `pytest`.  
- 🐳 **Dockerized**: Fully containerized setup with Docker Compose.  
- 🔄 **Seeding Script**: Populates database with grocery items (Bananas, Milk, Bread, etc.).



## 🏗️ Tech Stack
- **Backend**: FastAPI  
- **Frontend/Dashboard**: Streamlit  
- **Database**: PostgreSQL + SQLAlchemy  
- **Data Tools**: pandas  
- **Testing**: pytest  
- **DevOps**: Docker, Docker Compose, GitHub Actions  

## ⚙️ How to Run Locally

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)  
- Install [Python 3.11+](https://www.python.org/downloads/)  

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/smart-inventory-management.git
cd smart-inventory-management
```

### 2. Start backend (FastAPI + Postgres)
```bash
docker compose -f docker/docker-compose.yml up --build
```

Check health at 👉 [http://localhost:8000/health](http://localhost:8000/health)  
API docs at 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Seed grocery data
```bash
docker compose -f docker/docker-compose.yml exec api python -m scripts.seed_data
```

### 4. Run dashboard
```bash
python3 -m streamlit run web/dashboard.py
```

Dashboard available at 👉 [http://localhost:8501](http://localhost:8501)

## 🧑‍💻 Skills Demonstrated
- **Python (FastAPI, Streamlit, pandas)**  
- **REST API development**  
- **SQLAlchemy & PostgreSQL**  
- **Containerization (Docker, Docker Compose)**  
- **Unit Testing (pytest)**  
- **Git & GitHub (repo management, CI/CD)**  
- **Data modeling & analytics for retail**  

## 🎯 Next Steps / Roadmap
- Add **forecasting models** (demand prediction, reorder point).  
- Add **alerts** for low stock.  
- Extend dashboard with **charts and reports**.  
- Implement **GitHub Actions CI/CD** pipeline.  

## 👤 Author
**Mohamed**  
[LinkedIn](https://uk.linkedin.com/in/mohamed-ahmed-issa) | [GitHub](https://github.com/missacodes)
