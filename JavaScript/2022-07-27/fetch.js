// let country = "india";
// const data = fetch(`https://restcountries.com/v3.1/name/${country}`);

// console.log(data);

async function getData(country) {
  const data = await fetch(`https://restcountries.com/v3.1/name/${country}`);
  console.log(data);
}

getData("india");
