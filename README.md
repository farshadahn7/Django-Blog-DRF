# Django Blog API (DRF)


## 🚀 Features

- User registration & authentication (simple-JWT)
- CRUD for blog posts
- Categories for posts
- Asynchronous email sending with Celery & Redis
- Containerized development environment with Docker
- Local email capture with smtp4dev
- Interactive API documentation with Swagger

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Task Queue:** Celery + Redis  
- **Email Testing:** smtp4dev  
- **Containerization:** Docker & docker-compose
- **API Docs:** Swagger (drf-yasg)  

---


---

## ⚙️ Quick Start (Docker)

1. Clone and checkout dev:
```bash
git clone https://github.com/farshadahn7/Django-Blog-DRF.git
cd Django-Blog-DRF
git switch dev
```

2. Create environment variables
```bash
cp .env.example .env
# edit .env as needed
```
3. Start the services with Docker
```bash
docker-compose up --build -d
```

