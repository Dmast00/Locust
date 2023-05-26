import pandas as pd

def assign_excel_columns_to_variables(file_path):
    df = pd.read_excel(file_path)
    column_names = df.columns
    variables = {}

    for column_name in column_names:
        variables[column_name] = df[column_name].tolist()

    return variables
