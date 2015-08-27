import xml.etree.ElementTree as ET


class Base(object):

	def __init__(self):
		self._filename = self.file_name

	def to_string(self):
		tree = ET.parse(self._filename)
		root = tree.getroot()
		str_file = root.attrib
		return str_file


class ParseXML(Base):
	file_name = 'C:/Users/TomaS/repositorio/thomgonzalez/minidom/cfdi_test.xml'

xml = ParseXML().to_string()
print(xml)
		