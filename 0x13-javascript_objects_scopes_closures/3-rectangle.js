#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const row = 'X'.repeat(this.width);
    for (let k = 0; k < this.height; k++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
