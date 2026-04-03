from inference import reset, step

print("=== DEMO START ===")

obs = reset()
print("Initial Observation:", obs)

actions = ["scan_log", "flag_alert", "block_ip", "escalate_case"]

for action in actions:
    result = step(action)
    print(f"\nAction: {action}")
    print("Result:", result)

print("=== DEMO END ===")