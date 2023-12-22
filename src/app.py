from flask import Flask
# misma ruta importo el dict config 
from config import config
# habilitar los CORS y consumir sta pi desde otras rutas react / angular / vte 
from flask_cors import CORS

# Routes
from routes import Movie

app = Flask(__name__)

# habilito el acces desde el puerto 3000
CORS(app, resources={"*": {"origin": "http://localhost:3000"}})

# para las paginas noencotradas
def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    # en app la configuracion va a venir desde un objeto el dict config y su llave development
    # ordenamos la condig y el proyecto arranca de mejor manera
    app.config.from_object(config['development'])
    
    # Blueprints, el url_prefix sirve para indicar cuál será la ruta raiz
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
        
    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run()