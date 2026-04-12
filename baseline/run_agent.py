import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gradio as gr
from simulator.environment import CyberSecEnv


def run_agent():
    env = CyberSecEnv()
    obs = env.reset()

    logs = []
    total = 0

    while True:
        log = env.scan_log()

        # Decide action
        if "password" in log:
            action = "flag"
            color = "🟡"
        elif "failed login" in log:
            action = "block_ip"
            color = "🔴"
        elif "admin" in log:
            action = "flag"
            color = "🔴"
        elif "data download" in log:
            action = "block_ip"
            color = "🔴"
        else:
            action = "escalate"
            color = "🟢"

        logs.append(f"{color} LOG: {log}")
        logs.append(f"⚡ ACTION: {action}")

        obs, reward, done, info = env.step(action)
        total += reward

        if done:
            break

    return "\n".join(logs), f"{total:.2f}"


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔐 CyberSec AI Dashboard")
    gr.Markdown("### Real-time Threat Detection System")

    with gr.Row():
        with gr.Column(scale=3):
            logs_output = gr.Textbox(label="📜 Live Logs", lines=20)
        with gr.Column(scale=1):
            score_output = gr.Textbox(label="📊 Score")

    run_btn = gr.Button("🚀 Run Simulation")

    run_btn.click(fn=run_agent, inputs=[], outputs=[logs_output, score_output])

demo.launch(server_name="0.0.0.0", server_port=7860)