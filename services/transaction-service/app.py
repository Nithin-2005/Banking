from fastapi import FastAPI
app=FastAPI(title="transaction service")
@app.get("/")
def root(): return {"service":"transaction"}