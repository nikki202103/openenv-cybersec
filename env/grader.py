def compute_reward(action, correct, step_index, history):
    reward = 0

    if action == correct:
        reward += 1.0
    elif action in ["flag", "escalate"]:
        reward += 0.5
    else:
        reward -= 1.0

    # penalty for no action
    if action is None:
        reward -= 0.5

    # early detection bonus
    if step_index == 0 and action == correct:
        reward += 0.3

    # repetition penalty
    if len(history) > 0:
        last_action = history[-1]["action"]
        if last_action == action and action != correct:
            reward -= 0.3

    return reward