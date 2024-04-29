from llama_index.core import PromptTemplate
instruction_str = """\
1. Convert the user's query into executable Python code using Pandas on the DataFrame named 'df'.
2. Preprocess the 'Description' column for enhanced search accuracy by:
   - Converting text to lowercase.
   - Removing all non-alphanumeric characters except spaces.
3. Identify and extract the singular keywords from the user's query that specifically refer to the food item. Ensure these keywords are checked in the preprocessed 'Description' column using logical AND to combine conditions.
4. Chain string methods to preprocess and verify the conditions for the food item within the same line of code to streamline processing.
5. Apply the combined conditions to filter the DataFrame. Retrieve the first row that meets these conditions using `.head(1)`.
6. Based on the user's query, dynamically identify and extract the specific nutrient value from the appropriate column. Ensure you use the column name that corresponds to the requested nutrient. This should be derived directly from the user's query, not assumed or hardcoded.
7. Nutrient Columns: "Data.Alpha Carotene","Data.Beta Carotene","Data.Beta Cryptoxanthin","Data.Carbohydrate","Data.Cholesterol","Data.Choline","Data.Fiber","Data.Lutein and Zeaxanthin","Data.Lycopene","Data.Niacin","Data.Protein","Data.Retinol","Data.Riboflavin","Data.Selenium","Data.Sugar Total","Data.Thiamin","Data.Water","Data.Fat.Monosaturated Fat","Data.Fat.Polysaturated Fat","Data.Fat.Saturated Fat","Data.Fat.Total Lipid","Data.Major Minerals.Calcium","Data.Major Minerals.Copper","Data.Major Minerals.Iron","Data.Major Minerals.Magnesium","Data.Major Minerals.Phosphorus","Data.Major Minerals.Potassium","Data.Major Minerals.Sodium","Data.Major Minerals.Zinc","Data.Vitamins.Vitamin A - RAE","Data.Vitamins.Vitamin B12","Data.Vitamins.Vitamin B6","Data.Vitamins.Vitamin C","Data.Vitamins.Vitamin E","Data.Vitamins.Vitamin K"\
8. The final line of code should be a Python expression that can be called with the `eval()` function.
9. The code should represent a solution to the query.
10. PRINT ONLY THE EXPRESSION.
11. Do not quote the expression."""








new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about the specific nutritional content of various foods. The data is sourced from the 'food.csv' file,
            which includes a comprehensive list of foods along with their macro and micronutrient profiles. This agent is designed to output specific
            nutrient values for the user requested foods.
            Dataset Description: The data in 'food.csv' comes from the United States Department of Agriculture’s Food Composition Database. It includes information on various types of food, detailing the amounts of different vitamins, minerals, and macronutrient percentages. The food variety ranges from everyday items to specific brands, encompassing a wide array of nutrients tracked. This extensive dataset aids in providing detailed nutritional information to users, facilitating informed dietary choices based on scientifically backed data.

            Key Data Fields:
            - Category: General category of the food item.
            - Description: Detailed description including category and subcategories.
            - Nutrient Columns: "Data.Alpha Carotene","Data.Beta Carotene","Data.Beta Cryptoxanthin","Data.Carbohydrate","Data.Cholesterol","Data.Choline","Data.Fiber","Data.Lutein and Zeaxanthin","Data.Lycopene","Data.Niacin","Data.Protein","Data.Retinol","Data.Riboflavin","Data.Selenium","Data.Sugar Total","Data.Thiamin","Data.Water","Data.Fat.Monosaturated Fat","Data.Fat.Polysaturated Fat","Data.Fat.Saturated Fat","Data.Fat.Total Lipid","Data.Major Minerals.Calcium","Data.Major Minerals.Copper","Data.Major Minerals.Iron","Data.Major Minerals.Magnesium","Data.Major Minerals.Phosphorus","Data.Major Minerals.Potassium","Data.Major Minerals.Sodium","Data.Major Minerals.Zinc","Data.Vitamins.Vitamin A - RAE","Data.Vitamins.Vitamin B12","Data.Vitamins.Vitamin B6","Data.Vitamins.Vitamin C","Data.Vitamins.Vitamin E","Data.Vitamins.Vitamin K"
            """

