def validate_dict(rules, data):
    ok=True
    for key, prefix, middle, suffix in rules:
        if key in data:
            value = data[key]
            if not (value.startswith(prefix) and value.endswith(suffix) and middle in value[1:-1]):
                ok= False
        else: ok= False
    return ok



def main():
    rules = {
        ("name", "Mr", "John", "Doe"),
        ("email", "user@", "example", ".com"),
    }

    data = {
        "name": "MrJohnDoe",
        "email": "user@example.com",
    }

    result = validate_dict(rules, data)
    print(result)


main()
