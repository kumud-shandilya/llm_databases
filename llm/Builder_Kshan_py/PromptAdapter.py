from llm.Builder_Kshan_py.PromptBuilder import PromptBuilder
from llm.Builder_Kshan_py.SyntheticsGPTPromptBuilder import SyntheticsGPTPromptBuilder

class PromptAdapter:
    @staticmethod
    def get_prompt_builder() -> PromptBuilder:
        prompt_builder = SyntheticsGPTPromptBuilder()
        return prompt_builder
