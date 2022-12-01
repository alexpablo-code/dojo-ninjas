from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s,NOW(),NOW())"
        return connectToMySQL('dojo_and_ninjas').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL('dojo_and_ninjas').query_db(query)
        ninjas =[]
        for b in ninjas_from_db:
            ninjas.append(cls(b))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL('dojo_and_ninjas').query_db(query,data)
        ninja = cls(ninja_from_db[0])
        print(ninja)
        return ninja

    @classmethod
    def get_one_with_dojo(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;"
        results = connectToMySQL('dojo_and_ninjas').query_db(query,data)
        ninja = cls(results[0])
        print("__this is the NINJA w DOJO___", ninja)
        print("__THIS RESULTS__", results)

        for i in results:
            ninja.dojo = dojo.Dojo ({
                "id": i["dojos.id"],
                "name": i["name"],
                "created_at": i["dojos.created_at"],
                "updated_at": i["dojos.updated_at"]
            })

            
        return ninja

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojo_and_ninjas').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojo_and_ninjas').query_db(query,data)