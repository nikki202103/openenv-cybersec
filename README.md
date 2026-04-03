---
title: CyberSec OpenEnv
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
python_version: "3.10"
---

# CyberSec OpenEnv Environment

## Overview
This project implements a cybersecurity incident response simulation environment where an AI agent analyzes logs and performs actions such as:

- scan_log
- flag_alert
- block_ip
- escalate_case

The environment follows the OpenEnv interface and supports multi-step reasoning and reward-based evaluation.

---

## Project Structure

cybersec-openenv/

- env/
  - environment.py
  - tasks.py
  - grader.py

- inference.py  
- demo.py  
- Dockerfile  
- openenv.yaml  
- requirements.txt  
- README.md  

---

## How It Works

- The environment generates cybersecurity logs  
- The agent selects actions based on logs  
- Rewards are calculated based on correctness  
- Multi-step interactions simulate real-world incidents  

---

## Run Locally

pip install -r requirements.txt  
python demo.py  

---

## Hugging Face Space

https://huggingface.co/spaces/Adipanwar123/cybersec-openenv

---

## Features

- Multi-step reasoning environment  
- Tool-based action system  
- Reward-based grading logic  
- Partial observability (noisy logs)  
- OpenEnv compliant API  

---

## Author

Nikhil