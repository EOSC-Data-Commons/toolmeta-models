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

    # Version string (semantic versioning recommended) of the contract
    contract_version = Column(String, nullable=False)

    # Description aimed at humans and LLMs for semantic matching
    description = Column(Text)

    # Timestamp when the contract was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Timestamp when the contract was last updated
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    implementations = relationship(
        "ToolImplementation", back_populates="contract")

    # Relationships to normalized inputs and outputs
    inputs = relationship(
        "ToolInput", back_populates="contract", cascade="all, delete-orphan"
    )
    outputs = relationship(
        "ToolOutput", back_populates="contract", cascade="all, delete-orphan"
    )
