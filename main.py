import json
import graphene
import os


class Query(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()

    def resolve_name(root, info):
        return "Meekasan"
    
    def resolve_age(root, info):
        return "34"
    

schema = graphene.Schema(query=Query)
print(schema)

# query

test_query = """
query myquery {
    name
    
}
"""

result = schema.execute(test_query)
print(json.dumps(result.data, indent=3))