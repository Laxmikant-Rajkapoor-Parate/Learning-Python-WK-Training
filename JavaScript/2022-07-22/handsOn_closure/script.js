const heading = document.querySelector("h1");
const toogleButton = document.querySelector("button");

(() => {
  heading.classList.add("blue");
  toogleButton.addEventListener("click", () => {
    heading.classList.toggle("blue");
    heading.classList.toggle("green");
  });
})();
