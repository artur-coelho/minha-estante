import uvicorn

from settings import  USER_REPOSITORY_PORT


def server():
    kwargs = {"host": "0.0.0.0", "port": int(USER_REPOSITORY_PORT), "reload": True}
    
    uvicorn.run("app.main:app", **kwargs)


if __name__ == "__main__":
    server()