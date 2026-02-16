import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolConcept(Base):
    __tablename__ = "tool_concept"

    # Primary key: unique identifier for the semantic concept
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Human-readable name of the tool concept (e.g., "Linear Regression Training")
    name = Column(String, nullable=False)

    # Free-text description for humans and LLM consumption
    description = Column(Text)

    # Relationship: all contracts associated with this concept
    contracts = relationship("ToolContract", back_populates="concept")

    # Relationship: all artefacts implementing this concept
    implementations = relationship("ToolImplementation", back_populates="concept")
