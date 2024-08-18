from sqlalchemy.orm import Session
from app.infrastructure.repositories.models import VM

class VMRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_vm(self, vm_data: dict):
        """
        Add a new VM record to the database.
        """
        vm = VM(**vm_data)
        self.db_session.add(vm)
        self.db_session.commit()
        self.db_session.refresh(vm)
        return vm

    def get_vm(self, hostnamevm: str):
        """
        Retrieve a VM record from the database by hostname.
        """
        return self.db_session.query(VM).filter(VM.hostnamevm == hostnamevm).first()

    def list_vms(self):
        """
        Retrieve all VM records from the database.
        """
        return self.db_session.query(VM).all()
