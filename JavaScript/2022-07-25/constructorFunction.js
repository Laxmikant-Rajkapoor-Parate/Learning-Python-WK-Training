function fun(n, g, a) {
  this.name = n;
  this.gender = g;
  this.age = a;

  this.birthYear = function () {
    console.log(2022 - this.age);
  };
}

let obj1 = new fun("Ajay", "M", 26);
console.log(obj1);
console.log(obj1.__proto__);
console.log(fun.__proto__);

obj1.birthYear();
