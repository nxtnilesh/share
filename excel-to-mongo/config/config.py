MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "excelToMongo"
EXCEL_FILE = "excel_file/data.xlsx"
BATCH_SIZE = 100
LOG_FILE = "logs/insert_log.txt"

SHEET_STRUCTURE = {
    "Students": lambda row: {
        "name": row.get("Name"),
        "age": int(row.get("Age")) if row.get("Age") else None,
        "enrollment": {
            "id": row.get("EnrollmentID"),
            "course": row.get("Course")
        }
    },
    "Teachers": lambda row: {
        "full_name": row.get("FullName"),
        "department": row.get("Department"),
        "experience_years": int(row.get("Experience")) if row.get("Experience") else 0
    },
    "Courses": lambda row: {
        "code": row.get("CourseCode"),
        "title": row.get("Title"),
        "credits": float(row.get("Credits"))
    }
}
