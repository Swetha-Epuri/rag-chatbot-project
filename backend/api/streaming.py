from fastapi.responses import StreamingResponse
import asyncio


async def stream_response(text):
    
    words = text.split()

    for word in words:

        yield word + " "

        await asyncio.sleep(0.02)
        