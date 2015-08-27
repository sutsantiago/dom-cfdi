import xml.etree.ElementTree as ET


class Base(object):

	def __init__(self, file_names=None):
		self._filename = file_names

	def tostring(self):
		try:
			tree = ET.parse(self._filename)
			root = tree.getroot()
			str_file = root.attrib
		except Exception as e:
			print("Error: "+str(e))
		finally:
			return str_file

	def list_tostring(self):
		list_files = []
		try:
			for item in self._filename:
				tree = ET.parse(item['name'])
				root = tree.getroot()
				str_file = root.attrib
				list_files.append(str_file)
		except Exception as e:
			print("Error: "+str(e))
		finally:
			return list_files


class ParseXML(Base):
	
	def __init__(self, **kwargs):
		super(ParseXML, self).__init__(**kwargs)

	@property
	def simple(self):
		return self.tostring()

	@property
	def multiple(self):
		return self.list_tostring()

file_name = 'C:/Users/TomaS/repositorio/thomgonzalez/minidom/cfdi_test.xml'
files = [
	{'name':'C:/Users/TomaS/repositorio/thomgonzalez/minidom/cfdi_test.xml'},
	{'name':'C:/Users/TomaS/repositorio/thomgonzalez/minidom/cfdi_test.xml'}
]

xml = ParseXML(file_names=file_name).simple
xmls = ParseXML(file_names=files).multiple

print(xml)
print(xmls)