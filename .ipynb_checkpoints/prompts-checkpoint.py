from llama_index import PromptTemplate

# Detailed instructions for the usage of the generated Python code with pandas
instruction_str = """
1. Convert the query to executable Python code using Pandas.
2. The final line of code should be a Python expression that can be called with the `eval()` function.
3. Ensure the code represents a solution to the query regarding nutrition data analysis.
4. PRINT ONLY THE EXPRESSION, ensuring it is syntactically correct and does not include extraneous quotes.
5. Focus on accuracy and relevance to the query, pulling directly from nutritional data sets.
"""

# Template for prompting which includes dynamic data display and tailored instructions
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe named `df` that includes nutritional data similar to the CDC's Second Nutrition Report.
    Here is a preview of the dataframe (`df.head()`):
    {df_str}

    Please follow these detailed instructions:
    {instruction_str}
    Query: {query_str}

    Write the Python expression that answers the query:
    """
)

# Context description to inform the agent about its operational purpose
context = """Purpose: Assist users by providing accurate information and analysis based on nutrition data.
            This agent aids in interpreting population statistics and specifics about nutrient deficiencies
            and health outcomes from structured data sources like the CDC's NHANES nutrition reports."""
