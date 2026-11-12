from fastapi import FastAPI
app=FastAPI(title="loan service")
@app.get("/")
def root(): return {"service":"loan"}