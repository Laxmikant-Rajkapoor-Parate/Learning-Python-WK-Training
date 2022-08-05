var x = 10;

function changeX() {
  x = 20;
  const y = 30;
}

changeX();
console.log(x);
console.log(y); // throw Error
