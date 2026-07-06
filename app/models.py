from datetime import UTC, datetime
from sqlmodel import SQLModel, Field

class RoleBase(SQLModel):
    company: str
    title: str
    location: str
    work_mode: str
    seniority: str
    status: str = "open"
    source_url: str | None = None
    tech_stack: str = ""
    notes: str | None = None

class Role(RoleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
