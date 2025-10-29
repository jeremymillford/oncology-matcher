from sqlalchemy import Column, Integer, String
from.database import Base

class GeneProfile(Base):
    __tablename__ = "gene_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    gene = Column(String, nullable=False)
    type = Column(String, nullable=False)
    alteration = Column(String, nullable=False)
    alt_type = Column(String, nullable=False)