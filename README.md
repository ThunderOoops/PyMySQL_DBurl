# Flask + SQLAlchemy + PyMySQL API

A simple REST API using Flask, SQLAlchemy, and PyMySQL.

## Setup

```bash
pip install -r requirements.txt
```

Create the database in MySQL:
```sql
CREATE DATABASE flaskdb;
```

Update `config.py` with your MySQL credentials, then run:
```bash
python app.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | Get all users |
| POST | /users | Create a user |
| GET | /users/<id> | Get user by ID |
| DELETE | /users/<id> | Delete user by ID |

## Example

```bash
curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Ram", "email": "ram@example.com"}'
```
