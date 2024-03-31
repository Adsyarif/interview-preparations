// let myLinkedList = {
//   head: {
//     value: 10,
//     next: {
//       value: 5,
//       next: {
//         value: 10,
//         next: null,
//       },
//     },
//   },
// };

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    this.tail = this.head;
    this.length = 1;
  }

  append(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      // console.log(currentNode);
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }

  insert(index, value) {
    const newNode = {
      value: value,
      next: null,
    };

    if (index === 0) {
      this.prepend(value);
      return this.printList();
    }

    if (index >= this.length) {
      return this.append(value);
    }

    const leader = this.traverseToIndex(index - 1);
    const holdingPointer = leader.next;
    leader.next = newNode;
    newNode.next = holdingPointer;
    this.length++;
    return this.printList();
  }

  traverseToIndex(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  remove(index) {
    const leader = this.traverseToIndex(index - 1);
    const unwantedNode = leader.next;
    leader.next = unwantedNode.next;
    this.length--;
    return this.printList();
  }

  reverse() {
    if (!this.head.next) {
      return this.head;
    }

    let first = this.head;
    this.tail = this.head;
    let second = first.next;
    while (second) {
      const _ = second.next;
      second.next = first;
      first = second;
      second = _;
    }
    this.head.next = null;
    this.head = first;
    return this.printList();
  }
}

const myLinkedList = new LinkedList(10);
// console.log(myLinkedList);
myLinkedList.append(5);
// console.log(myLinkedList);
myLinkedList.append(16);
myLinkedList.remove(1);
console.log(myLinkedList.printList());
// myLinkedList.printList();

// console.log(myLinkedList);
// console.log(myLinkedList.prepend(2));
// console.log(myLinkedList.insert(1, 101));
