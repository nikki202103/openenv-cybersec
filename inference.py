from env.environment import CyberSecEnv

env = CyberSecEnv()

def run():
    obs = env.reset()
    total = 0

    while True:
        log = env.scan_log()

        if "password" in log:
            action = "flag_alert"
        elif "failed login" in log:
            action = "block_ip"
        else:
            action = "escalate_case"

        obs, reward, done, info = env.step(action)
        total += reward

        if done:
            break

    return {"final_score": total}