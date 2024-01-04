import json
from pydantic import BaseModel, create_model

# Read JSON file
with open('sample.json', 'r') as file:
    data = json.load(file)

# Function to convert JSON schema to Pydantic model
def generate_pydantic_model(class_name, schema):
    properties = {}
    for prop_name, prop_schema in schema['properties'].items():
        prop_type = prop_schema['type']
        if prop_type == 'string':
            properties[prop_name] = (str, ...)
        elif prop_type == 'integer':
            properties[prop_name] = (int, ...)
        # Extend this logic for other types as needed

    pydantic_model = create_model(class_name, **properties)
    print(pydantic_model)
    return pydantic_model

# Create Pydantic models from JSON
generated_models = {}
for class_name, schema in data.items():
    print(schema)
    model = generate_pydantic_model(class_name, schema)
    generated_models[class_name] = model

# Now you have Pydantic classes generated from the JSON definitions
# Access them like generated_models['Person']
