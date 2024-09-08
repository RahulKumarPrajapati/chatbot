from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# My own exception handler class
class ExceptionHandler(Exception):
    def __init__(self, name, status_code, msg = ""):
        self.name= name
        self.status_code = status_code
        self.msg = msg

# # My own exception handler
@app.exception_handler(ExceptionHandler)
async def exception_handler(req: Request, exc: ExceptionHandler):
    return JSONResponse(
        status_code= exc.status_code,
        content= {"message": f"Oops! Error --> {exc.name} occurred", "description": exc.msg}
    )