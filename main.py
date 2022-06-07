from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/fetch/{url}')
async def fetch(url: str):
    response = requests.get(f'https://{url}')
    return {'response': response.content}
