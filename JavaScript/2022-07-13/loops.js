const marks = [30, 45, 67, 38, 46, 89];
var sum = 0;
var avg = 0;

for (var i = 0; i < marks.length; i++) {
  sum += marks[i];
}

avg = sum / marks.length;

console.log(sum);
console.log(avg);
