"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def show(self,id):
        query = "SELECT * FROM notes where id  = {}".format(id)
        return self.db.query_db(query)

    def create(self, note):
        query = "INSERT INTO notes (title, description, created_at, updated_at) values ('{}', '{}', now(),now())".format(note['title'], note['description'])
        self.db.query_db(query)
        return "inserted"

    def index(self):
        query = "SELECT * FROM notes"
        return self.db.query_db(query);

    def delete(self,id):
        query = 'DELETE from notes where id = {}'.format(id)
        self.db.query_db(query);
        return 'I should delete somethign (model)'

    def update(self,note, id):
        query = "UPDATE notes set title = '{}', description = '{}', updated_at = now() where id = {}".format(note['title'], note['description'],id)
        self.db.query_db(query)
        return 'if something broke we could use this to determine if the function ran'
