"""
from typing import List
from azure.ai.language.lro import CompletionsOptions
from azure.core.credentials import AzureKeyCredential
from azure.ai.language import LanguageModelCredential, LanguageModelApi

import LLMClient

class GPTClient(LLMClient.LLMClient):
    def __init__(self):
        super().__init__()
        self.model_name = "syntheticsKQL"

    async def get_completions_async(self, prompts: List[str]) -> str:
        final_prompt = "\n".join(prompts)

        completions_options = CompletionsOptions(
            prompts=[final_prompt],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop_sequences=["#", ";"],
            nucleus_sampling_factor=self.nucleus_sampling_factor,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )

        completions_response = await self.oai_client.begin_completions(
            deployment_or_model_name=self.model_name,
            options=completions_options
        ).result()

        completions = completions_response.value
        response_kql = completions[0].text
        return response_kql

    async def invoke_llm_command_async(self, prompts: List[str], model: str) -> str:
        kql_query = await self.get_completions_async(prompts)
        return kql_query

    """


#import openai
import asyncio

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from typing import List
from llm.Builder_Kshan_py.LLMClient import LLMClient

class GPTClient(LLMClient): 
    def __init__(self):
        super().__init__()
        self.model_name = "syntheticsKQL"


    async def get_completions_async(self, prompts: List[str]) -> str:
        final_prompt1 = "\n".join(prompts)

        print(final_prompt1)

        llm = LLMClient().llm

        final_prompt = "{prompts_str} \n {table_schema} \n {user_prompt}"

        prompt_llm = PromptTemplate.from_template(final_prompt)

        chain = LLMChain(
            llm = llm, 
            prompt = prompt_llm
            )

        return chain.run({'prompts_str': prompts[0], 'table_schema': prompts[1], 'user_prompt': prompts[2]})

        """completionsResponse = openai.Completion.create(
            engine="syntheticsKQL",
            prompt = final_prompt1,
            temperature=0.0,
            max_tokens=500,
            top_p=0.0,
            frequency_penalty=0.00,
            presence_penalty=0.0,
            stop=["#",";"]
        )

        completions = completionsResponse.values
        print(completionsResponse.choices[0]["text"])"""
        #return "hii"
  
    def invoke_llm_command_async(self, prompts: List[str], model: str) -> str:
        kql_query = self.get_completions_async(prompts)
        return kql_query

 
async def test():
    obj = GPTClient()

    prompts = "### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\n\nSELECT"

    result = await obj.get_completions_async(prompts)

    print(result)










