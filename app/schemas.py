from sqlmodel import SQLModel
from datetime import datetime

class RoleCreate(SQLModel):
    company: str
    title: str
    location: str
    work_mode: str
    seniority: str
    status: str = "open"
    source_url: str | None = None
    tech_stack: str = ""
    notes: str | None = None

class RoleUpdate(SQLModel):
    company: str | None = None
    title: str | None = None
    location: str | None = None
    work_mode: str | None = None
    seniority: str | None = None
    status: str | None = None
    source_url: str | None = None
    tech_stack: str | None = None
    notes: str | None = None

class RoleRead(SQLModel):
    id: int
    company: str
    title: str
    location: str
    work_mode: str
    seniority: str
    status: str
    source_url: str | None = None
    tech_stack: str = ""
    notes: str | None = None
    created_at: datetime
    updated_at: datetime