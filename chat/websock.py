import asyncio
import websockets

async def chat_server(websocket, path):
    async for message in websocket:
        # Handle incoming message
        print(f"Received message: {message}")
        
        # Forward message to other connected clients
        for client in clients:
            if client != websocket:
                await client.send(message)

async def start_chat_server():
    async with websockets.serve(chat_server, "localhost", 8000):
        print("Chat server started!")
        await asyncio.Future()  # Keep the server running indefinitely

# Start the chat server
asyncio.run(start_chat_server())