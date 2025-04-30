from litestar import Request
from litestar.connection import ASGIConnection
from litestar.exceptions import NotAuthorizedException
from litestar.handlers import BaseRouteHandler
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.tables import SessionsBase

from catalog.applications.auth.schemas import SessionUser


# guard for protected endpoints
def current_user_guard(connection: ASGIConnection, _: BaseRouteHandler) -> None:
    if not connection.cookies.get("id"):
        raise NotAuthorizedException()


async def current_user(request: Request) -> SessionUser | None:
    data = (
        await SessionsBase.select(SessionsBase.user_id)
        .where(SessionsBase.token == request.cookies.get("id"))
        .first()
        .run()
    )
    if data:
        session_user = (
            await BaseUser.select(
                BaseUser.id,
                BaseUser.username,
                BaseUser.email,
                BaseUser.last_login,
            )
            .where(BaseUser._meta.primary_key == data["user_id"])  # noqa: SLF001
            .first()
            .run()
        )
        return SessionUser.model_validate(session_user)
    return None
