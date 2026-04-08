from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberSecEnv

app = FastAPI()

env = CyberSecEnv()


# ✅ Root route
@app.get("/")
def home():
    return {"status": "running"}


# ✅ RESET ENDPOINT (VERY IMPORTANT)
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        }
    }


# ✅ STEP ENDPOINT (VERY IMPORTANT)
class ActionInput(BaseModel):
    action: str


@app.post("/step")
def step(input: ActionInput):
    obs, reward, done, info = env.step(input.action)

    return {
        "observation": {
            "available_tools": obs["available_tools"],
            "history": obs["history"]
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info or {}
    }


# =========================
# ✅ VALIDATION PART (DO NOT REMOVE)
# =========================

def choose_action(obs):
    tools = obs["available_tools"]

    if "scan_log" in tools:
        return "scan_log"
    elif "flag_alert" in tools:
        return "flag_alert"
    elif "block_ip" in tools:
        return "block_ip"
    else:
        return "escalate_case"


def main():
    env_local = CyberSecEnv()

    obs = env_local.reset()

    total_reward = 0
    step_count = 0

    print("[START] task=cybersec", flush=True)

    done = False
    while not done:
        action = choose_action(obs)

        obs, reward, done, info = env_local.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    score = total_reward / step_count if step_count > 0 else 0

    print(f"[END] task=cybersec score={score} steps={step_count}", flush=True)


if __name__ == "__main__":
    main()