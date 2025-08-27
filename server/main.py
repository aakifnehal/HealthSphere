from fastapi import FastAPI
from auth.routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
