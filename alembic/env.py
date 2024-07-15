import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la base de datos y los modelos
from app.db.base import Base
from app.models.user import User
from app.models.company import Company
from app.models.plan import Plan
from app.models.subscription import Subscription

# Esto es el objeto de configuración de Alembic, que proporciona acceso
# a los valores dentro del archivo .ini en uso.
config = context.config

# Interpretar el archivo de configuración para Python logging.
# Esta línea configura los loggers básicamente.
fileConfig(config.config_file_name)

print("SQLAlchemy URL: ", config.get_main_option("sqlalchemy.url"))


# Añade el MetaData de tus modelos aquí para 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecuta migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta migraciones en modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
