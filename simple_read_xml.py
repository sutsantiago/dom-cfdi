from xml.dom import minidom
 
def get_comprobante(doc):
	nodoComprobante = doc.getElementsByTagName("cfdi:Comprobante")
	element = {
		"lugarExpedicion": nodoComprobante[0].getAttribute("LugarExpedicion"),
		"total": nodoComprobante[0].getAttribute("total"),
		"descuento": nodoComprobante[0].getAttribute("descuento"),
		"noCertificado": nodoComprobante[0].getAttribute("noCertificado"),
		"fecha": nodoComprobante[0].getAttribute("fecha"),
		"folio": nodoComprobante[0].getAttribute("folio"),
		"serie": nodoComprobante[0].getAttribute("serie"),
	}
	return element

def get_emisor(doc):
	nodoEmisor = doc.getElementsByTagName("cfdi:Emisor")
	nodoDomicilioFiscal = doc.getElementsByTagName("cfdi:DomicilioFiscal")
	element = {
		"rfc": nodoEmisor[0].getAttribute("rfc"),
		"nombre": nodoEmisor[0].getAttribute("nombre"),
		"calle"	: nodoDomicilioFiscal[0].getAttribute("calle"),
		"noExterior": nodoDomicilioFiscal[0].getAttribute("noExterior"),
		"noInterior": nodoDomicilioFiscal[0].getAttribute("noInterior"),
		"colonia": nodoDomicilioFiscal[0].getAttribute("colonia"),
		"municipio": nodoDomicilioFiscal[0].getAttribute("municipio"),
		"estado": nodoDomicilioFiscal[0].getAttribute("estado"),
		"pais": nodoDomicilioFiscal[0].getAttribute("pais"),
		"codigoPostal": nodoDomicilioFiscal[0].getAttribute("codigoPostal"),
	}
	return element

def get_receptor(doc):
	nodoReceptor = doc.getElementsByTagName("cfdi:Receptor")
	element = {
		"rfc": nodoReceptor[0].getAttribute("rfc"),
		"nombre": nodoReceptor[0].getAttribute("nombre"),
	}
	return element

def get_nomina(doc):
	nodoNomina = doc.getElementsByTagName("nomina:Nomina")
	element = {
		"salarioBaseCotApor": nodoNomina[0].getAttribute("SalarioBaseCotApor"),
		"periodicidadPago": nodoNomina[0].getAttribute("PeriodicidadPago"),
		"tipoJornada": nodoNomina[0].getAttribute("TipoJornada"),
		"puesto": nodoNomina[0].getAttribute("Puesto"),
		"antiguedad": nodoNomina[0].getAttribute("Antiguedad"),
		"fechaInicioRelLaboral": nodoNomina[0].getAttribute("FechaInicioRelLaboral"),
		"departamento": nodoNomina[0].getAttribute("Departamento"),
		"numDiasPagados": nodoNomina[0].getAttribute("NumDiasPagados"),
		"fechaFinalPago": nodoNomina[0].getAttribute("FechaFinalPago"),
		"fechaInicialPago": nodoNomina[0].getAttribute("FechaInicialPago"),
		"fechaPago": nodoNomina[0].getAttribute("FechaPago"),
		"numSeguridadSocial": nodoNomina[0].getAttribute("NumSeguridadSocial"),
		"curp": nodoNomina[0].getAttribute("CURP"),
		"numEmpleado": nodoNomina[0].getAttribute("NumEmpleado"),
	}
	return element

def get_percepciones(doc):
	nodoPercepciones = doc.getElementsByTagName("nomina:Percepciones")
	element = {
		"totalGravado": nodoPercepciones[0].getAttribute("TotalGravado"),
		"totalExento": nodoPercepciones[0].getAttribute("TotalExento"),
	}
	return element
	
def get_percepcion(doc):
	nodos = doc.getElementsByTagName("nomina:Percepcion")
	lisPer = []
	for nodo in nodos: 
		element = {
			"clave": nodo.getAttribute("Clave"),
			"tipoPercepcion": nodo.getAttribute("TipoPercepcion"),
			"concepto": nodo.getAttribute("Concepto"),
			"importeGravado": nodo.getAttribute("ImporteGravado"),
			"importeExento": nodo.getAttribute("ImporteExento"),
		}
		lisPer.append(element)
	return lisPer

def get_deducciones(doc):
	nodoDeducciones = doc.getElementsByTagName("nomina:Deducciones")
	element = {
		"totalGravado": nodoDeducciones[0].getAttribute("TotalGravado"),
		"totalExento": nodoDeducciones[0].getAttribute("TotalExento"),
	}
	return element

def get_deduccion(doc):
	nodos = doc.getElementsByTagName("nomina:Deduccion")
	lisDed = []
	for nodo in nodos:
		element = {
			"clave": nodo.getAttribute("Clave"),
			"tipoPercepcion": nodo.getAttribute("TipoDeduccion"),
			"concepto": nodo.getAttribute("Concepto"),
			"importeGravado": nodo.getAttribute("ImporteGravado"),
			"importeExento": nodo.getAttribute("ImporteExento"),
		}
		lisDed.append(element)
	return lisDed

def get_horas_extra(doc):
	nodos = doc.getElementsByTagName("nomina:HorasExtra")
	lisHrs = []
	for nodo in nodos:
		element = {
			"dias": nodo.getAttribute("Dias"),
			"tipoHoras": nodo.getAttribute("TipoHoras"),
			"horasExtra": nodo.getAttribute("HorasExtra"),
			"importePagado": nodo.getAttribute("ImportePagado"),
		}
		lisHrs.append(lisHrs)
	return lisHrs

def get_xml_data(path=None):
	doc = minidom.parse(path)

	data = {
		"comprobante": get_comprobante(doc),
		"emisor": get_emisor(doc),
		"receptor": get_receptor(doc),
		"nomina": get_nomina(doc),
		"percepciones": get_percepciones(doc),
		"percepcion": get_percepcion(doc),
		"deduciones": get_deducciones(doc),
		"deducion": get_deduccion(doc),
		"horasExtra": get_horas_extra(doc),
	}

	return data


#call funtion
print(get_xml_data("CFDI_v11.xml"))