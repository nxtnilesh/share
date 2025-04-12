import json
from datetime import datetime, timezone

states_to_extract = [
  "Andaman and Nicobar Islands",
  "Andhra Pradesh",
  "Arunachal Pradesh",
  "Assam",
  "Bihar",
  "Chandigarh",
  "Chhattisgarh",
  "Dadra and Nagar Haveli and Daman and Diu",
  "Delhi",
  "Goa",
  "Gujarat",
  "Haryana",
  "Himachal Pradesh",
  "Jammu and Kashmir",
  "Jharkhand",
  "Karnataka",
  "Kerala",
  "Lakshadweep",
  "Madhya Pradesh",
  "Maharashtra",
  "Manipur",
  "Meghalaya",
  "Mizoram",
  "Nagaland",
  "Odisha",
  "Puducherry",
  "Punjab",
  "Rajasthan",
  "Sikkim",
  "Tamil Nadu",
  "Telangana",
  "Tripura",
  "Uttar Pradesh",
  "Uttarakhand",
  "West Bengal"
]

print("len of state",len(states_to_extract))
fixed_country_oid = "6715f9293065b2a277cc83aa"

with open("cities.json", "r") as f:
    cities_data = json.load(f)

current_timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

seen_states = {}
for city in cities_data:
    state = city.get("state")
    iso_code = city.get("gst-state-code")
    if state in states_to_extract and state not in seen_states:
        seen_states[state] = iso_code

documents = []
base_oid_prefix = "6715f92a3065b2a277cc83"  # 22 characters, we'll append 2 more hex digits

for idx, (state, iso_code) in enumerate(seen_states.items()):
    oid_suffix = f"{194 + idx:02x}"  # start from c2 (hex for 194)
    generated_oid = base_oid_prefix + oid_suffix

    doc = {
        "_id": {
            "$oid": generated_oid
        },
        "_country": {
            "$oid": fixed_country_oid
        },
        "name": state,
        "isoCode": iso_code,
        "createdAt": {
            "$date": current_timestamp
        },
        "updatedAt": {
            "$date": current_timestamp
        }
    }
    documents.append(doc)

with open("state.json", "w") as f:
    json.dump(documents, f, indent=4)

print(" State data with generated _id and fixed _country ObjectId saved to state.json")
