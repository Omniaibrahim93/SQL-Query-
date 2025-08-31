Northwind NL-to-SQL Project
Overview
This project uses LangChain and Agentic RAG to convert natural language questions into SQL queries on the Northwind Traders database.
The system consists of two agents:

1. Agent 1 – SQL Executor
- Executes SQL queries on the database.
- Returns results as a DataFrame or table.

2. Agent 2 – NL-to-SQL Generator
- Accepts user questions in natural language.
- Uses FAISS or Chroma to retrieve schema and example query context.
- Generates accurate SQL queries while reducing hallucinations.
Project Structure
northwind_rag_project/
├── data/
│   └── Northwind.db          # SQLite version of the Northwind database
├── agents/
│   ├── nl_to_sql_agent.py    # Agent 2 (NL-to-SQL Generator)
│   └── sql_executor.py       # Agent 1 (SQL Executor)
├── main.py                   # Orchestrator linking both agents
├── requirements.txt
└── README.md
Setup Instructions
1. Open the project in VS Code or any Python IDE.
2. Create a virtual environment:
   python -m venv venv
   # Windows: venv\Scripts\activate
   # Mac/Linux: source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Make sure Northwind.db is placed inside the data/ folder.
Running the Project
1. To generate SQL from a natural language question:
   python agents/nl_to_sql_agent.py
2. To run the full system (generate SQL and execute it):
   python main.py
Sample Questions
- Which customers ordered the most in 2024?
- Top 3 selling product categories in France
- How many suppliers are based in the UK?
- Total revenue in Q2 2023
How RAG Improves SQL Accuracy
- FAISS/Chroma stores schema descriptions and example queries.
- When a question is asked, relevant context is retrieved before generating SQL.
- This reduces hallucinations and ensures correct table and column names.
Notes
- Responses are designed to return in 3–5 seconds.
- Memory can be used to handle follow-up questions in multi-turn conversations.
- Ensure your OpenAI API key is set in your environment before running the project.
