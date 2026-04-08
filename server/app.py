from env.environment import CyberSecEnv


def main():
    env = CyberSecEnv()

    obs = env.reset()

    total_reward = 0
    step_count = 0

    print("[START] task=cybersec", flush=True)

    done = False
    while not done:
        tools = obs["available_tools"]

        if "scan_log" in tools:
            action = "scan_log"
        elif "flag_alert" in tools:
            action = "flag_alert"
        elif "block_ip" in tools:
            action = "block_ip"
        else:
            action = "escalate_case"

        obs, reward, done, info = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    score = total_reward / step_count if step_count > 0 else 0

    print(f"[END] task=cybersec score={score} steps={step_count}", flush=True)


if __name__ == "__main__":
    main()