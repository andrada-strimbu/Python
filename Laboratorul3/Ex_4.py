def build_xml_element(tag, content, **attributes):
    attribute_str = ' '.join([f'{key}="{value}"' for key, value in attributes.items()])
    xml_element = f"<{tag} {attribute_str}>{content}</{tag}>"
    return xml_element


def main():
    xml_string = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(xml_string)


main()
