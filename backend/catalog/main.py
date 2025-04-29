import uvicorn

from catalog.config import settings

if __name__ == "__main__":
    uvicorn.run(
        app="application:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.debug,
    )
