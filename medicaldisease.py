def search(patients, disease):
    found_patients = []  
    for patient in patients:
        if patient["Disease"] == disease:
            found_patients.append(patient["Name"])  
    return found_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
patients_with_disease = search(patients, search_disease)
print(f"Patients with {search_disease}: {patients_with_disease}")