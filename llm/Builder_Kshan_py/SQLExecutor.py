import requests
import json
import asyncio

from llm.Builder_Kshan_py.QueryExecutor import QueryExecutor

class SQLExecutor(QueryExecutor):
    async def execute_query(self, query_type: str, query: str) -> str:
        results = ""

        values = {
            "Type": query_type,
            "Query": query.replace("\n", " ")
        }

        try:
            response = requests.post("http://localhost:8000/getData", json=values)
            if response.status_code == 200:
                results = response.json()
        except requests.exceptions.RequestException:
            pass

        return results
