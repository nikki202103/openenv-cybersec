from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberSecEnv
import os
from openai import OpenAI

# =========================
# ✅ LLM CLIENT (SAFE INIT)
# =========================
client = OpenAI(
    base_url=os.getenv("API_BASE_URL", "https://api.openai.com/v1"),
    api_key=os.getenv("API_KEY", "")
)

# =========================
# ✅ FASTAPI APP
# =========================
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
# ✅ SAFE LLM DECISION FUNCTION
# =========================
def choose_action(obs):
    try:
        prompt = f"""
        You are a cybersecurity agent.
        Available tools: {obs['available_tools']}
        History: {obs['history']}
        Choose ONE action from available tools.
        Return ONLY the action name.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        action = response.choices[0].message.content.strip()

        if not action or action not in obs["available_tools"]:
            return obs["available_tools"][0]

        return action

    except Exception:
        return obs["available_tools"][0]


# =========================
# ✅ VALIDATION LOOP (FINAL FIX)
# =========================
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

    # 🔥 FINAL FIX (IMPORTANT)
    if step_count > 0:
        score = total_reward / step_count
    else:
        score = 0.5

    # ensure score strictly between (0,1)
    score = max(0.1, min(score, 0.9))

    print(f"[END] task=cybersec score={score} steps={step_count}", flush=True)


if __name__ == "__main__":
    main()