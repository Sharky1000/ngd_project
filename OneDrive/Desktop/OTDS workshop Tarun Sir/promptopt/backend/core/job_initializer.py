from pydantic import BaseModel, field_validator
from typing import List, Optional, Literal

class RunConfig(BaseModel):
    task_name: str
    task_type: Literal["classification", "summarization", "extraction", "judge", "generation"]
    mode: Literal["dataset", "nodataset"]
    base_prompt: str
    scorer: Literal["accuracy", "llm_judge"] = "accuracy"
    max_iterations: int = 8
    early_stop_threshold: float = 0.92
    variants_per_iter: int = 5
    dataset: Optional[List[dict]] = None
    criteria: Optional[List[str]] = None

    @field_validator("base_prompt")
    @classmethod
    def validate_prompt_length(cls, v):
        if len(v) > 16000:
            raise ValueError("base_prompt exceeds 16000 chars")
        return v