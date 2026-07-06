from fastapi import FastAPI

app = FastAPI(
    title="AscendAI API",
    description="Backend API for AscendAI - AI Powered Career Operating System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AscendAI 🚀",
        "status": "Backend is running successfully"
    }