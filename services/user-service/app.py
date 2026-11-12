from fastapi import FastAPI
app=FastAPI(title="user service")
@app.get("/")
def root(): return {"service":"user"}