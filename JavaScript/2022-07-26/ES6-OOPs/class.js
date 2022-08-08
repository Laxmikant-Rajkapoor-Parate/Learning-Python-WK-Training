class patient {
  constructor(n, g, a) {
    this.name = n;
    this.gender = g;
    this.age = a;
  }

  birthYear() {
    console.log(2022 - this.age);
  }
}

const one = new patient("Ajay", "M", 26);

one.birthYear();
console.log(one.__proto__);
console.log(patient.prototype);
