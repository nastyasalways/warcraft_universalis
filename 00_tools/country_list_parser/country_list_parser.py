# "C:\Python26_x84\Python.exe" "C:\Users\Ben\Documents\Python Projects\parse_definitions.py"

# Scrap definitions.txt to create the province localisation.
import random
import os
import sys

def getScriptPath():
	""" Returns current path of script """
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
os.chdir( getScriptPath() )

dropped_file = sys.argv[1]
print dropped_file

file = open( "table.txt", "w+" )

with open( dropped_file ) as sourceFile:
	current_file_content = [x.strip('\n') for x in sourceFile.readlines()]
	for line in current_file_content:	
		string = line.split( "=" )
		tag = string[0]
		country_name = string[1]
		tag = tag.strip( "=" )
		tag = tag.strip( " " )
		country_name = country_name.strip( ' ' )
		country_name = country_name.strip( '"' )
		country_name = country_name.strip( '\t' )
		country_name = country_name.strip( 'txt' )
		country_name = country_name.strip( 'countries' )
		country_name = country_name.strip( '.' )
		country_name = country_name.strip( '/' )
		print tag
		print country_name
			
		file.write( "| " + country_name + " | " + tag + " | " + " | " + " | " + " |\n" )
	
file.close()