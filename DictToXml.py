def create_tag(tag):
    """Creates an xml tag shell

    Args:
        tag: xml tag to be created

    Returns:
        An empty xml tag shell with a placeholder value in the body
    """
    xmltag = '<_tag_>_xml_</_tag_>'
    return xmltag.replace('_tag_', tag)


def insert_content(tag, content):
    """Inserts content into the body of an xml tag shell

    Args:
        tag: an empty xml tag shell, can be string or list of strings
        content: content to insert into shell, can be string or list of strings

    Returns:
        Return xml tag(s) with content replacing placeholders
    """
    if not isinstance(tag, list):
        return tag.replace('_xml_', content)
    else:
        compound = ''
        for x in range(0, len(tag)):
            compound += tag[x].replace('_xml_', content[x])
        return compound


def dict_to_xml(obj):
    """Converts python dictionary to an xml string

    Args:
        obj: A python dictionary

    Returns:
        An xml string representation of the passed dictionary
    """
    for key, value in obj.iteritems():
        xml = create_tag(key)
        if key is 'rpc':
            xml = xml.replace('<rpc>', '<rpc semp-version="' + version + '">')
        if isinstance(value, list):
            concat = ""
            for object in value:
                concat += dict_to_xml(object)
            xml = insert_content(xml, concat)
            return xml
        else:
            if isinstance(value, dict):
                xml = insert_content(xml, dict_to_xml(value))
                return xml
            else:
                xml = insert_content(xml, value)
                return xml
