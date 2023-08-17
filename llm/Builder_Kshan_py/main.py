from llm.Builder_Kshan_py.PromptController import PromptController
from llm.Builder_Kshan_py.LLMAdapter import LLMAdapter
from llm.Builder_Kshan_py.QueryExecutionAdapter import QueryExecutionAdapter
import json

from ..serializers import UserPromptSerializer

import asyncio

async def test(UserPromptData: UserPromptSerializer):

    print(UserPromptData)
    query = UserPromptData["user_query"]
    table = UserPromptData["table_name"]

    print(query)
    print(table)

    user_prompt = f"{query} from {table}"

    prompt_controller = PromptController()
    prompt_controller.set_persona("user")
    prompt_controller.initialize_prompt_controller()
    prompts = prompt_controller.build_prompts(user_prompt)

    llm_client = LLMAdapter.get_llm_instance()
    llm_client.set_properties()
    kql_query = await llm_client.invoke_llm_command_async(prompts, "")

    query = f"Select {kql_query}".replace('/n', ' ')

    print(query)

    executor = QueryExecutionAdapter.get_query_executor()
    json_data = await executor.execute_query("sql", query)
    # json_data = {"query" : query}
    print(json_data)

    # if not json_data:
    #     json_data = json.dumps({"data": [{"Results": "No records in DB"}]})

    return json_data



