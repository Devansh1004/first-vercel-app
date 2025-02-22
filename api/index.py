from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>My Vercel App</title>
        </head>
        <body>
            <h1>Welcome to My First Vercel-Deployed App!</h1>
            <p>This is a simple Python web app deployed using Vercel.</p>
        </body>
    </html>
    """
