from langchain_ollama.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from typing import List, Optional

class LLMWithToolsManager:
    SUPPORTED_MODELS = {
        "ollama": ChatOllama,
    }

    def __init__(
        self,
        provider: str = "ollama",
        model_name: str = "llama3",
        tools: Optional[List[Tool]] = None,
        **llm_kwargs
    ):
        self.provider = provider.lower()
        self.model_name = model_name
        self.tools = tools or []
        self.llm_kwargs = llm_kwargs

        self.llm = self.SUPPORTED_MODELS[self.provider](model=self.model_name, **self.llm_kwargs)
        self.llm_with_tools = self.llm.bind_tools(self.tools) if self.tools else self.llm

    def add_tool(self, tool: Tool):
        self.tools.append(tool)
        self.llm_with_tools = self.llm.bind_tools(self.tools)

    def invoke(self, prompt: str):
        return self.llm_with_tools.invoke(prompt)