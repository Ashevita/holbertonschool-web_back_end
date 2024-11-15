// 1-block-scoped.js

export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true; // utilisation de const dans le bloc conditionnel pour éviter la redéclaration globale
    const task2 = false;
  }

  return [task, task2];
}
