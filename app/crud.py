from datetime import UTC, datetime
from sqlmodel import Session, select
from app.models import Role
from app.schemas import RoleCreate, RoleUpdate

def create_role(session: Session, role_data: RoleCreate) -> Role:
    role = Role.model_validate(role_data)
    session.add(role)
    session.commit()
    session.refresh(role)
    return role

def list_roles(
    session: Session,
    company: str | None = None,
    location: str | None = None,
    status: str | None = None,
    tech: str | None = None,
    offset: int = 0,
    limit: int = 10,
) -> list[Role]:
    statement = select(Role)
    if company:
        statement = statement.where(Role.company.contains(company))
    if location:
        statement = statement.where(Role.location.contains(location))
    if status:
        statement = statement.where(Role.status.contains(status))
    if tech:
        statement = statement.where(Role.tech_stack.contains(tech))
    statement = statement.offset(offset).limit(limit)
    return (session.exec(statement).all())

def get_role(session: Session, role_id: int) -> Role | None:
    return session.get(Role, role_id)

def update_role(session: Session, role: Role, role_data: RoleUpdate) -> Role:
    update_data = role_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(role, key, value)
    role.updated_at = datetime.now(UTC)
    session.add(role)
    session.commit()
    session.refresh(role)
    return role

def delete_role(session: Session, role: Role) -> None:
    session.delete(role)
    session.commit()