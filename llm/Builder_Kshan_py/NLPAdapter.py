from llm.Builder_Kshan_py.NLPProvider import NLPProvider
from llm.Builder_Kshan_py.UserNLPClient import UserNLPClient

class NLPAdapter:
    @staticmethod
    def getNLPClient(persona: str) -> UserNLPClient:
        nlpClient = UserNLPClient()
 
        return nlpClient
