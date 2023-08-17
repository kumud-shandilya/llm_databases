from typing import List
from abc import ABC, abstractmethod

from llm.Builder_Kshan_py.IPromptBuilder import IPromptBuilder

class PromptBuilder(IPromptBuilder):
    @abstractmethod
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> str:
        pass

    @abstractmethod
    def ShowPrompts(self) -> None:
        pass
