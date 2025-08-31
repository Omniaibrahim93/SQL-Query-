Agent 1: SQL Executor
---------------------
- Connects to Northwind.db (SQLite)
- Executes SQL queries received from Agent 2
- Returns results as a DataFrame or error message
"""

import sqlite3
import pandas as pd

class SQLExecutorAgent:
    def __init__(self, db_path="data/Northwind.db"):
        self.conn = sqlite3.connect(db_path)

    def execute_query(self, sql_query: str):
        try:
            df = pd.read_sql_query(sql_query, self.conn)
            return df
        except Exception as e:
            return f"❌ SQL Execution Error: {e}"

# 🔹 Test run
if __name__ == "__main__":
    executor = SQLExecutorAgent()
    test_query = "SELECT * FROM Customers LIMIT 5;"
    result = executor.execute_query(test_query)
    print(result)
