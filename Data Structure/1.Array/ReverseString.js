const reverse = (str) => {
  let t0 = performance.now();
  let strArray = [];
  for (let i = 0; i < str.length; i++) {
    strArray.push(str[i]);
  }

  let reverseArr = [];
  for (let i = 0; i < str.length; i++) {
    reverseArr[i] = strArray[str.length - 1 - i];
  }

  console.log(reverseArr.join(""));
  let ti = performance.now();

  console.log(ti - t0);
};

reverse("Makan Ayam");

console.log(" ");
console.log(" ");

const reverse2 = (str) => {
  let t0 = performance.now();
  if (!str || str.length < 2 || typeof str !== "string") {
    return "Hmm thats not good";
  }

  let backward = [];
  let strLength = str.length - 1;
  for (let i = strLength; i >= 0; i--) {
    backward.push(str[i]);
  }
  console.log(backward.join(""));
  let ti = performance.now();

  console.log(ti - t0);
};

reverse2("Makan Ayam");

console.log(" ");
console.log(" ");

const reverse3 = (str) => {
  let t0 = performance.now();
  console.log(str.split("").reverse().join(""));
  let ti = performance.now();

  console.log(ti - t0);
};

reverse3("Makan Ayam");

console.log(" ");
console.log(" ");

const reverse4 = (str) => {
  let t0 = performance.now();
  console.log([...str].reverse().join(""));
  let ti = performance.now();

  console.log(ti - t0);
};

reverse4("Makan Ayam");
