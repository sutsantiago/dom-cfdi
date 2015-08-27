import xml.etree.ElementTree as ET


class Base(object):

	def __init__(self):
		self._filename = self.file_name

	def tostring(self):
		tree = ET.parse(self._filename)
		root = tree.getroot()
		str_file = root.attrib
		return str_file

	def list_tostring(self):
		return None


class ParseXML(Base):
	file_name = 'C:/Users/TomaS/repositorio/thomgonzalez/minidom/cfdi_test.xml'

	@property
	def simple(self):
		return self.tostring()

	@property
	def multiple(self):
		return self.list_tostring()


xml = ParseXML().simple
print(xml)
		