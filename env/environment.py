import random
from env.tasks import tasks
from env.grader import compute_reward

# -----------------------------
# PARTIAL OBSERVABILITY
# -----------------------------
def add_noise(log):
    if random.random() < 0.3:
        log = log.replace("unknown", "normal")
        log = log.replace("failed", "successful")
    return log


class CyberSecEnv:
    def __init__(self):
        self.task = None
        self.step_index = 0
        self.history = []
        self.current_log = None
        self.last_action = None

    # -------------------------
    # RESET
    # -------------------------
    def reset(self):
        self.task = random.choice(tasks)
        self.step_index = 0
        self.history = []
        self.last_action = None

        return self._get_obs()

    # -------------------------
    # OBSERVATION
    # -------------------------
    def _get_obs(self):
        step = self.task["steps"][self.step_index]
        self.current_log = add_noise(step["log"])

        return {
            "available_tools": [
                "scan_log",
                "flag_alert",
                "block_ip",
                "escalate_case"
            ],
            "history": self.history[-3:]
        }

    # -------------------------
    # TOOLS
    # -------------------------
    def scan_log(self):
        self.last_action = "scan_log"
        return f"LOG: {self.current_log}"

    def flag_alert(self):
        self.last_action = "flag_alert"
        return "Alert flagged"

    def block_ip(self):
        self.last_action = "block_ip"
        return "IP blocked"

    def escalate_case(self):
        self.last_action = "escalate_case"
        return "Case escalated"

    # -------------------------
    # STEP
    # -------------------------
    def step(self, action):
        # 🔥 Execute tool based on action
        if action == "scan_log":
            result = self.scan_log()
        elif action == "flag_alert":
            result = self.flag_alert()
        elif action == "block_ip":
            result = self.block_ip()
        elif action == "escalate_case":
            result = self.escalate_case()
        else:
            result = "Invalid action"

        correct = self.task["steps"][self.step_index]["correct"]

        reward = compute_reward(
            action,
            correct,
            self.step_index,
            self.history
        )

        # Update history
        self.history.append({
            "log": self.current_log,
            "action": action
        })

        # Move to next step
        self.step_index += 1
        done = self.step_index >= len(self.task["steps"])

        obs = None if done else self._get_obs()

        return obs, reward, done, {"correct": correct}

    # -------------------------
    # STATE
    # -------------------------
    def state(self):
        return {
            "step_index": self.step_index,
            "history": self.history
        }