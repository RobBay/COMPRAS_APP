from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import Base

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}')>"