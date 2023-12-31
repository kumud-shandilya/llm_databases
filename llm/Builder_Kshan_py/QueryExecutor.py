import abc

from llm.Builder_Kshan_py.IQueryExecutor import IQueryExecutor

class QueryExecutor(IQueryExecutor, abc.ABC):
    @abc.abstractmethod
    async def execute_query(self, query_type: str, query: str) -> str:
        pass
