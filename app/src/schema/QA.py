from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field

class QA(BaseModel):
    """Question and Answer."""

    question: str = Field(description="Question to answer.")
    answer: str = Field(description="Answer to the question.")
    source: Optional[str] = Field(
        default=None, description="Source of the answer."
    )