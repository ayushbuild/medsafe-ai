def risk_score(symptoms):

    symptoms = symptoms.lower()

    if "chest pain" in symptoms:
        return "HIGH RISK: Seek medical help immediately"

    if "breathing difficulty" in symptoms:
        return "HIGH RISK: Emergency care required"

    if "fever" in symptoms:
        return "LOW RISK: Monitor temperature"

    return "UNKNOWN RISK: Consult doctor if symptoms persist"