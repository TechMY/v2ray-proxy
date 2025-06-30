import asyncio
from quart import Quart, websocket, request
import aiohttp

app = Quart(__name__)

TARGET_URL = 'https://true.mmpctech.xyz'  # ← DO V2Ray IP address here

@app.websocket('/')
async def proxy_ws():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(TARGET_URL, ssl=False) as ws_remote:
            async def from_client():
                async for message in websocket:
                    await ws_remote.send_bytes(message)

            async def to_client():
                async for msg in ws_remote:
                    if msg.type == aiohttp.WSMsgType.BINARY:
                        await websocket.send(msg.data)

            await asyncio.gather(from_client(), to_client())

@app.route('/')
async def index():
    return "Proxy is running"
