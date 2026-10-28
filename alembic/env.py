import os
from logging.config import fileConfig
from app.pets.pets_model import PetModel
from dotenv import load_dotenv

from alembic import context
from app.shared.database import (
    Base,
)  # Subimos el import arriba para evitar la advertencia

load_dotenv()

config = context.config

#Asegurarse de pasarle un string valido o cadena vacia
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
