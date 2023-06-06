from typing import List

from langchain.agents import Tool
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools.base import BaseTool
from langchain.vectorstores import FAISS

##connecting with Selenium wrapper