// Définition de la classe Car
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Méthode de clonage
  cloneCar() {
    const NewCar = this.constructor[Symbol.species] || this.constructor;
    return new NewCar();
  }

  // Déclaration du symbole species pour permettre un clonage correct
  static get [Symbol.species]() {
    return this;
  }
}
