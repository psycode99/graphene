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



    

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(Person)


    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)
    

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    # for List
    # array = graphene.List(Person, size=graphene.Int(default_value=1))


    # def resolve_array(root, info, size):
    #     return DATA[:size]
    
    

schema = graphene.Schema(query=Query, mutation=MyMutation)
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