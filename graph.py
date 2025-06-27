from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode
from state import AgentState
from tools import get_tools


from nodes import chatbot, route_model_output

import dotenv

dotenv.load_dotenv()

builder = StateGraph(AgentState)
builder.set_entry_point(START)
builder.set_finish_point(END)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(get_tools))


builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    route_model_output,
    {
        "tools":"chatbot",
        "__end__":END
    }
)

builder.add_edge("tools", "chatbot")

graph = builder.compile(name="ReAct Agent")