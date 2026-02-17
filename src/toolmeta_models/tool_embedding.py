from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()


class ToolEmbedding(Base):
    """
    Represents a vector embedding for a tool entity.
    Embeddings are model-generated representations of text or structured data,
    used for semantic search, matching, or AI-based reasoning.
    """

    __tablename__ = "embedding"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # The type of entity this embedding belongs to: 'tool_contract', 'tool_concept', 'tool_input'
    entity_type = Column(String, nullable=False, index=True)

    # The ID of the entity the embedding is associated with
    entity_id = Column(Integer, nullable=False, index=True)

    # The specific embedding model used, e.g., "text-embedding-3-large"
    model_name = Column(String, nullable=False)

    # Optionally, the type of embedding: description, schema, summary, etc.
    embedding_type = Column(String, nullable=True)

    # The actual vector; using PostgreSQL pgvector extension
    vector = Column(Vector(1536), nullable=False)

    # Optional hash of the source content used to generate this embedding
    content_hash = Column(String, nullable=True)

    # Additional metadata about the embedding (e.g., prompt, token count)
    emb_metadata = Column(JSONB, nullable=True)

    # Timestamp of when the embedding was created
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    def __repr__(self):
        return f"<Embedding(id={self.id}, entity_type={self.entity_type}, entity_id={self.entity_id}, model={self.model_name})>"
