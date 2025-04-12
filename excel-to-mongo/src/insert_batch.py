from pymongo import errors
import logging

def insert_batches(data, collection, batch_size):
    total = len(data)
    for i in range(0, total, batch_size):
        batch = data[i:i + batch_size]
        try:
            collection.insert_many(batch, ordered=False)
            logging.info(f"Inserted batch ${i // batch_size + 1} (${len(batch)} records) into '${collection.name}'")
        except errors.BulkWriteError as bwe:
            logging.warning(f"Bulk write error in batch ${i // batch_size + 1} for collection '${collection.name}'")
            for error in bwe.details.get("writeErrors", []):
                logging.error(f"  - Index: ${error['index']}, Error: ${error['errmsg']}")
