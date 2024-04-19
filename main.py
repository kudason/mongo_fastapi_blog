### ========== Import Library ========== ###
from fastapi import FastAPI              ###
from routes.routes import endPoints      ###
### ========== Import Library ========== ###


# Create instant
app = FastAPI()

app.include_router(endPoints)