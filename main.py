import sys
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello dear Kostya"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

def main():
    print(f"Python version: {sys.version}")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

# test 

