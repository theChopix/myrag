from db import Collection
from config import config

class Project:
    """A class to represent a project in the database.
    It provides methods to upload chunks of data to the project."""

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.collection = Collection(project_name)

    def upload_chunk(self, file: str):
        
        # check if collection exists
        meta_collection = Collection[config.META_COLLECTION_NAME]
        if not meta_collection.find_document({"project_name": self.project_name}):
            # create collection
            meta_collection.insert_document({"project_name": self.project_name})

        self.collection.insert_document({"file": file})
        # TODO:
        # handle attributes:
         # 'group_id'
         # 'group_name'
         # 'group_order'
         # 'group_type'
         # 'id'