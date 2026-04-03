import gradio as gr
from baseline.run_agent import run_simulation

def run():
    return run_simulation()

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🛡️ CyberSec AI Agent Dashboard")

    output = gr.Textbox(label="Logs", lines=25)

    btn = gr.Button("Run Simulation")
    btn.click(fn=run, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)