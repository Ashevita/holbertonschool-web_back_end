import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);  // Appelle le constructeur de Building pour initialiser _sqft
    this._floors = floors;
  }

  // Getter pour _floors
  get floors() {
    return this._floors;
  }

  // Surcharge de la méthode evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
