# -*- encoding: utf-8 -*-
# AUTOR: mauricio2992


from PyPDF2 import PdfFileReader, PdfFileWriter #importamos modulo y librerias
import os #importamos modulo socket para ir a otras carpetas
import sys
import pyexiv2 #importamos modulo para informacion exif, se debe ejecutar apt-get install python-pyexiv2 python-pyexiv2-doc

print chr(27)+"[0;92m"
print " /$$      /$$             /$$                     /$$$$$$$$ /$$ /$$          "
print "| $$$    /$$$            | $$                    | $$_____/|__/| $$          "
print "| $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$       | $$       /$$| $$  /$$$$$$ "
print "| $$ $$/$$ $$ /$$__  $$|_  $$_/   |____  $$      | $$$$$   | $$| $$ /$$__  $$"
print "| $$  $$$| $$| $$$$$$$$  | $$      /$$$$$$$      | $$__/   | $$| $$| $$$$$$$$"
print "| $$\  $ | $$| $$_____/  | $$ /$$ /$$__  $$      | $$      | $$| $$| $$_____/"
print "| $$ \/  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$      | $$      | $$| $$|  $$$$$$$"
print "|__/     |__/ \_______/   \___/   \_______/      |__/      |__/|__/ \_______/"
print "                                                                             "

print chr(27)+"[0m"

def printMeta(ruta): # funcion que obtiene los metadatos de archivos pdf en un directorio
	for dirpath, dirnames, files in os.walk(ruta): # para el diretorio, nombre y archivos en la carpeta docs
		for name in files: #recorremos los posibles fichreos
			ext = name.lower().rsplit('.', 1)[-1]
			if ext in ['pdf']:
				print chr(27)+"[0;31m"+"[+] Metadata for file: %s " %(dirpath+os.path.sep+name)+chr(27)+"[0m" # pintamos el titulo de metadata for file y el directorio y nombre del documento
				pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb')) # abrimos el fichero
				docInfo = pdfFile.getDocumentInfo() # creamos un diccionario con la info recolectada
				for metaItem in docInfo:
					print '[+] ' + metaItem + ':' + docInfo[metaItem]
				print "\n"

def metaJpg(ruta): # funcion que obtiene los metadatos exif de una imagen jpg
	for dirpath,dirname,files in os.walk(ruta): 
		for name in files:
			ext=name.lower().rsplit('.',1)[-1]
			if ext in ['jpg']:
				metadata = pyexiv2.ImageMetadata(dirpath+os.path.sep+name)
				metadata.read()
				print chr(27)+"[0;31m"+"### Metadata for file: %s" %(dirpath+os.path.sep+name)+chr(27)+"[0m"
				for metadato in metadata.exif_keys: 
					print chr(27)+"[0m"+metadato+": "+chr(27)+"[0;32m"+metadata[metadato].raw_value
				print "\n"+chr(27)+"[0m"

if len(sys.argv)==3:
	if sys.argv[1]=="1":
		printMeta(sys.argv[2]) # invocamos la funcion con la ruta como parametro '''
	elif sys.argv[1]=="2":
		metaJpg(sys.argv[2]) # invocamos la funcion con la ruta como parametro
	else:
		print "Options \n\n1. PDF\n2. JPG\n\nUse:\npython metadatos.py [option] [path]\n\nExample:\npython metadatos.py 1 /root/Escritorio"
else:
	print "Options \n\n1. PDF\n2. JPG\n\nUse:\npython metadatos.py [option] [path]\n\nExample:\npython metadatos.py 1 /root/Escritorio"
