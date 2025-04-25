from project import Project
from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextLoad:
    def __init__(self, path: str):
        self.path = path

    def load(self):
        """Load the text file and return its content."""
        with open(self.path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
        
    def split(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """Split the content into chunks."""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.all_splits = text_splitter.split_documents([self.content])
        return self.all_splits
    
    def import_as_project(self, project_name: str):
        """Import the text file as a project."""
        self.project = Project(project_name)
        for i in range(len(self.all_splits)):
            self.project.upload_chunk(self.all_splits[i].page_content)

    

        