const screen = document.getElementById("screen");
const origional = document.getElementById("origional");
const unique = document.getElementById("unique");
let patientList = [];

const handleChange = () => {
  patientList = [...patientList, screen.value];
  origional.innerText = patientList;
  const s = new Set(patientList);
  x = Array.from(s);
  unique.innerText = x;
};
