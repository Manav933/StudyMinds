# StudyMinds - Student Notes Sharing Platform

A comprehensive platform for students to share and manage study notes, built with Django.

## Features

- User authentication and profile management
- Note upload and management
- Rating and review system
- Advanced search and filtering
- Bookmark system
- Comments and discussions
- Email notifications
- Admin dashboard

## Tech Stack

- Backend: Django
- Frontend: HTML, CSS, Bootstrap, JavaScript
- Database: SQLite (Development) / PostgreSQL (Production)
- Media Handling: Django's MEDIA_URL and MEDIA_ROOT

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd StudyMinds
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file in the root directory:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

## Project Structure

- `users/` - User authentication and profile management
- `notes/` - Note upload, listing, and download functionality
- `ratings/` - Review and rating system

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 