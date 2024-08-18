from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VM(Base):
    __tablename__ = 'vms'

    id = Column(Integer, primary_key=True, index=True)
    addressip = Column(String, index=True)
    hostname = Column(String)
    gateway = Column(String)
    nameserver = Column(String)
    RAM = Column(Integer)
    CPU = Column(Integer)
    hostnamevm = Column(String, unique=True)
    size = Column(Integer)
    proxy = Column(String)
    network = Column(String)
    tenant_name = Column(String)
    template_name = Column(String)
