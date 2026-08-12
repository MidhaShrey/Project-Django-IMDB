# WatchMate

A Django REST Framework API for a movie/show watchlist platform. Users can browse streaming platforms, view watchlisted titles, and leave one review per title with a 1–5 star rating. Authentication is handled via DRF Token Authentication.

Built while following a Udemy course on Django REST Framework.

## Tech Stack

- **Python** 3.13
- **Django** 6.0
- **Django REST Framework** 3.17
- **SQLite** (default dev database)
- **Token Authentication** (`rest_framework.authtoken`)
- **python-dotenv** for environment variable management

## Project Structure

```
watchmate_Udemy/
├── manage.py                      # Django management entrypoint
├── requirements.txt               # Python dependencies
├── .env                            # Environment variables (SECRET_KEY, etc.)
├── db.sqlite3                     # SQLite database (dev)
│
├── watchmate/                     # Project configuration
│   ├── __init__.py
│   ├── settings.py                # Installed apps, DRF config, DB config
│   ├── urls.py                    # Root URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── watchlist_app/                 # Core app: platforms, watchlist, reviews
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                  # StreamPlatform, WatchList, Review
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   └── api/
│       ├── serializers.py         # ReviewSerializer, WatchlistSerializer, StreamPlatformSerializer
│       ├── views.py                # StreamPlatformVS, WatchListAV/DetailsAV, ReviewCreate/List/Details
│       ├── permissions.py         # AdminOrReadOnly, ReviewUserOrReadOnly
│       └── urls.py                # /watch/ routes
│
└── user_app/                      # Auth app: login via token
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── tests.py
    ├── migrations/
    └── api/
        ├── serializers.py
        ├── views.py
        └── urls.py                 # /account/ routes
```

## Data Models

**StreamPlatform** (`watchlist_app/models.py`)
- `name`, `about`, `website`
- Has many `WatchList` entries (`related_name='watchlist'`)

**WatchList**
- `title`, `storyline`
- `platform` — FK to `StreamPlatform`
- `avg_rating`, `number_rating` — updated automatically when a review is created
- `created`, `active`

**Review**
- `review_user` — FK to `User`
- `rating` (1–5, validated), `description`
- `watchlist` — FK to `WatchList` (`related_name='reviews'`)
- `active`, `created`, `updated`
- One review per user per watchlist entry is enforced in `ReviewCreate`

## API Endpoints

### Auth — `/account/`

| Method | Endpoint      | Description                        |
|--------|---------------|-------------------------------------|
| POST   | `/account/login/` | Obtain an auth token (username/password) |

### Watchlist — `/watch/`

| Method | Endpoint                              | Description                          |
|--------|----------------------------------------|---------------------------------------|
| GET    | `/watch/list/`                         | List all watchlist entries            |
| POST   | `/watch/list/`                         | Create a watchlist entry              |
| GET    | `/watch/detail/<id>/`                  | Retrieve a watchlist entry            |
| PUT    | `/watch/detail/<id>/`                  | Update a watchlist entry              |
| DELETE | `/watch/detail/<id>/`                  | Delete a watchlist entry              |
| GET    | `/watch/stream/`                       | List stream platforms                 |
| POST   | `/watch/stream/`                       | Create a stream platform              |
| GET    | `/watch/stream/<id>/`                  | Retrieve a stream platform             |
| PUT    | `/watch/stream/<id>/`                  | Update a stream platform               |
| DELETE | `/watch/stream/<id>/`                  | Delete a stream platform               |
| POST   | `/watch/<id>/review-create/`           | Create a review for a watchlist entry |
| GET    | `/watch/<id>/review/`                  | List reviews for a watchlist entry (auth required) |
| GET    | `/watch/review/<id>/`                  | Retrieve a review                      |
| PUT    | `/watch/review/<id>/`                  | Update a review (owner only)          |
| DELETE | `/watch/review/<id>/`                  | Delete a review (owner only)          |

## Permissions

- **`AdminOrReadOnly`** — anyone can read; only admins can write.
- **`ReviewUserOrReadOnly`** — anyone can read; only the review's author can update/delete it (object-level permission).
- Authentication is via `Token` — clients must send `Authorization: Token <token>` after logging in.

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with:
   ```
   SECRET_KEY=your-django-secret-key
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (needed to manage platforms/watchlist via admin):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`, and the Django admin at `/admin/`.

## Notes

- `DEBUG` is currently hardcoded to `True` in `settings.py` — set this to `False` and configure `ALLOWED_HOSTS` before deploying.
- Watchlist rating logic (`avg_rating`) currently averages only the incoming rating with the existing average, not a true running mean across all reviews.
