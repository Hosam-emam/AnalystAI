from fastapi import APIRouter

agent_router = APIRouter()

@agent_router.get("/")
def root():
    return {"response": "Agent server is online!", "status_code": 200}

