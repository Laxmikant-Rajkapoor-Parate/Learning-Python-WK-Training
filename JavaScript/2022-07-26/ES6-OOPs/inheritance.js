class parent {
  constructor(n, g, a) {
    this.name = n;
    this.gender = g;
    this.age = a;
  }

  birthYear() {
    console.log(2022 - this.age);
  }
}

class child extends parent {
  constructor(n, g, a, rn) {
    super(n, g, a);
    this.rollNo = rn;
  }

  display() {
    console.log(this);
  }
}

const obj = new child("Ajay", "M", 26, 8271);

obj.display();
