from fastapi import FastAPI


app = FastAPI(title="Support Desk API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
