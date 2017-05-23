from xml.dom import minidom


class XmlReader(object):
	"""
	Clase base de XML.
	"""

	def __init__(self, path=None):
		self.document = minidom.parse(path)

	def get_file(self):
		return self.document

	def get_elements(self, node_xml):
		return self.document.getElementsByTagName(node_xml)

	def get_attribute(self, node, field=None):
		"""
		Retorna un atributo en especifico.
		"""
		data = {}
		atribute = node[0].getAttribute(field)
		data[field] = atribute
		return data

	def get_list_attributes(self, nodes, fields=[]):
		"""
		Retorna lista de atributos.
		"""
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

	def get_dict_attributes(self, node, fields=[]):
		"""
		Retorna diccionario de atributos.
		"""
		data = {}
		# Recorrer lista de atributos.
		for name in fields:
			# Extraer datos del nodo.
			atribute = node[0].getAttribute(name)
			# Actualizar diccionario.
			data.update({name: atribute})
		return data
