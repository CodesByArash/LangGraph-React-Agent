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



















# from langchain.llms import ChatOllama
# from langchain.tools import Tool

# class LLMWithToolsManager:
#     def __init__(self, model_name: str = "llama3", tools: list[Tool] = None):
#         self.model_name = model_name
#         self.tools = tools or []
#         self.llm = self._init_llm()
#         self.llm_with_tools = self._bind_tools()

#     def _init_llm(self):
#         return ChatOllama(model=self.model_name)

#     def _bind_tools(self):
#         if self.tools:
#             return self.llm.bind_tools(self.tools)
#         return self.llm

#     def add_tool(self, tool: Tool):
#         self.tools.append(tool)
#         self.llm_with_tools = self.llm.bind_tools(self.tools)

#     def invoke(self, prompt: str) -> str:
#         return self.llm_with_tools.invoke(prompt)

# from langchain_community.chat_models import ChatOllama
# from langchain_community.chat_models import ChatOpenAI
# from langchain.tools import Tool
# from typing import List, Optional, Union

# class LLMWithToolsManager:
#     SUPPORTED_MODELS = {
#         "ollama": ChatOllama,
#         "openai": ChatOpenAI
#     }

#     def __init__(
#         self,
#         provider: str = "ollama",
#         model_name: str = "llama3",
#         tools: Optional[List[Tool]] = None,
#         **llm_kwargs
#     ):
#         self.provider = provider.lower()
#         self.model_name = model_name
#         self.tools = tools or []
#         self.llm_kwargs = llm_kwargs

#         self.llm = self._init_llm()
#         self.llm_with_tools = self._bind_tools()

#     def _init_llm(self):
#         if self.provider not in self.SUPPORTED_MODELS:
#             raise ValueError(
#                 f"Unsupported LLM provider '{self.provider}'. "
#                 f"Supported providers are: {list(self.SUPPORTED_MODELS.keys())}"
#             )

#         LLMClass = self.SUPPORTED_MODELS[self.provider]
#         try:
#             return LLMClass(model=self.model_name, **self.llm_kwargs)
#         except Exception as e:
#             raise RuntimeError(f"Failed to initialize LLM: {e}")

#     def _bind_tools(self):
#         try:
#             return self.llm.bind_tools(self.tools) if self.tools else self.llm
#         except Exception as e:
#             raise RuntimeError(f"Failed to bind tools: {e}")

#     def add_tool(self, tool: Tool):
#         self.tools.append(tool)
#         self.llm_with_tools = self._bind_tools()

#     def invoke(self, prompt: str) -> str:
#         try:
#             return self.llm_with_tools.invoke(prompt)
#         except Exception as e:
#             return f"Error invoking model: {e}"