from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja 

class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the burgers that are associated with a restaurant.
        self.ninjas = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojo_and_ninjas').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('dojo_and_ninjas').query_db(query)
        dojos =[]
        for one_dojo in dojos_from_db:
            dojos.append(cls(one_dojo))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id =%(id)s"
        results = connectToMySQL('dojo_and_ninjas').query_db(query, data)
        # results will be a list of topping objects with the ninja attached to each row.
        print("this is results",results)
        dojo = cls(results[0])
        for row_from_db in results:
            # Now we parse in the ninja data to make instance of ninjas and add them into our list.

            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(ninja_data))
        print("___THIS IS THE DOJO VAR___", dojo)
        return dojo 