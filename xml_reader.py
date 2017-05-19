from xml.dom import minidom


class Field(object):
	def __init__(self, attribute_name):
		self.attribute_name = attribute_name


class Base(object):
	"""
	Clase base de XML.
	"""
	def __init__(self, path=None):
		self.doc = minidom.parse(path)

	def get_elements(self, node):
		return self.doc.getElementsByTagName(node)

	def get_attributes(self, node, fields):
		data = {}
		# Recorrer lista de atributos
		for name in fields:
			# Extraer datos con los nombres.
			for item in node:
				atribute = item.getAttribute(name)
			# Agregar a la lista 
			data.update({name: atribute})
		return data


class XmlReader(Base):
	"""
	Clase para la lectura de XML
	"""

	def __init__(self, **kwargs):
		super(XmlReader, self).__init__(**kwargs)

	def get_fields(self):
		fields = []

		for field in self.map_fields:
			name = getattr(field, 'attribute_name')
			fields.append(name)

		return fields

	def get_data(self):
		fields = self.get_fields()
		node = self.get_elements(self.node)

		_data = self.get_attributes(node, fields)
		return _data

		
class Comprobante(XmlReader):
	"""
	Nodo de comprobante
	"""

	node = 'cfdi:Comprobante'

	map_fields = (
		Field(attribute_name='serie'),
		Field(attribute_name='folio'),
	)



path = 'CFDI_v12.xml'
comprobante = Comprobante(path=path)
data = comprobante.get_data()

print(data)