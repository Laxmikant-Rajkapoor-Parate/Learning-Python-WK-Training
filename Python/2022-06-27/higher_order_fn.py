from functools import reduce

def get_year(date):
    return int(date.split('-')[2])

def get_yob(patient_dob):
    yob = list(map(get_year, patient_dob))
    return yob

def get_age(yob):
    age = list(map(lambda age: 2022 - age, yob))
    return age

if __name__ == '__main__':
    patient_dob = ['13-06-1993', '04-10-2001', '26-09-2004', '30-01-2010']
    yob = get_yob(patient_dob)
    ages = get_age(yob)

    eligible_to_vote = list(filter(lambda age: age >= 18, ages))

    print("Eligible to vote are:")
    print(eligible_to_vote)

    sum_age = reduce(lambda age1, age2: age1 + age2, ages)
    print("Average age: " + str(sum_age / len(ages)))
