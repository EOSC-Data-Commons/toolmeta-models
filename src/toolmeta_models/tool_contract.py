import uuid
from sqlalchemy import Column, String, Text, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from toolmeta_models.base import Base


class ToolContract(Base):
    __tablename__ = "tool_contract"

    # Primary key: unique identifier for the contract
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Foreign key to the associated ToolConcept
    concept_id = Column(
        UUID(as_uuid=True), ForeignKey("tool_concept.id"), nullable=False
    )

    # Version string (semantic versioning recommended) of the contract
    version = Column(String, nullable=False)

    # Description aimed at humans and LLMs for semantic matching
    description = Column(Text)

    # Embedding vector for AI similarity search (e.g., OpenAI embeddings)
    embedding = Column(Vector(768))

    # Timestamp when the contract was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    concept = relationship("ToolConcept", back_populates="contracts")
    implementations = relationship(
        "ToolImplementation", back_populates="contract")

    # Relationships to normalized inputs and outputs
    inputs = relationship(
        "ToolInput", back_populates="contract", cascade="all, delete-orphan"
    )
    outputs = relationship(
        "ToolOutput", back_populates="contract", cascade="all, delete-orphan"
    )
