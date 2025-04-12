import logging
from config.config import MONGO_URI, DB_NAME, EXCEL_FILE, BATCH_SIZE, LOG_FILE, SHEET_STRUCTURE
from src.logger import setup_logger
from src.db import connect_to_mongo
from src.data_processor import load_excel, process_sheet
from src.insert_batch import insert_batches

setup_logger(LOG_FILE)

def main():
    try:
        xl = load_excel(EXCEL_FILE)
        db = connect_to_mongo(MONGO_URI, DB_NAME)

        for sheet_name in xl.sheet_names:
            if sheet_name not in SHEET_STRUCTURE:
                logging.warning(f"Skipping sheet '${sheet_name}': No structure defined.")
                continue

            structured_data = process_sheet(xl, sheet_name)
            collection = db[sheet_name]
            insert_batches(structured_data, collection, BATCH_SIZE)

        logging.info("✅ All sheets processed successfully.")
        print("✅ Data inserted. Check logs/insert_log.txt for details.")

    except Exception as e:
        logging.critical(f"❌ Fatal error: ${e}")
        print("❌ Error occurred. See log for details.")

if __name__ == "__main__":
    main()
