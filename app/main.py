from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def main():
    with open("templates/upload.html", 'r') as f:
        return f.read()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
