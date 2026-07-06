from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlmodel import Session
from app.crud import create_role, delete_role, get_role, list_roles, update_role
from app.database import create_db_and_tables, get_session
from app.schemas import RoleCreate, RoleRead, RoleUpdate