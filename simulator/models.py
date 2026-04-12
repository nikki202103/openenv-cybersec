from pydantic import BaseModel
from typing import List, Dict, Optional

class Observation(BaseModel):
    available_tools: List[str]
    history: List[Dict]

class State(BaseModel):
    step_index: int
    history: List[Dict]

class StepResult(BaseModel):
    observation: Optional[dict]
    reward: float
    done: bool
    info: dict