from litestar.config.cors import CORSConfig

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"],
    allow_methods=[
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "PATCH",
        "OPTIONS",
    ],
    allow_headers=["Origin", "Content-Type", "X-CSRFToken"],
    allow_credentials=True,
)
