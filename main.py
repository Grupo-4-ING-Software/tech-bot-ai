from fastapi import FastAPI
from pipeline import generate_learning_path

app = FastAPI()

@app.get("/roadmap/{career}")
async def get_roadmap(career: str):
    try:
        roadmap = generate_learning_path(career)
        return roadmap
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
