import uuid
from sqlalchemy import Column, String, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolInput(Base):
    __tablename__ = "tool_input"

    # Primary key: unique identifier for this input port
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Foreign key to the parent contract
    contract_id = Column(
        UUID(as_uuid=True), ForeignKey("tool_contract.id"), nullable=False
    )

    # Name of the input (e.g., "training_data")
    name = Column(String, nullable=False)

    # Modality kind (e.g., "tabular", "image", "model") describing general data type
    modality_kind = Column(String, nullable=False)

    # Modality structure (optional, e.g., "rectangular", "3D array")
    modality_structure = Column(String)

    # Accepted encodings/formats (e.g., ["csv", "parquet"])
    encoding_formats = Column(ARRAY(String))

    # Structural constraints expressed as strings (e.g., ["X.rows == y.rows", "n >= p+1"])
    constraints = Column(ARRAY(String))

    # Assumptions for validity (e.g., ["linearity", "iid_samples"])
    assumptions = Column(ARRAY(String))

    # Relationship back to parent contract
    contract = relationship("ToolContract", back_populates="inputs")

    # Relationship to variables defined on this input
    variables = relationship(
        "ToolVariable", back_populates="input", cascade="all, delete-orphan"
    )
