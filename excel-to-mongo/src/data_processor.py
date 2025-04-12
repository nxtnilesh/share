import pandas as pd
import logging
from config.config import SHEET_STRUCTURE

def load_excel(file_path):
    xl = pd.ExcelFile(file_path)
    logging.info(f"Loaded Excel file: {file_path}")
    return xl

def process_sheet(xl, sheet_name):
    try:
        df = xl.parse(sheet_name)
        formatter = SHEET_STRUCTURE.get(sheet_name)
        if not formatter:
            raise ValueError(f"No formatter defined for sheet '${sheet_name}'")

        structured_docs = [formatter(row) for _, row in df.iterrows()]
        logging.info(f"Processed ${len(structured_docs)} records for sheet '${sheet_name}'")
        return structured_docs

    except Exception as e:
        logging.error(f"Error processing sheet '${sheet_name}': ${e}")
        raise
