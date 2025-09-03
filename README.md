# Smart Inventory Management System (Starter)

A simple, portfolio-ready starter using **FastAPI** + **PostgreSQL** + **Docker**.  
No coding required to run the demo.

## Quick Start

1) Install **Docker Desktop** and make sure it is running.
2) Open a terminal in this folder and run:
```bash
docker compose -f docker/docker-compose.yml up --build
```
3) In another terminal, seed some fake data:
```bash
docker compose -f docker/docker-compose.yml exec api python scripts/seed_data.py
```
4) Open your browser:
- Health check: http://localhost:8000/health
- API docs (Swagger): http://localhost:8000/docs

## Publish to GitHub
- Open **GitHub Desktop** → Add existing repository → Choose this folder → Publish.

## Project Layout
```
smart-inventory-management/
├── api/                 # FastAPI app
├── db/                  # SQLAlchemy models and DB session
├── scripts/             # seed_data.py to create demo products/inventory
├── tests/               # basic tests
├── docker/              # Dockerfile and docker-compose
└── .github/workflows    # CI (pytest)
```
