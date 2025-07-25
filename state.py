from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from langgraph.managed import IsLastStep
from typing_extensions import Annotated
from typing import TypedDict, List



class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
