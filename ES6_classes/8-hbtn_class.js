export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Méthode de conversion en Number
  valueOf() {
    return this._size;
  }

  // Méthode de conversion en String
  toString() {
    return this._location;
  }
}
