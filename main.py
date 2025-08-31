Main Orchestrator
-----------------
- Takes user question (natural language)
- Passes it to Agent 2 (NL-to-SQL Generator)
- Sends generated SQL to Agent 1 (SQL Executor)
- Returns final results
"""

from agents.nl_to_sql_agent import generate_sql
from agents.sql_executor import SQLExecutorAgent

def main():
    # Initialize SQL Executor
    executor = SQLExecutorAgent()

    # Example: user input (replace later with CLI or Streamlit UI)
    user_question = "Which customers ordered the most in 2024?"

    # Step 1: Generate SQL from NL (Agent 2)
    sql_query = generate_sql(user_question)
    print("🔹 Generated SQL:\n", sql_query)

    # Step 2: Execute SQL (Agent 1)
    result = executor.execute_query(sql_query)
    print("\n🔹 Query Results:\n", result)

if __name__ == "__main__":
    main()
