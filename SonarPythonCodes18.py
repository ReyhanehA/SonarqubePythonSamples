parser = etree.XMLParser() # Noncompliant: by default resolve_entities is set to true
tree1 = etree.parse('ressources/xxe.xml', parser)
root1 = tree1.getroot()

parser = etree.XMLParser(resolve_entities=True) # Noncompliant
tree1 = etree.parse('ressources/xxe.xml', parser)
root1 = tree1.getroot()
-------------------------------------------------

    When validating XML:

parser = etree.XMLParser(resolve_entities=True) # Noncompliant
treexsd = etree.parse('ressources/xxe.xsd', parser)
rootxsd = treexsd.getroot()
schema = etree.XMLSchema(rootxsd)
-------------------------------------------------

    When transforming XML:

ac = etree.XSLTAccessControl(read_network=True, write_network=False)  # Noncompliant, read_network is set to true/network access is authorized
transform = etree.XSLT(rootxsl, access_control=ac)
-------------------------------------------------
xml.sax module:

parser = xml.sax.make_parser()
myHandler = MyHandler()
parser.setContentHandler(myHandler)

parser.setFeature(feature_external_ges, True) # Noncompliant
parser.parse("ressources/xxe.xml")
