import sys, os
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../lib/')

from flask import Flask, session, current_app

from .user_pages import user_pages


from pymongo import MongoClient



def create_app():
    flaskapp = Flask("app-web")

    flaskapp.register_blueprint(user_pages)

    return flaskapp



app = create_app()
