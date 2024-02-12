from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

metadata = {
    "type": "object",
    "description": "Recipe metadata",
    "properties": {
        "title": {
            "type": "string",
            "description": "Recipe title",
        },
    }
},

ingredients = {
    "type": "array",
    "description": "A list of logical groups, each containing a list of ingredients",
    "items": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Group title",
                },
                "ingredients": {
                    "type": "array",
                    "description": "Ingredient list",
                    "items": {
                        "type": "string",
                        "description": "individual ingredient with measurements"
                    },
                }
            }
    },
}

instructions = {
    "type": "array",
    "description": "An ordered list of instructions for a recipe",
    "items": {
            "type": "string",
            "description": "An individual step of the recipe"
    },
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "format_recipe",
            "description": "Consolidate a recipe into a clear format",
            "parameters": {
                "type": "object",
                "properties": {
                    # "metadata": metadata,
                    "ingredients": ingredients,
                    "instructions": instructions
                }
            },
        }
    }
]

prompt = """
Consolidate and organize this recipe, based on the following information:
- Provide metadata for the recipe.
- Provide a list of ingredients with measurements in grams
- Provide a numbered set of instructions for the recipe itself.
    Keep this short and brief, but do not omit crucial information.

You can only reply with the function format_recipe.
"""

f = open("recipe.txt", "r")
content = f.read()
    

messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": content}
    ]

completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=messages,
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "format_recipe"}}
)

print(completion)
