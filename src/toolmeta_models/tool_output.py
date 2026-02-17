import uuid
from sqlalchemy import Column, String, Text, ForeignKey
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
    name = Column(String)

    # Description for LLM consumption, explaining the purpose and expected content of this output
    description = Column(Text)

    # Modality kind (e.g., "model", "tabular", "image")
    modality = Column(String)

    # Encoding format (e.g., "pickle", "csv")
    encoding_format = Column(String)

    # Schema optionally describing the structure of the output.
    schema = Column(Text)

    # Schema version for compatibility checks
    schema_version = Column(String)

    # Schema type (e.g., "json_schema", "avro", "custom") to indicate how to interpret the schema field
    schema_type = Column(String)

    # Relationship back to parent contract
    contract = relationship("ToolContract", back_populates="outputs")
