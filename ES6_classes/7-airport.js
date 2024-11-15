export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Méthode toString pour renvoyer la représentation par défaut
  toString() {
    return `[object ${this._code}]`;
  }
}
