export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // Getter et setter pour _code
  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = value;
  }

  // Getter et setter pour _name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Méthode displayFullCurrency
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
