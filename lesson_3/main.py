import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import JSONResponse

app = FastAPI()


data_user = [{"user_id": 1, "full_name": "dsafdsaf"},
             {"user_id": 2, "full_name": "sdf"}]


class UserNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f"User with id {user_id} not found")


@app.get("/user_by_id")
async def root(user_id: int):
    user = next(filter(lambda u: u["user_id"] == user_id, data_user), None)
    if not user:
        # return JSONResponse(content={"error": f"User with id {user_id} not found"},
        #                     status_code=status.HTTP_404_NOT_FOUND)
        raise UserNotFoundException(user_id)
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000)