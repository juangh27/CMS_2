import websocket

url = "ws://localhost:8000/ws/practiceConsumer/"  # Replace with your WebSocket URL

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with status code {close_status_code}: {close_msg}")

def on_open(ws):
    print("WebSocket connection established")
    # Send a health check message
    ws.send('{"event": "health_check"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()