from litestar.exceptions import NotAuthorizedException
from piccolo.apps.user.tables import BaseUser
from piccolo_api.session_auth.tables import SessionsBase

from catalog.applications.auth.schemas import (
    SessionUser,
    UserModelLogin,
    UserModelRegister,
)


class AuthService:
    async def user_register(self, data: UserModelRegister) -> dict[str, str]:
        if (
            await BaseUser.exists().where(BaseUser.email == data.email).run()
            or await BaseUser.exists().where(BaseUser.username == data.username).run()
        ):
            user_error = "User with that email or username already exists."
            return {"error": user_error}
        # save user
        query = BaseUser(**data.model_dump())
        _ = await query.save().run()
        return {"message": "User created"}

    async def user_login(self, data: UserModelLogin) -> SessionsBase:
        # login user in
        valid_user = await BaseUser.login(
            username=data.username, password=data.password
        )
        if not valid_user:
            msg = "Invalid username or password"
            raise NotAuthorizedException(msg)
        # create session
        return await SessionsBase.create_session(user_id=valid_user)

    async def user_delete(self, session_user: SessionUser) -> None:
        """
        Delete user
        """
        await BaseUser.delete().where(BaseUser.id == session_user.id).run()


auth_service = AuthService()
