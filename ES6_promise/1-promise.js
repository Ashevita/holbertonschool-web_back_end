export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      // Résoudre avec un objet contenant les attributs demandés
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      // Rejeter avec une erreur contenant le message spécifié
      reject(new Error('The fake API is not working currently'));
    }
  });
}
