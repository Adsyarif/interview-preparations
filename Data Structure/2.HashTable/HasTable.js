class HashTable {
  constructor(size) {
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
  }

  set(key, values) {
    let address = this._hash(key);
    if (!this.data[address]) {
      this.data[address] = [];
      //   console.log(this.data);
    }
    this.data[address].push([key, values]);
    // console.log(this.data);
    return this.data;
  }

  get(key) {
    let address = this._hash(key);
    const currentBucket = this.data[address];
    if (currentBucket) {
      for (let i = 0; i < currentBucket.length - 1; i++) {
        if (currentBucket[i][0] === key) {
          return currentBucket[i][1];
        }
      }
    }
    return undefined;
  }

  keys() {
    const keysArray = [];
    for (let i = 0; i < this.data.length - 1; i++) {
      if (this.data[i]) {
        // console.log(this.data[i]);
        keysArray.push(this.data[i][0][0]);
      }
    }
    // console.log(keysArray);
    return keysArray;
  }
}

const myHashTable = new HashTable(50);
myHashTable.set("grapes", 10000);
myHashTable.get("grapes");
myHashTable.set("apples", 9);
myHashTable.get("apples");
console.log(myHashTable.keys());

myHashTable.data;
