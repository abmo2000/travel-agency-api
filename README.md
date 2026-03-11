# ✈️ Travel Agency — Django REST API

## Project Structure

```
travel_agency_project/
│
├── travel_agency/                  # Django project config
│   ├── settings/
│   │   ├── base.py                 # Shared settings
│   │   ├── development.py          # Dev settings
│   │   └── production.py          # Prod settings (security headers, HTTPS, etc.)
│   └── urls.py                     # Root URL config
│
├── apps/
│   ├── accounts/                   # Custom User + JWT Auth
│   ├── destinations/               # Destinations & gallery
│   ├── packages/                   # Travel packages
│   ├── bookings/                   # User bookings
│   └── testimonials/               # Reviews & ratings
│
├── requirements.txt
├── manage.py
└── .env.example
```

---

## Quick Start

### 1. Clone & create virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment
```bash
cp .env.example .env
# Edit .env with your values
```

### 4. Create MySQL database
```sql
CREATE DATABASE travel_agency_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Run migrations
```bash
python manage.py makemigrations accounts destinations packages bookings testimonials
python manage.py migrate
```

### 6. Create superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run development server
```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint                        | Auth Required | Description              |
|--------|---------------------------------|---------------|--------------------------|
| POST   | `/api/v1/auth/register/`        | ❌            | Register new user        |
| POST   | `/api/v1/auth/login/`           | ❌            | Get JWT tokens           |
| POST   | `/api/v1/auth/token/refresh/`   | ❌            | Refresh access token     |
| POST   | `/api/v1/auth/logout/`          | ✅            | Blacklist refresh token  |
| GET    | `/api/v1/auth/profile/`         | ✅            | Get/Update profile       |
| GET    | `/api/v1/destinations/`         | ❌            | List destinations        |
| GET    | `/api/v1/packages/`             | ❌            | List packages            |
| GET    | `/api/v1/packages/{slug}/`      | ❌            | Package detail           |
| GET    | `/api/v1/bookings/`             | ✅            | My bookings              |
| POST   | `/api/v1/bookings/`             | ✅            | Create booking           |
| GET    | `/api/v1/testimonials/`         | ❌            | Approved testimonials    |
| POST   | `/api/v1/testimonials/`         | ✅            | Submit testimonial       |

### Filtering & Search Examples
```
GET /api/v1/packages/?difficulty=easy
GET /api/v1/packages/?search=paris
GET /api/v1/packages/?ordering=-price
GET /api/v1/packages/?page=2
GET /api/v1/destinations/?is_featured=true&country=France
```

---

## Django Admin
Access at `/admin/` — Features:
- **Users**: Full CRUD, avatar upload
- **Destinations**: with inline gallery images
- **Packages**: with fieldsets, slug auto-generation
- **Bookings**: filter by status, date hierarchy, bulk status update
- **Testimonials**: bulk approve/reject actions

---

## API Documentation
- Swagger UI: `/api/docs/`
- ReDoc:       `/api/redoc/`
- OpenAPI schema: `/api/schema/`

---

## Production Deployment (Gunicorn)

```bash
export DJANGO_SETTINGS_MODULE=travel_agency.settings.production
python manage.py collectstatic --noinput
gunicorn travel_agency.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
