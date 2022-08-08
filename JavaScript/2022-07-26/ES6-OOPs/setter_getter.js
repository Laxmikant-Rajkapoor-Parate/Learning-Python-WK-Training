class patient {
  #age;
  constructor(n, g, a) {
    this.name = n;
    this.gender = g;
  }

  birthYear() {
    console.log(2022 - this.age);
  }

  set patientAge(a) {
    this.#age = a;
  }

  get getAge() {
    return this.#age;
  }
}

const obj = new patient("Ajay", "M", 26);

// gives error
// patient.age = 10;

obj.patientAge = 40;

console.log(obj);
console.log(obj.getAge);
