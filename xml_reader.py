from xml.dom import minidom


class Field(object):
	def __init__(self, attribute_name):
		self.attribute_name = attribute_name


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

	def get_attributes(self, nodes, fields):
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


class Base(object):

	def get_fields(self):
		fields = []

		for field in self.map_fields:
			name = getattr(field, 'attribute_name')
			fields.append(name)

		return fields


class Comprobante(Base):
	"""
	Nodo de comprobante
	"""
	node_xml = 'cfdi:Comprobante'

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

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data


class Emisor(Base):
	"""
	Nodo Emisor
	"""
	node_xml = 'cfdi:Emisor' 

	map_fields = (
		Field(attribute_name='rfc'),
		Field(attribute_name='nombre'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def get_regimen_fiscal(self):
		data = {}
		regimen_node = self.document.get_elements('cfdi:RegimenFiscal')
		regimen = regimen_node[0].getAttribute('Regimen')
		data['Regimen'] = regimen
		return data

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data
	

class Receptor(Base):
	"""
	Nodo Emisor
	"""
	node_xml = 'cfdi:Receptor'

	map_fields = (
		Field(attribute_name='rfc'),
		Field(attribute_name='nombre'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data


class Concepto(Base):
	"""
	Nodo Emisor
	"""
	node_xml = 'cfdi:Concepto'

	map_fields = (
		Field(attribute_name='valorUnitario'),
		Field(attribute_name='unidad'),
		Field(attribute_name='cantidad'),
		Field(attribute_name='descripcion'),
		Field(attribute_name='importe'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data
		

class Nomina(Base):
	"""
	Nodo de Nomina
	"""
	node_xml = 'nomina12:Nomina'

	map_fields = (
		Field(attribute_name='Version'),
		Field(attribute_name='TotalPercepciones'),
		Field(attribute_name='TotalOtrosPagos'),
		Field(attribute_name='TotalDeducciones'),
		Field(attribute_name='TipoNomina'),
		Field(attribute_name='NumDiasPagados'),
		Field(attribute_name='FechaPago'),
		Field(attribute_name='FechaInicialPago'),
		Field(attribute_name='FechaFinalPago'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data


class NominaEmisor(Base):
	"""
	Nodo de Nomina Emisor
	"""
	node_xml = 'nomina12:Emisor'

	map_fields = (
		Field(attribute_name='RfcPatronOrigen'),
		Field(attribute_name='RegistroPatronal'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data


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

	document = XmlReader(path=path)

	comprobante = Comprobante(document=document).data()
	emisor = Emisor(document=document).data()
	receptor = Receptor(document=document).data()
	concepto =  Concepto(document=document).data()
	nomina = Nomina(document=document).data()
	nomina_emisor =  NominaEmisor(document=document).data()
	print(
	comprobante,
	emisor,
	receptor,
	concepto, 
	nomina,
	nomina_emisor)
