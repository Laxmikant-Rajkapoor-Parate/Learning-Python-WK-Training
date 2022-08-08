// let patient = {
//   name: "Ajay",
//   gender: "M",
//   age: 25,
// };

// patient = { ...patient, newThing: "newValue", anotherThing: "anotherValue" };
// console.log(patient);

const nums = [1, 2, 3];

const fun = (a, b, c) => {
  console.log(a + b + c);
};

fun(1);
fun(1, 2);
fun(1, 2, 3);
fun(1, 2, 3, 4);
fun(...nums);
