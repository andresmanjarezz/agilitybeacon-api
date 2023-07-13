from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.roles import roles_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.applicationurl import applicationurls_router
from app.api.api_v1.routers.jobs import jobs_router
from app.api.api_v1.routers.playbooks import playbook_router
from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app import tasks


app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    roles_router,
    prefix="/api/v1",
    tags=["roles"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    applicationurls_router,
    prefix="/api/v1",
    tags=["application-urls"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    jobs_router,
    prefix="/api/v1",
    tags=["jobs"],
)
app.include_router(
    playbook_router,
    prefix="/api/v1",
    tags=["playbook"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
