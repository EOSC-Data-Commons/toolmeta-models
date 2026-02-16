import uuid
from sqlalchemy import Column, String, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolOutput(Base):
    __tablename__ = "tool_output"

    # Primary key: unique identifier for this output
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Foreign key to parent contract
    contract_id = Column(
        UUID(as_uuid=True), ForeignKey("tool_contract.id"), nullable=False
    )

    # Output name (e.g., "model")
    name = Column(String, nullable=False)

    # Modality kind (e.g., "model", "tabular", "image")
    modality_kind = Column(String, nullable=False)

    # Encoding format (e.g., "pickle", "csv")
    encoding_format = Column(String)

    # Guarantees or postconditions (e.g., ["trained_linear_model"])
    guarantees = Column(ARRAY(String))

    # Relationship back to parent contract
    contract = relationship("ToolContract", back_populates="outputs")
