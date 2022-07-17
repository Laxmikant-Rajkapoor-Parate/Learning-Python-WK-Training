import json

def load_patient_data():
    with open(r'Python\data\data.json', 'r') as json_file_handler:
        data = json.load(json_file_handler)
    return data

def update_data(id, name, patient_data):
    for patient in patient_data['patient_list']:
        if patient['patient_id'] == id:
            patient['firstname'] = name
    
def save_data(patient_data):
    with open(r'Python\data\data.json', 'w') as json_file_handler:
        json.dump(patient_data, json_file_handler, indent=2)

if __name__ == '__main__':
    patient_data = load_patient_data()

    update_data(2, "Sita", patient_data)
    save_data(patient_data)
