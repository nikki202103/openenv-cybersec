from env.environment import CyberSecEnv

def choose_action(obs):
    """
    Simple intelligent policy (better than random)
    """
    tools = obs["available_tools"]

    # basic logic (safe + valid)
    if "scan_log" in tools:
        return "scan_log"
    elif "flag_alert" in tools:
        return "flag_alert"
    elif "block_ip" in tools:
        return "block_ip"
    else:
        return "escalate_case"


def main():
    env = CyberSecEnv()

    # START
    obs = env.reset()
    print("[START] task=cybersec", flush=True)

    done = False
    step_count = 0
    total_reward = 0.0

    while not done:
        action = choose_action(obs)

        obs, reward, done, info = env.step(action)

        step_count += 1
        total_reward += float(reward)

        # STEP OUTPUT (STRICT FORMAT)
        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    # END OUTPUT (STRICT FORMAT)
    print(f"[END] task=cybersec score={total_reward} steps={step_count}", flush=True)


# VERY IMPORTANT (DO NOT REMOVE)
if __name__ == "__main__":
    main()