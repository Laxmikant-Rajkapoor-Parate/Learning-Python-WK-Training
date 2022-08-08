// displays the patient object
const patient1 = {
  name: "Ajay",
  gender: "M",
  age: 26,

  display: function () {
    console.log(this);
  },
};

// displays empty object
const patient2 = {
  name: "Ajay",
  gender: "M",
  age: 26,

  display: () => {
    console.log(this);
  },
};

// patient1.display();
// patient2.display();

// const copy = patient1;
const copy = patient2;
copy.display();
