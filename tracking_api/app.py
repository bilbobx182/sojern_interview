import os
import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from functools import lru_cache

fastapi_app = FastAPI()


# Defaulting to every 25 requests it checks again
@lru_cache(maxsize=25)
def check_file():
    """
    Simple method to check if file exists, allows for caching IO.
    :return: bool
    """
    if os.path.exists('/tmp/ok'):
        return True
    return False


@fastapi_app.get("/ping")
def ping():
    if check_file():
        return JSONResponse("OK", status_code=200)
    else:
        return JSONResponse("Service Unavailable", status_code=503)


@fastapi_app.get("/img")
def get_image():
    """
    Returns a green gif.
    :return: response of image/gif type.
    """
    # First segments of x01 and x01 are the size bytes.
    # https://giflib.sourceforge.net/whatsinagif/bits_and_bytes.html
    gif_bytes = b'GIF89a\x01\x00\x01\x00\x90\x00\x00\x9C\xFF\xFF\x00\x00\x00\x21\xF8\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B'
    response = Response(content=gif_bytes, media_type="image/gif")
    return response


if __name__ == "__main__":
    # Workers to scale it out and handle multiple requests.
    uvicorn.run("app:fastapi_app",
                host=os.getenv('sojernhost', '0.0.0.0'),
                workers=os.getenv('sojernworkers', 2),
                port=(os.getenv('sojernport', 9008)),
                reload=True)
