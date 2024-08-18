from fastapi import FastAPI
from app.api.vm_router import router as vm_router

app = FastAPI()

app.include_router(vm_router, prefix="/api")
