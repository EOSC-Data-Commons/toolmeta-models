import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolArtifact(Base):
    __tablename__ = "tool_artifact"

    # Primary key: unique identifier for this artefact
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)

    version = Column(String, nullable=False)

    # Archetype: type of execution artefact (e.g., galaxy_workflow, docker, notebook, service)
    archetype = Column(String, nullable=False)

    # Location or reference to the artefact (URI, registry, file path)
    location = Column(String, nullable=False)

    # Metadata for extra information, e.g., execution hints, container info
    raw_metadata = Column(Text)

    # Metadata type to indicate how to interpret the metadata field
    metadata_type = Column(String)

    # Metadata version for compatibility checks
    metadata_version = Column(String)

    # Relationship to link artefact to contracts
    implementations = relationship(
        "ToolImplementation", back_populates="artifact")
