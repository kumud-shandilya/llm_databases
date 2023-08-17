from llm.Builder_Kshan_py.MetadataManager import MetadataManager
from llm.Builder_Kshan_py.KQLMetadataManager import KQLMetadataManager

class DomainAdapter:
    @staticmethod
    def getMetadataManager() -> MetadataManager:
        metadataManager = KQLMetadataManager()
        return metadataManager
