from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Store active users {username: websocket}
active_connections = {}

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    active_connections[username] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            message = data.get("message")
            receiver = data.get("to")

            if receiver in active_connections:
                await active_connections[receiver].send_json({
                    "from": username,
                    "message": message
                })
            # Also send back confirmation to sender
            await websocket.send_json({
                "from": "You",
                "message": message
            })
    except WebSocketDisconnect:
        del active_connections[username]
