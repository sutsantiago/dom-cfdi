from xml.dom import minidom


class Base(object):
	"""docstring for Base"""


class XmlReader(object):

	def __init__(self, path=None):
		self.doc = minidom.parse(path)

	def get_data(self):
		data = {}
		return data
		
		
class Field(object):
	def __init__(self, attribute_name):
		self.attribute_name = attribute_name


class Compronate(object):
	"""
	Nodo de comprobante
	"""
	node = 'cfdi:Comprobante'

	map_fields = (
		Field(attribute_name='serie'),
		Field(attribute_name='folio'),
	)



path = 'CFDI_v12.xml'
data =  XmlReader(path=path).get_data()
print(data)