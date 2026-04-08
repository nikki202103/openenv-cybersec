from fastapi import FastAPI
from env.environment import CyberSecEnv

app = FastAPI()


# ✅ Root route (fixes "Not Found")
@app.get("/")
def home():
    return {"status": "running"}


# ✅ Your action logic
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


# ✅ REQUIRED main() for validator
def main():
    env = CyberSecEnv()

    obs = env.reset()

    total_reward = 0
    step_count = 0

    print("[START] task=cybersec", flush=True)

    done = False
    while not done:
        action = choose_action(obs)

        obs, reward, done, info = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    score = total_reward / step_count if step_count > 0 else 0

    print(f"[END] task=cybersec score={score} steps={step_count}", flush=True)


# ✅ IMPORTANT (must be present)
if __name__ == "__main__":
    main()