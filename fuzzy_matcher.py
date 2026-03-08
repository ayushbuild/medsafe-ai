from rapidfuzz import process
import json

with open("medicine_db.json") as f:
    med_db = json.load(f)

def match_medicine(name):
    match = process.extractOne(name, med_db.keys())
    if match[1] > 70:
        return match[0], med_db[match[0]]
    return None, None