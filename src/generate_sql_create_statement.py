from toolmeta_models import ToolGeneric
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql

print(
    CreateTable(ToolGeneric.__table__)
    .compile(dialect=postgresql.dialect())
)

