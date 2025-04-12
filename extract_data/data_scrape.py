import openpyxl
import json
from bson import ObjectId
from datetime import datetime, timezone

# Load the workbook and select the sheet
workbook = openpyxl.load_workbook("joblo_data.xlsx")
# sheet = workbook["job function"]
# sheet = workbook["Skills"]
sheet = workbook["Industry"]

# Generate proper UTC timestamp
current_timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

# Create a list to store formatted documents
documents = []

for row in sheet.iter_rows(min_row=1, max_col=1, values_only=True):
    if row[0] is not None:
        doc = {
            "_id": {
                "$oid": str(ObjectId())
            },
            "name": row[0],
            "createdAt": {
                "$date": current_timestamp
            },
            "updatedAt": {
                "$date": current_timestamp
            }
        }
        documents.append(doc)

# Save to JSON file
with open("industry.json", "w") as json_file:
    json.dump(documents, json_file, indent=4)

print("Data extracted and saved in MongoDB-style format.")
