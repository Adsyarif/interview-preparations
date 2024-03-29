const recurring = (arr) => {
  let checkArr = [];
  let arrElement = arr.length;

  for (i = 0; i < arrElement; i++) {
    // console.log(i);
    if (!checkArr.includes(arr[i])) {
      checkArr.push(arr[i]);
    } else {
      return arr[i];
    }
  }
  return undefined;
}; //O(n^2)

input1 = recurring([0, 1, 1, 0, 5, 9, 5]);
console.log(input1);

const recurring2 = (arr) => {
  let map = {};
  for (let i = 0; i < arr.length; i++) {
    if (map[arr[i]] !== undefined) {
      return arr[i];
    } else {
      map[arr[i]] = i;
    }
  }
  return undefined;
}; //O(n)

input2 = recurring2([0, 1, 1, 0, 5, 9, 5]);
console.log(input2);
