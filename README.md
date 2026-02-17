# FastAPI Chat Application

This project is a simple chat application built using FastAPI, allowing two clients to communicate with each other in real-time via WebSockets. All chat history is cleared when the application is closed.

## Features

- Real-time chat between two clients
- WebSocket support for live messaging
- Temporary chat history that resets on application shutdown

## Project Structure

```
fastapi-private-chat/
│
├── main.py
├── templates/
│   └── index.html
├── requirements.txt
└── Dockerfile            # Docker image instructions
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-chat-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI application, run:
```
uvicorn src.main:app --reload
```