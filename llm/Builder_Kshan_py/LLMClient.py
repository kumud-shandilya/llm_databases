import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"
os.environ["OPENAI_API_BASE"] = "https://syntheticsoai.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "d12cf2ed7e14418ab2fb6783b3414e1a"

import openai
from langchain.llms import OpenAI

from llm.Builder_Kshan_py.ILLMClient import ILLMClient

from abc import ABC, abstractmethod

class LLMClient(ILLMClient):
    def __init__(self):
        self.temperature = 0.0
        self.min_tokens = 100
        self.max_tokens = 500
        self.stop_sequences = []
        self.nucleus_sampling_factor = 0.0
        self.frequency_penalty = 0.74
        self.presence_penalty = 0.0
        self.oai_client = None
        self.uri = "https://syntheticsoai.openai.azure.com/"
        self.api_key = "d12cf2ed7e14418ab2fb6783b3414e1a"

        self.llm = OpenAI(
            openai_api_base = "https://syntheticsoai.openai.azure.com/",
            openai_api_key = "d12cf2ed7e14418ab2fb6783b3414e1a",
            engine= "syntheticsKQL",
            temperature=0.00,
            max_tokens=8000,
            top_p=0.00,
            frequency_penalty=0.00,
            presence_penalty=0.00,
            stop=["#",";"]
            )

    def set_properties(self):
        pass
    def invoke_llm_command_async(self, prompts, model):
        pass