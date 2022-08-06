let expression = "";
const screen = document.getElementById("screen");

const display = (id) => {
  if (id == "eval") {
    try {
      const result = eval(expression);
      screen.value = result;
      expression = "";
    } catch (error) {
      alert(`ERROR, ${error}`);
    }
  } else {
    expression += document.getElementById(id).value;
    screen.value = expression;
  }
};
