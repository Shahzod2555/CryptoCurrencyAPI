from src.main import create_app
import uvicorn

run_app = create_app()

if __name__ == "__main__":
	uvicorn.run("app:run_app", reload=True)
