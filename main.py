from fastapi import FastAPI, HTTPException
from pipeline import generate_learning_path

app = FastAPI()

@app.get("/roadmap/{career}")
async def get_roadmap(career: str):
    result = generate_learning_path(career)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
