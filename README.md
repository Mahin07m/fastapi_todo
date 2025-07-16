# FastAPI ToDo Application

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A modern ToDo application built with FastAPI featuring user authentication and task management.

## Features

- ✅ User registration and authentication
- 🔐 JWT token-based security
- 📝 Create, read, update, and delete tasks
- 🔍 Filter and search tasks
- 🐳 Docker-ready for easy deployment
- 🚀 Fast performance with FastAPI

## Prerequisites

- Python 3.9+
- Docker (optional)
- Docker Compose (optional)

## Getting Started

### Docker

1. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

2. The API will be available at:
   ```
   http://localhost:8000/docs
   ```

3. To stop the containers:
   ```bash
   docker-compose down
   ```

## Docker Details

The project includes the following Docker configuration:

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```


## API Documentation

After starting the application, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
fastapi_todo/
├── routers/
│   ├── authentication.py
│   ├── task.py
│   ├── token.py
│   └── user.py
├── database.py
├── hashing.py
├── main.py
├── models.py
├── oauth2.py
├── requirements.txt
├── schemas.py
├── Dockerfile

```

## Environment Variables

Create a `.env` file for environment variables:

```
DATABASE_URL=sqlite:///./user.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:
- Mahin - [GitHub Profile](https://github.com/Mahin07m)
