from fastapi import FastAPI
from env.environment import CyberSecEnv

app = FastAPI()
env = CyberSecEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: str):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": float(reward),
        "done": bool(done),
        "info": info or {}
    }