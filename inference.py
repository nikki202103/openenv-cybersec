from env.environment import CyberSecEnv

env = CyberSecEnv()

def reset():
    obs = env.reset()
    return {"observation": obs}

def step(action: str):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }