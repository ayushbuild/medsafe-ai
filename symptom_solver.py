def symptom_advice(symptom):

    symptom = symptom.lower()

    if "fever" in symptom:
        return "Drink fluids, rest, and monitor temperature."

    if "headache" in symptom:
        return "Stay hydrated, avoid screen time, try relaxation."

    if "cough" in symptom:
        return "Warm fluids, honey, and steam inhalation may help."

    return "Monitor symptoms and consult a doctor if it persists."