DOM CFDI
=======

Description
Reading xml file with python using the library minidom.

Requirements
* python v3.3.3
* minidom

Reference library
https://docs.python.org/2/library/xml.dom.minidom.html

use
===

```python

from xml_reader import XmlReader
from xml_serialize import XmlSerialize

document = XmlReader(path=path)
xml_serialize = XmlSerialize()
data = xml_serialize.get_serializer(document=document)

```
