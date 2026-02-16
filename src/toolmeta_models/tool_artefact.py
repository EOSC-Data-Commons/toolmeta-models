import uuid
from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolArtefact(Base):
    __tablename__ = "tool_artefact"

    # Primary key: unique identifier for this artefact
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Archetype: type of execution artefact (e.g., galaxy_workflow, docker, notebook, service)
    archetype = Column(String, nullable=False)

    # Location or reference to the artefact (URI, registry, file path)
    location = Column(Text, nullable=False)

    # Metadata for extra information, e.g., execution hints, container info
    metadata = Column(JSON)

    # Relationship to link artefact to contracts
    implementations = relationship("ToolImplementation", back_populates="artefact")
