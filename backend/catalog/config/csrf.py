from litestar.config.csrf import CSRFConfig

from catalog.config import settings

csrf_config = CSRFConfig(
    secret=settings.app.secret_key,
    safe_methods={
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "PATCH",
        "OPTIONS",
    },
)
