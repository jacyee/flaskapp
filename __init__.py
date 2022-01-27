from flask import Flask, jsonify
import os

def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config = True)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        #load instance config if exits when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    @app.route('/')
    def hello():
        return jsonify({'message':'helloworld'})
    
    @app.route('/pet')
    def pet():
        return jsonify({'pet':'mugi'})
    
    return app
