"""Module for ZeroShot agent for GPT3.5 Turbo"""
import types
from typing import Any, List, Dict, Tuple

from langchain import LLMChain, PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.agents.agent import AgentExecutor
from langchain.agents.mrkl.base import ZeroShotAgent as LangChainZeroShotAgent
from langchain.chat_models import ChatOpenAI
from langchain.experimental import BabyAGI
from langchain.schema import AgentAct.iaion
from langchain.tools.base import BaseTool


from agent.browser_agent import BrowserAgent
from agent.utils import get_agent_tools, get_vectorstore


