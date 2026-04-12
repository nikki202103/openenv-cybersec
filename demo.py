from inference import reset, step, ActionInput

print("=== DEMO START ===")

obs = reset()
print("Initial Observation:", obs)

actions = ["scan_log", "flag_alert", "block_ip", "escalate_case"]

for action in actions:
    result = step(ActionInput(action=action))
    print(f"\nAction: {action}")
    print("Result:", result)
    if result.get('done'):
        break

print("=== DEMO END ===")