from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberSecEnv

app = FastAPI()
env = CyberSecEnv()

class ActionInput(BaseModel):
    action: str

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
def step(input: ActionInput):
    obs, reward, done, info = env.step(input.action)

    return {
        "observation": {
            "available_tools": obs["available_tools"] if obs else [],
            "history": obs["history"] if obs else []
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }