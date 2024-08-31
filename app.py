from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from model import make_prediction

app = FastAPI()

# إعداد Jinja2 للقوالب
templates = Jinja2Templates(directory=".")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict")
async def get_prediction(request: Request):
    params = dict(request.query_params)
    prediction = make_prediction(**params)
    return prediction

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)