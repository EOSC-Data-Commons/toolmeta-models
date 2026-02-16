import uuid
from sqlalchemy import Column, String, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolVariable(Base):
    __tablename__ = "tool_variable"

    # Primary key: unique identifier for this variable
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Foreign key to the input this variable belongs to
    input_id = Column(UUID(as_uuid=True), ForeignKey(
        "tool_input.id"), nullable=False)

    # Variable name (e.g., "X", "y")
    name = Column(String, nullable=False)

    # Datatype of the variable (e.g., "numeric", "string", "boolean")
    datatype = Column(String, nullable=False)

    # Shape of the variable (e.g., ["n", "p"] for 2D array)
    shape = Column(ARRAY(String))

    # Relationship back to parent input
    input = relationship("ToolInput", back_populates="variables")
