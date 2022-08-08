// invoking functions hand in hand
(function (a, b) {
  console.log(a + b);
})(1, 2);

((a, b) => {
  console.log(a + b);
})(10, 20);

// console.log();
