from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_qdrant import QdrantVectorStore

load_dotenv()

# Vector Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

# Chat model (Gemini, free tier)
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def process_query(query:str):
    print("Searching Chunks", query)
    search_results = vector_db.similarity_search(query=query)

    context = "\n\n\n".join([
    f"Page Content: {result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results
    ])

    SYSTEM_PROMPT = f"""
    You are a helpful AI Assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

    You should only answer the user based on the following context and navigate the user to open the right page number to know more.

    Context:
    {context}
    """

    response = chat_model.invoke([
    ("system", SYSTEM_PROMPT),
    ("human", query),
    ])

    print(f"🤖: {response.content}")