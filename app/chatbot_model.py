# app/chatbot.py
import os
import openai
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_and_combine_pdfs(pdf_paths):
    reader = PDFReader()
    documents = []
    for path in pdf_paths:
        documents.extend(reader.load_data(file=path))
    return documents

def get_index(data, index_name):
    if not os.path.exists(index_name):
        print("Building index:", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

# List of PDF files to be indexed
pdf_paths = ["data/ting.pdf", "data/performance.pdf", "data/fat_loss.pdf", "data/overall_nutrition.pdf"]
combined_data = load_and_combine_pdfs(pdf_paths)
combined_index = get_index(combined_data, "combined_deficiency")
combined_engine = combined_index.as_query_engine()

tools = [
    QueryEngineTool(
        query_engine=combined_engine,
        metadata=ToolMetadata(
            name="nutri_data",
            description="this gives detailed information about common nutritional deficiencies",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

def get_chatbot_response(user_input):
    return str(agent.query(user_input))