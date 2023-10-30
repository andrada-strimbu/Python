def validate_dict(rules, data):
    for key, prefix, middle, suffix in rules:
        if key in data:
            value = data[key]
            if not (value.startswith(prefix) and value.endswith(suffix) and middle in value[1:-1]):
                return False
        else:
            return False
    return True


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
