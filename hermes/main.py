import typing as t
from fastapi import FastAPI, Depends
from hermes.utils.db import get_db
from sqlmodel import text, Session, select
from hermes.dto.user import UserRequest
# from hermes.models.users import User
from hashlib import sha256
from hermes.routes import auth, warmup


app = FastAPI()


app.include_router(auth.router)
app.include_router(warmup.router)


@app.get("/")
async def health_check():
    return {
        "message": "Mailr API v0.0.1",
        "status": "ok"
    }



# @app.get("/users")
# async def read_users(session: Session =Depends(get_db)) -> t.List[User]:
#     users = session.exec(select(User))
#     return [user for user in users.all()]


# @app.post("/users")
# async def create_user(user_request: UserRequest, session=Depends(get_db)):

#     user = User(
#         hashed_password=sha256(user_request.password.encode('utf-8')).hexdigest(),
#         **user_request.model_dump(mode="json")
#     )
#     session.add(user)
#     session.commit()

#     return user.id
