# def yield_one_by_one(arr):
#     for num in arr:
#         yield num

# arr = [1,2,3,4,5]

# for itr in yield_one_by_one(arr):
#     print(itr)

import json

def load_patient():
    with open(r'Python\data\data.json', 'r') as fp:
        data = json.load(fp)
        for patient in data['patient_list']:
            yield patient

for patient in load_patient():
    print(patient)
    print()