from uuid import uuid4

from sqlalchemy import (Column, ForeignKey, String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import UUIDType


# Create Base class
BaseModel = declarative_base()


def get_session(db_file):
    engine = create_engine('sqlite:///{}'.format(db_file))
    BaseModel.metadata.create_all(engine, checkfirst=True)
    return sessionmaker(bind=engine)()


class Location(BaseModel):
    __tablename__ = 'locations'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    title = Column(String)
    description = Column(String, unique=True)
    alias = Column(String, unique=True, nullable=True)


class Exit(BaseModel):
    __tablename__ = 'exits'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    source_id = Column(UUIDType(binary=False), ForeignKey('source.id'))
    source = relationship("Location", back_populates="exits")
    destination_id = Column(UUIDType(binary=False),
                            ForeignKey('destination.id'))
    destination = relationship("Location")
    direction = Column(String)
