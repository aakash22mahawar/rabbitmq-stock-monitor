from fastapi import FastAPI, BackgroundTasks
import subprocess
from apple_stock_monitor import apple_stock_price
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get-stock-price")  #for debugging purpose only
async def get_stock_price():
    try:
        stock_data = apple_stock_price()
        return JSONResponse(content=stock_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/send-stock-price") #for debugging  purpose only
async def send_stock_price(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_pro_script)
    return {"status": "Message is being sent to RabbitMQ in the background"}

def run_pro_script():
    try:
        # Run the pro.py script as a subprocess
        subprocess.run(['python', 'pro.py'], check=True)
    except Exception as e:
        print(f"An error occurred while running pro.py: {e}")

# To run the FastAPI application with Uvicorn
# Use the following command:
# uvicorn main:app --reload
