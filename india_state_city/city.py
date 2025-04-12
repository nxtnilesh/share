import json
from datetime import datetime, timezone

with open("state.json", "r") as f:
    states_data = json.load(f)

with open("cities.json", "r") as f:
    cities_data = json.load(f)

state_id_map = {state["name"]: state["_id"]["$oid"] for state in states_data}

current_timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

city_documents = []

for city in cities_data:
    state_name = city.get("state")
    city_name = city.get("city")
    lat = city.get("latitude")
    lon = city.get("longitude")

    if state_name in state_id_map:
        city_doc = {
            "_state": {
                "$oid": state_id_map[state_name]
            },
            "name": city_name,
            "coordinates":{
                "lat": lat,
                "lon":lon
            },
            "createdAt": {
                "$date": current_timestamp
            },
            "updatedAt": {
                "$date": current_timestamp
            }
        }
        city_documents.append(city_doc)

with open("city.json", "w") as f:
    json.dump(city_documents, f, indent=4)

print("✅ Cities saved in city.json with matching _state ObjectIds.")
