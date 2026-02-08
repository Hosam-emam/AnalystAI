from fastapi import APIRouter
from .agent import agent_router

base_router = APIRouter()

base_router.include_router(router=agent_router, prefix="/agents", tags=["Agents"])
