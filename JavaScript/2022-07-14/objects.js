const student = {
  name: "Laxmikant",
  gender: "Male",
  //   greet: () => {
  //     console.log("This is greet function");
  //   },
};

console.log(student.name);
console.log(student["gender"]);

student.greet = () => {
  console.log("This is greet from outside");
};

student.greet();

// console.log(student);
console.table(student);
