import uuid
from sqlalchemy import Column, String, Text, ForeignKey, ARRAY
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

    # Semantic function of the input (e.g., "data", "parameter", "config", "predictor")
    role = Column(String)

    # Description for LLM consumption, explaining the purpose and expected content of this input
    description = Column(String)

    # Modality kind (e.g., "tabular", "image", "model") describing general data type
    modality = Column(String)

    # Accepted encodings/formats (e.g., ["csv", "parquet"])
    encoding_formats = Column(ARRAY(String))

    # Schema optionally describing the expected structure of the input (e.g., JSON schema, column names/types) JSONB
    schema = Column(Text)

    # Schema version for compatibility checks
    schema_version = Column(String)

    # Schema type (e.g., "json_schema", "avro", "custom") to indicate how to interpret the schema field
    schema_type = Column(String)

    # Relationship back to parent contract
    contract = relationship("ToolContract", back_populates="inputs")
