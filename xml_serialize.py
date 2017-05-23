from xml_reader import XmlReader


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

class Comprobante(Base):
	"""
	Nodo de comprobante
	"""
	NODE_XML = 'cfdi:Comprobante'

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
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class Emisor(Base):
	"""
	Nodo Emisor
	"""
	NODE_XML = 'cfdi:Emisor' 

	map_fields = (
		Field(attribute_name='rfc'),
		Field(attribute_name='nombre'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	def get_regimen_fiscal(self):
		regfis_node = self.document.get_elements('cfdi:RegimenFiscal')
		reg_fiscal = self.document.get_attribute(regfis_node, 'Regimen')
		return reg_fiscal

	@property
	def data(self):
		regimen = self.get_regimen_fiscal()
		data = self.document.get_dict_attributes(self.node, self.fields)
		# Agrega regimen Fiscal
		data['regimen_fiscal'] = regimen
		return data
	

class Receptor(Base):
	"""
	Nodo Emisor
	"""
	NODE_XML = 'cfdi:Receptor'

	map_fields = (
		Field(attribute_name='rfc'),
		Field(attribute_name='nombre'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class Concepto(Base):
	"""
	Nodo Emisor
	"""
	NODE_XML = 'cfdi:Concepto'

	map_fields = (
		Field(attribute_name='valorUnitario'),
		Field(attribute_name='unidad'),
		Field(attribute_name='cantidad'),
		Field(attribute_name='descripcion'),
		Field(attribute_name='importe'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data
		

class Nomina(Base):
	"""
	Nodo de Nomina
	"""
	NODE_XML = 'nomina12:Nomina'

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
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()	

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class NominaEmisor(Base):
	"""
	Nodo de Nomina Emisor
	"""
	NODE_XML = 'nomina12:Emisor'

	map_fields = (
		Field(attribute_name='RfcPatronOrigen'),
		Field(attribute_name='RegistroPatronal'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class NominaReceptor(Base):
	"""
	Nodo de Nomina Receptor
	"""
	NODE_XML = 'nomina12:Receptor'

	map_fields = (
		Field(attribute_name='TipoRegimen'),
		Field(attribute_name='TipoJornada'),
		Field(attribute_name='TipoContrato'),
		Field(attribute_name='SalarioDiarioIntegrado'),
		Field(attribute_name='SalarioBaseCotApor'),
		Field(attribute_name='RiesgoPuesto'),
		Field(attribute_name='Puesto'),
		Field(attribute_name='PeriodicidadPago'),
		Field(attribute_name='NumSeguridadSocial'),
		Field(attribute_name='NumEmpleado'),
		Field(attribute_name='FechaInicioRelLaboral'),
		Field(attribute_name='Departamento'),
		Field(attribute_name='Curp'),
		Field(attribute_name='CuentaBancaria'),
		Field(attribute_name='ClaveEntFed'),
		Field(attribute_name='Banco'),
		Field(attribute_name='Antigüedad')
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class Percepciones(Base):
	"""
	Nodo de Nomina Emisor
	"""
	NODE_XML = 'nomina12:Percepciones'

	map_fields = (
		Field(attribute_name='TotalSueldos'),
		Field(attribute_name='TotalGravado'),
		Field(attribute_name='TotalExento'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class Percepcion(Base):
	"""
	Nodo de Percepcion
	"""
	NODE_XML = 'nomina12:Percepcion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoPercepcion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='ImporteGravado'),
		Field(attribute_name='ImporteExento'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_list_attributes(self.node, self.fields)
		return data


class Deducciones(Base):
	"""
	Nodo de Deducciones
	"""
	NODE_XML = 'nomina12:Deducciones'

	map_fields = (
		Field(attribute_name='TotalOtrasDeducciones'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data


class Deduccion(Base):
	"""
	Nodo de Deduccion
	"""
	NODE_XML = 'nomina12:Deduccion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoDeduccion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='Importe'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_list_attributes(self.node, self.fields)
		return data


class OtroPago(Base):
	"""
	Nodo de OtroPago
	"""
	NODE_XML = 'nomina12:OtroPago'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoOtroPago'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='Importe'),
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	def get_subsidio_empleao(self):
		subsidio_node = self.document.get_elements('nomina12:SubsidioAlEmpleo')
		subsidio = self.document.get_attribute(subsidio_node, 'SubsidioCausado')
		return subsidio

	@property
	def data(self):
		sub_causado = self.get_subsidio_empleao()
		data = self.document.get_list_attributes(self.node, self.fields)
		data[0]['subsidio_empleo'] = sub_causado
		return data


class TimbreFiscalDigital(Base):
	"""
	Nodo de Timbre Fiscal Digital
	"""
	NODE_XML = 'tfd:TimbreFiscalDigital'

	map_fields = (
		Field(attribute_name='selloSAT'),
		Field(attribute_name='selloCFD'),
		Field(attribute_name='noCertificadoSAT'),
		Field(attribute_name='UUID'),
		Field(attribute_name='FechaTimbrado')
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.NODE_XML)
		self.fields = self.get_fields()

	@property
	def data(self):
		data = self.document.get_dict_attributes(self.node, self.fields)
		return data
		

class XmlSerialize(object):



	def get_serializer(self, document):	
		cfdi = {}

		comprobante = Comprobante(document=document)
		emisor = Emisor(document=document)
		receptor = Receptor(document=document)
		concepto = Concepto(document=document)
		nomina = Nomina(document=document)
		nomina_emisor = NominaEmisor(document=document)
		nomina_receptor = NominaReceptor(document=document)
		percepciones = Percepciones(document=document)
		percepcion = Percepcion(document=document)
		deducciones = Deducciones(document=document)
		deduccion = Deduccion(document=document)
		otro_pago = OtroPago(document=document)
		timbre = TimbreFiscalDigital(document=document)

		cfdi['comprobante'] = comprobante.data
		cfdi['emisor'] = emisor.data
		cfdi['receptor'] = receptor.data		
		cfdi['concepto'] = concepto.data
		cfdi['nomina'] = nomina.data		
		cfdi['nomina_emisor'] = nomina_emisor.data
		cfdi['nomina_receptor'] = nomina_receptor.data
		cfdi['percepciones'] = percepciones.data
		cfdi['percepcion'] = percepcion.data
		cfdi['deducciones'] = deducciones.data
		cfdi['deduccion'] = deduccion.data
		cfdi['otro_pago'] = otro_pago.data
		cfdi['timbre'] = timbre.data

		return cfdi
