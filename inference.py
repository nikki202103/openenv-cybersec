from env.environment import CyberSecEnv

env = CyberSecEnv()

def reset():
    obs = env.reset()
    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        }
    }

def step(action: str):
    obs, reward, done, info = env.step(action)
    
    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }