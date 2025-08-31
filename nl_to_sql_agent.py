Agent 2: NL-to-SQL Generator with RAG
-------------------------------------
- Uses LangChain + FAISS to retrieve schema context
- Generates SQL queries from natural language questions
"""

from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 🔹 إعداد الـ docs (schema + sample queries)
docs = [
    Document(page_content="Customers table: CustomerID, CompanyName, ContactName, Country"),
    Document(page_content="Orders table: OrderID, CustomerID, EmployeeID, OrderDate, ShipCountry"),
    Document(page_content="OrderDetails table: OrderID, ProductID, UnitPrice, Quantity, Discount"),
    Document(page_content="Products table: ProductID, ProductName, SupplierID, CategoryID, UnitPrice"),
    Document(page_content="Suppliers table: SupplierID, CompanyName, ContactName, Country"),
    Document(page_content="Categories table: CategoryID, CategoryName, Description"),

    # Sample queries
    Document(page_content="Which customers ordered the most in 2024? Needs Customers + Orders + OrderDetails"),
    Document(page_content="Top 3 selling product categories in France -> Products + Categories + Orders + OrderDetails"),
    Document(page_content="How many suppliers are based in the UK? -> Suppliers"),
    Document(page_content="Total revenue in Q2 2023? -> Orders + OrderDetails"),
]

# 🔹 FAISS Vector Store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# 🔹 LLM + RetrievalQA
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
retrieval_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

# 🔹 Function to generate SQL
def generate_sql(user_question: str) -> str:
    sql_query = retrieval_chain.run(user_question)
    return sql_query

# 🔹 Run test
if __name__ == "__main__":
    question = "Which customers ordered the most in 2024?"
    sql_query = generate_sql(question)

    print("User Question:", question)
    print("Generated SQL:\n", sql_query)
