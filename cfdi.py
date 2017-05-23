from xml_reader import XmlReader
from xml_serialize import XmlSerialize

		

def get_data_cfdi(path):

	document = XmlReader(path=path)
	serializer_data = XmlSerialize().get_serializer(document=document)
	return serializer_data



path = 'CFDI_v12.xml'
data = get_data_cfdi(path=path)
print(data)