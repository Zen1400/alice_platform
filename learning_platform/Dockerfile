FROM python:3.13.2-slim

# Set environment variables to prevent .pyc files and buffer issues (still not sure what this does)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod +x entrypoint.sh


# Doesn't have access to compose env untill runtime, so it's now in enterpoint
# RUN python manage.py collectstatic --noinput

# CMD ["gunicorn", "learning_platform.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

CMD ["/app/entrypoint.sh"]
