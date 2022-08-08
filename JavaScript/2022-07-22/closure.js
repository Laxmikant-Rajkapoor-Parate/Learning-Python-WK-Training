// nesting of functions
const parentFun = () => {
  let x = 10;
  let y = 20;

  const childFun = () => {
    ++x;
    console.log(x);
    console.log(y);
  };

  childFun();
};

parentFun();
