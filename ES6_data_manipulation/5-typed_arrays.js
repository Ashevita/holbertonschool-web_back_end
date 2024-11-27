export default function createInt8TypedArray(length, position, value) {
  // Créer un nouvel ArrayBuffer de taille `length`
  const buffer = new ArrayBuffer(length);

  // Créer une vue DataView pour manipuler le buffer
  const view = new DataView(buffer);

  // Vérifier si la position est valide
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Insérer la valeur à la position donnée
  view.setInt8(position, value);

  return view;
}
