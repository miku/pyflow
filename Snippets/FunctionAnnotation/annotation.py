
def hello(greeting: "greeting word", name: "custom name") -> "result":
    return f"{greeting} from {name}"

print(hello("hello", "world"))
print(hello.__annotations__)

# hello from world
# {'greeting': 'greeting word', 'name': 'custom name', 'return': 'result'}
