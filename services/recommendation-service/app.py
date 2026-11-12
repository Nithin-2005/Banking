from fastapi import FastAPI
app=FastAPI(title="recommendation service")
@app.get("/")
def root(): return {"service":"recommendation"}