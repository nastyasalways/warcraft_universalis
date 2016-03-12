# "C:\Python26_x84\Python.exe" "C:\Users\Ben\Documents\Python Projects\parse_definitions.py"

# Scrap definitions.txt to create the province localisation.
import random
import os
import sys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
os.chdir( getScriptPath()  + "\output" )

dropped_file = sys.argv[1]
print dropped_file

e_file = open( "prov_names_l_english.yml", "w+" )
f_file = open( "prov_names_l_french.yml", "w+" )
g_file = open( "prov_names_l_german.yml", "w+" )
s_file = open( "prov_names_l_spanish.yml", "w+" )
e_file.write( "l_english:\n" )
f_file.write( "l_french:\n" )
g_file.write( "l_german:\n" )
s_file.write( "l_spanish:\n" )

wastelands = open( "wastelands.txt", "w+" )
seas = open( "seas.txt", "w+" )
lakes = open( "lakes.txt", "w+" )

with open( dropped_file ) as sourceFile:
	current_file_content = [x.strip('\n') for x in sourceFile.readlines()]
	skip = False
	for line in current_file_content:
		if skip == True:	
			string = line.split( ";" )
			id = string[0]
			print id
			comment = string[5]
			type = string[4]
			
			if comment == "x":
				comment = ""
				
			if type == "wasteland":
				wastelands.write ( id + " # " + comment + "\n" )
			
			if type == "sea":
				seas.write ( id + " " )
				
			if type == "lake":
				lakes.write ( id + " " )
				
			e_file.write( " PROV" + id + ": \"" + comment + "\"\n" )
			f_file.write( " PROV" + id + ": \"" + comment + "\"\n" )
			g_file.write( " PROV" + id + ": \"" + comment + "\"\n" )
			s_file.write( " PROV" + id + ": \"" + comment + "\"\n" )
		else:
			skip = True
			
e_file.close()
f_file.close()
g_file.close()
s_file.close()
wastelands.close()
seas.close()
lakes.close()