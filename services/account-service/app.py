from fastapi import FastAPI
app=FastAPI(title="account service")
@app.get("/")
def root(): return {"service":"account"}