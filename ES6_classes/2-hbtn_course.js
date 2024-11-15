export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  get length() {
    return this._length;
  }

  set length(len) {
    if (typeof len !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = len;
    }
  }

  get students() {
    return this._students;
  }

  set students(array) {
    if (!(array instanceof Array)) {
      throw new TypeError('Students must be an array');
    }
    if (!array.every((student) => typeof student === 'string')) {
      throw new TypeError('Each student must be a string');
    }
    this._students = array;
  }
}
