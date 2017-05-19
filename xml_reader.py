from xml.dom import minidom


class Field(object):
	def __init__(self, attribute_name):
		self.attribute_name = attribute_name


class Base(object):

	def get_fields(self):
		fields = []

		for field in self.map_fields:
			name = getattr(field, 'attribute_name')
			fields.append(name)

		return fields

	def get_node(self):
		return self.node
		

class XmlReader(object):
	"""
	Clase base de XML.
	"""

	def __init__(self, path=None):
		self.document = minidom.parse(path)

	def get_file(self):
		return self.document

	def get_elements(self, document):
		return document.getElementsByTagName(node)

	def get_attributes(self, node_xml, fields):
		node = self.get_elements(node_xml)

		data = {}
		# Recorrer lista de atributos
		for name in fields:
			# Extraer datos con los nombres.
			for item in node:
				atribute = item.getAttribute(name)
			# Agregar a la lista 
			data.update({name: atribute})
		return data

	def list_attributes(self, node_xml, fields):
		nodes = self.get_elements(node_xml)
		
		data = []
		dic = {}
		# Extraer datos del nodo.
		for node in nodes:
			# Recorrer lista de atributos.
			for name in fields:
				atribute = node.getAttribute(name)
				# Actualizar diccionario.
				dic.update({name: atribute})
			# Agregar a la lista los diccionarios.
			data.append(dic)
		return data


class Comprobante(Base):
	"""
	Nodo de comprobante
	"""

	node = 'cfdi:Comprobante'

	map_fields = (
		Field(attribute_name='version'),
		Field(attribute_name='tipoDeComprobante'),
		Field(attribute_name='fecha'),
		Field(attribute_name='serie'),
		Field(attribute_name='folio'),
		Field(attribute_name='sello'),
		Field(attribute_name='noCertificado'),
		Field(attribute_name='certificado'),
		Field(attribute_name='metodoDePago'),
		Field(attribute_name='fomaDePago'),
		Field(attribute_name='subTotal'),
		Field(attribute_name='descuento'),
		Field(attribute_name='total'),
		Field(attribute_name='TipoCambio'),
		Field(attribute_name='Moneda'),
		Field(attribute_name='LugarExpedicion')
	)


class Percepcion(Base):
	"""docstring for ClassName"""
	node = 'nomina12:Percepcion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoPercepcion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='ImporteGravado'),
		Field(attribute_name='ImporteExento'),
	)


class Deduccion(Base):
	"""docstring for ClassName"""
	node = 'nomina12:Deduccion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoDeduccion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='Importe'),
	)


class ParseXml(object):

	path = 'CFDI_v12.xml'

	xml_reader = XmlReader(path=path)
	file = xml_reader.get_file()
	print(file)

	comprobante = Comprobante()
	node = comprobante.get_node()
	fields = comprobante.get_fields()

	print(node, fields)
