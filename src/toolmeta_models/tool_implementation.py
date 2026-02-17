from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from toolmeta_models.base import Base


class ToolImplementation(Base):
    __tablename__ = "tool_implementation"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Foreign key to artifact implementing the tool
    artifact_id = Column(
        UUID(as_uuid=True), ForeignKey("tool_artifact.id"), primary_key=True
    )

    # Foreign key to tool contract implemented
    contract_id = Column(
        UUID(as_uuid=True), ForeignKey("tool_contract.id"), primary_key=True
    )

    # Relationships back to parent objects
    artifact = relationship("ToolArtifact", back_populates="implementations")
    contract = relationship("ToolContract", back_populates="implementations")
