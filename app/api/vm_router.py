from fastapi import APIRouter, HTTPException, Depends
from app.domain.vm_service import VMService
from app.models.vm_request import VMCreateRequest

router = APIRouter()

# Dependency to get VMService
def get_vm_service():
    return VMService()  # Assuming VMService does not need any parameters for now

@router.post("/create_vm")
async def create_vm(vm_request: VMCreateRequest, service: VMService = Depends(get_vm_service)):
    try:
        result = service.create_vm(vm_request)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
