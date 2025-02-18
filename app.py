# importer les dépendances de Flask
from flask import Flask, request, make_response, jsonify

# initialiser l'application Flask
app = Flask(__name__)

# route par défaut
@app.route('/')
def index():
    return 'Hello World'

# fonction pour les réponses
def results():
    # construire un objet de requête
    req = request.get_json(force=True)

    # extraire l'action du JSON
    action = req.get('queryResult').get('action')

    # retourner une réponse de fulfillment
    return {'fulfillmentText': 'Ceci est une réponse de webhook'}

# créer une route pour le webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # retourner la réponse
    return make_response(jsonify(results()))
# exécuter l'application
if __name__ == '__main__':
    app.run()