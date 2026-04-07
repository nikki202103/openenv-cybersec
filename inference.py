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
    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        }
    }

@app.post("/step")
def step(action: str):
    obs, reward, done, info = env.step(action)

    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info or {}
    }