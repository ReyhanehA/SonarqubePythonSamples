    #When validating XML:

parser = etree.XMLParser(resolve_entities=True) # Noncompliant
treexsd = etree.parse('ressources/xxe.xsd', parser)
rootxsd = treexsd.getroot()
schema = etree.XMLSchema(rootxsd)