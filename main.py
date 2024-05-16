import json
import graphene
import os


DATA = [
    {
        "name": "Sekibayashi",
        "age": "34"
    }, 

    {
        "name": "Adam Dudley",
        "age": "45"
    }
]


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()


class Query(graphene.ObjectType):
    array = graphene.List(Person, size=graphene.Int(default_value=1))


    def resolve_array(root, info, size):
        return DATA[:size]
    
    
    

schema = graphene.Schema(query=Query)
print(schema)

# query

test_query = """
query myquery {
    array (size: 2) {
        name
    }
    
}
"""

result = schema.execute(test_query)
print(json.dumps(result.data, indent=3))