# Use official Python image
FROM python:3.9-slim


LABEL org.opencontainers.image.source="https://github.com/Mahin07m/fastapi_todo"

RUN apt-get update

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set working directory
WORKDIR /app

# Copy only necessary files
COPY ./requirements.txt .
COPY ./main.py .
COPY ./database.py .
COPY ./hashing.py .
COPY ./models.py .
COPY ./oauth2.py .
COPY ./schemas.py .
COPY ./routers/ ./routers/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]