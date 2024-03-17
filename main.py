import unittest
from pydantic import BaseModel
from fastapi import FastAPI


# Inializing an instance
app = FastAPI()



# Main App router 
@app.get("/")
async def main():
    return {"Message" : "Hello,World!"}


# Todos : 1 - Pushing this to a Github Repo
