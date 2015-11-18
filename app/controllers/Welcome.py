"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')


    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        return self.load_view('index.html') #note is an array of notes hopefully.
    def index_notes(self):
        notes = self.models['WelcomeModel'].index()
        return self.load_view('partials/notes_index.html', notes = notes)

    def create(self):
        print request.form
        self.models['WelcomeModel'].create(request.form)
        return "I posted something"

    def update(self, id):
        print request.form
        self.models['WelcomeModel'].update(request.form, id)
        return "I will update something"

    def delete(self, id):
        self.models['WelcomeModel'].delete(id)
        return "I will delete something"

    def show(self,id):
        note = self.models['WelcomeModel'].show(id) #list of length 1
        return self.load_view('partials/notes_show.html', note = note[0])
