from typing import TYPE_CHECKING

from litestar import Litestar, asgi
from piccolo.apps.user.tables import BaseUser
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from piccolo_api.session_auth.tables import SessionsBase

from catalog.config.cors import cors_config
from catalog.config.csrf import csrf_config

if TYPE_CHECKING:
    from litestar.types import Receive, Scope, Send


# mounting Piccolo Admin
@asgi("/admin/", is_mount=True)
async def admin(scope: "Scope", receive: "Receive", send: "Send") -> None:
    _ = create_admin(tables=[BaseUser, SessionsBase])


async def open_database_connection_pool():
    try:
        engine = engine_finder()
        if engine:
            await engine.start_connection_pool()
        else:
            raise Exception
    except Exception:
        print("Unable to connect to the database")


async def close_database_connection_pool():
    try:
        engine = engine_finder()
        if engine:
            await engine.close_connection_pool()
        else:
            raise Exception
    except Exception:
        print("Unable to connect to the database")


app = Litestar(
    route_handlers=[
        admin,
    ],
    cors_config=cors_config,
    csrf_config=csrf_config,
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
