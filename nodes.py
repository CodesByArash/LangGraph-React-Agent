from langchain_core.messages import HumanMessage, AIMessage
from llm import LLMWithToolsManager
from typing import cast, Literal

from state import AgentState
from tools import get_tools


tools = get_tools()

llm = LLMWithToolsManager(provider="ollama", model_name="llama3", tools=tools)


def chatbot(state:AgentState)->AgentState:
    """This node will solve the request that user inputs"""
    response = cast(
        AIMessage,
        llm.invoke(
            state["messages"]
        ).content,
    )

    llm.invoke(state["messages"])

    print(f"\nAI: {response.content}")
    return {"messages": [response]}


def route_model_output(state: AgentState) -> Literal["__end__", "tools"]:
    """Determine the next node based on the model's output.

    This function checks if the model's last message contains tool calls.

    Args:
        state (State): The current state of the conversation.

    Returns:
        str: The name of the next node to call ("__end__" or "tools").
    """
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(
            f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
        )
    if not last_message.tool_calls:
        return "__end__"
    return "tools"


