from litestar import Request
from litestar.controller import Controller
from litestar.datastructures import Cookie
from litestar.handlers import delete, post
from litestar.response import Response
from litestar.status_codes import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from catalog.applications.auth.guards import current_user, current_user_guard
from catalog.applications.auth.schemas import UserModelLogin, UserModelRegister
from catalog.applications.auth.services import auth_service


class AuthController(Controller):
    path = "/accounts"
    tags = ("Accounts",)

    @post("/register")
    async def register(self, data: UserModelRegister) -> dict[str, str]:
        """
        Register user
        """
        return await auth_service.user_register(data=data)

    @post("/login")
    async def login(self, data: UserModelLogin) -> Response:
        """
        Login and authenticate user
        """
        session = await auth_service.user_login(data=data)
        return Response(
            content={"message": "Succesfully logged in"},
            status_code=HTTP_201_CREATED,
            cookies=[
                Cookie(
                    key="id",
                    value=f"{session['token']}",
                    max_age=3600,
                    httponly=True,
                )
            ],
        )

    @post("/logout")
    async def logout(self) -> Response:
        """
        Logout user
        """
        response = Response(
            content={"message": "Succesfully logged out"},
            status_code=HTTP_201_CREATED,
        )
        response.delete_cookie(key="id")
        return response

    @delete("/delete", guards=[current_user_guard])
    async def delete_user(self, request: Request) -> None:
        """
        Delete user
        """
        session_user = await current_user(request)
        if session_user:
            await auth_service.user_delete(session_user=session_user)

        response = Response(
            content=None,
            status_code=HTTP_204_NO_CONTENT,
        )
        response.delete_cookie(key="id")
