# MetaFile

MetaFile es un script creado por mauricio2992 en Python para la extracción de los metadatos de los archivos PDF y JPG de un directorio. Para su funcionamiento es necesaria la instalación de las librerías PyPDF2 y pyexiv2, ejecutando en Debian:

$sudo apt-get install python-pyexiv2 python-pyexiv2-doc\n$sudo pip install PyPDF2

para su uso se ejecuta:

python metafile.py [option] [path]

Options: 1. PDF / 2. JPG

Ejemplo:

python metafile.py 1 /root/Documents 