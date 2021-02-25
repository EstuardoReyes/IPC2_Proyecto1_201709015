from xml.etree.ElementTree import Element, tostring
from ElementTree_pretty import prettify

album=etree.Element("album")
doc=etree.ElementTree(album)
album.append(etree.Element("autor"))
album.append(etree.Element("titulo"))
album.append(etree.Element("formato"))
album.append(etree.Element("localizacion"))
album[0].text="SABINA Y CIA Nos sobran los motivos"
album[0].attrib["pais"]="ES"
album[1].text="Joaquín Sabina"
album[2].text="MP3"
album[3].text="Varios CD5"