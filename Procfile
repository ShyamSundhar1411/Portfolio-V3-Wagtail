release: python manage.py migrate
web: python manage.py collectstatic --noinput; gunicorn portfolio.wsgi --log-file - --log-level debug