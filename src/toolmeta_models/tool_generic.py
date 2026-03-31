import uuid
from sqlalchemy import Column, String, Text, ARRAY, DateTime, func, Integer
from sqlalchemy.dialects.postgresql import JSONB
from toolmeta_models.base import Base


class ToolGeneric(Base):
    __tablename__ = "tool_generic"

    # Primary key: unique identifier for this artifact
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Using an auto-incrementing integer as the primary key for simplicity
    id = Column(Integer, primary_key=True, autoincrement=True)

    uri = Column(String, nullable=False, unique=True)

    name = Column(String, nullable=False)

    version = Column(String, nullable=False)

    # Description oif tool 
    description = Column(Text)

    # Archetype: type of execution artifact (e.g., galaxy_workflow, docker, notebook, service)
    archetype = Column(String, nullable=False)

    # Location or reference to the artifact (URI, registry, file path)
    location = Column(String, nullable=False)

    # Input file formats
    input_file_formats = Column(ARRAY(String))

    # Output file formats
    output_file_formats = Column(ARRAY(String))

    # Input file descriptions
    input_file_descriptions = Column(ARRAY(String))

    # Output file descriptions
    output_file_descriptions = Column(ARRAY(String))

    # License information
    license = Column(String)

    # Keywords list for searchability
    keywords = Column(ARRAY(String))

    # Tag list for categorization
    tags = Column(ARRAY(String))

    # Metadata for extra information, e.g., execution hints, container info
    raw_metadata = Column(JSONB)

    # Metdata schema to validate the raw_metadata field
    metadata_schema = Column(JSONB)

    # Metadata type to indicate how to interpret the metadata field
    metadata_type = Column(String)

    # Metadata version for compatibility checks
    metadata_version = Column(String)

    # Timestamp when the contract was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Timestamp when the contract was last updated
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # User 
    created_by = Column(String)

