import json

with open("interaction_db.json") as f:
    interactions = json.load(f)


def check_interactions(meds):

    results = []

    for i in range(len(meds)):
        for j in range(i + 1, len(meds)):

            pair1 = f"{meds[i]} + {meds[j]}"
            pair2 = f"{meds[j]} + {meds[i]}"

            if pair1 in interactions:
                results.append((pair1, interactions[pair1]))

            elif pair2 in interactions:
                results.append((pair2, interactions[pair2]))

    return results
