export default function guardrail(mathFunction) {
  const queue = [];
  
  try {
    const result = mathFunction();
    queue.push(result); // Ajouter le résultat de la fonction
  } catch (error) {
    queue.push(`Error: ${error.message}`); // Ajouter le message d'erreur en cas d'exception
  } finally {
    queue.push('Guardrail was processed'); // Ajouter ce message dans tous les cas
  }

  return queue;
}
