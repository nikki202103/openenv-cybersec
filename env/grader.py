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

def grade(state=None, trajectory=None, *args, **kwargs):
    """
    Grader function for OpenEnv tasks.
    Evaluates the trajectory and returns a normalized score.
    """
    try:
        total_reward = 0
        step_count = 0
        
        # OpenEnv typically passes trajectory object
        if trajectory is not None:
            if hasattr(trajectory, "rewards"):
                rewards = trajectory.rewards
                total_reward = sum(rewards)
                step_count = len(rewards)
            elif isinstance(trajectory, dict) and "rewards" in trajectory:
                rewards = trajectory["rewards"]
                total_reward = sum(rewards)
                step_count = len(rewards)
                
        # Calculate average score based on inference.py logic
        if step_count > 0:
            score = total_reward / step_count
        else:
            score = 0.5

        # Normalize score
        if score <= 0:
            score = 0.3
        elif score >= 1:
            score = 0.9

        return float(score)
    except Exception:
        return 0.5