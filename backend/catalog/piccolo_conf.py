from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from catalog.config import settings

DB = PostgresEngine(
    config={
        "database": settings.db.name,
        "user": settings.db.user,
        "password": settings.db.password,
        "host": settings.db.host,
        "port": settings.db.port,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "piccolo_admin.piccolo_app",
    ]
)
