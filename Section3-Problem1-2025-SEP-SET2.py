def is_hypertensive(patient: dict) -> bool:
    """Returns True if the patient has high blood pressure (>= 140), else False."""
    
    
    return patient["blood_pressure"] >= 140
    


def is_tachycardic(patient: dict) -> bool:
    """Returns True if the patient has a high heart rate (> 100), else False."""
    
    
    return patient["heart_rate"] > 100
    


def patients_with_risk(patients: list) -> list:
    """Returns list of patient IDs who are hypertensive or tachycardic."""
    
    
    return [p["p_id"] for p in patients if is_hypertensive(p) or is_tachycardic(p)]
    


def average_age_with_risk(patients: list) -> float:
    """Returns the average age of all patients with risk (rounded to 2 decimals)."""
    
    
    risky = [p["age"] for p in patients if is_hypertensive(p) or is_tachycardic(p)]
    return round(sum(risky) / len(risky), 2) if risky else 0
    


def categorize_patient(patients: list) -> dict:
    """Categorizes patients into four groups based on health condition."""
    
    
    categories = {
        "normal": set(),
        "only_hypertensive": set(),
        "only_tachycardic": set(),
        "hypertensive_and_tachycardic": set()
    }
    for p in patients:
        hyper = is_hypertensive(p)
        tachy = is_tachycardic(p)
        if hyper and tachy:
            categories["hypertensive_and_tachycardic"].add(p["p_id"])
        elif hyper:
            categories["only_hypertensive"].add(p["p_id"])
        elif tachy:
            categories["only_tachycardic"].add(p["p_id"])
        else:
            categories["normal"].add(p["p_id"])
    return categories
    

# Hospital Patient Analytics
# You are given a list of dictionaries, where each dictionary represents a patient in a hospital. Each patient dictionary contains the following fields:

# "p_id": Patient ID (string)
# "age": Age of the patient (integer)
# "blood_pressure": Patient's blood pressure reading (integer)
# "heart_rate": Patient's heart rate (integer)
# Your task is to implement the following functions:

# Function 1: is_hypertensive(patient)
# Input: A single patient dictionary
# Output: Returns True if the patient has high blood pressure (blood_pressure >= 140), else False.

# Function 2: is_tachycardic(patient)
# Input: A single patient dictionary
# Output: Returns True if the patient has a high heart rate (heart_rate > 100), else False.

# Function 3: patients_with_risk(patients)
# Input: List of patient dictionaries
# Output: Returns a list of patient IDs who are either hypertensive or tachycardic (or both).

# Function 4: average_age_with_risk(patients)
# Input: List of patient dictionaries
# Output: Returns the average age of all patients with risk, rounded to 2 decimal places. If no patients have risk, return 0.

# Function 5: categorize_patient(patients)
# Input: List of patient dictionaries
# Output: Returns a dictionary categorizing patients into:

# "normal"
# "only_hypertensive"
# "only_tachycardic"
# "hypertensive_and_tachycardic"
# Each key should map to a set of patient IDs.

# Example
# Input:

# patients = [
#     {"p_id": "P1", "age": 45, "blood_pressure": 150, "heart_rate": 95},
#     {"p_id": "P2", "age": 52, "blood_pressure": 120, "heart_rate": 110},
#     {"p_id": "P3", "age": 30, "blood_pressure": 135, "heart_rate": 85}
# ]
# Output:

# is_hypertensive(patients[0]) -> True  
# is_tachycardic(patients[1]) -> True  
# patients_with_risk(patients) -> ['P1', 'P2']  
# average_age_with_risk(patients) -> 48.5  
# categorize_patient(patients) -> {
#     "normal": {"P3"},
#     "only_hypertensive": {"P1"},
#     "only_tachycardic": {"P2"},
#     "hypertensive_and_tachycardic": set()
# }



