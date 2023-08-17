from typing import List

from llm.Builder_Kshan_py.PromptBuilder import PromptBuilder

class SyntheticsGPTPromptBuilder(PromptBuilder):
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> List[str]:
        result = ""
        prompts = []
        print("**************************")

        prompts.append("Given an input generate a syntactically correct SQL Query for MSSQL. In Query qualify columns as <TableName>.<ColumnName> format. Use <as> when columns don't have a name")
        prompts.append("### SQL Tables with their properties:\n")
        result = "\n".join(prompts)

        tables = "\n".join(tableschema)

        print(tables)

        result_list = []

        result_list.append(result)
        result_list.append(tables)
        result_list.append("\n### " + userPrompt + "\nSELECT ")

        return result_list

    def ShowPrompts(self) -> None:
        raise NotImplementedError()
