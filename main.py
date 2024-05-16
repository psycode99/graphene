import json
import graphene
import os


class Query(graphene.ObjectType):
    name = graphene.String(value=graphene.String(default_value="Kengan Ashura"))
    age = graphene.String()

    def resolve_name(root, info, value):
        return "hello {}".format(value)
    
    def resolve_age(root, info):
        return "34"
    

schema = graphene.Schema(query=Query)
print(schema)

# query

test_query = """
query myquery {
    name (value: "Ohma Tokita")
    age
    
}
"""

result = schema.execute(test_query)
print(json.dumps(result.data, indent=3))