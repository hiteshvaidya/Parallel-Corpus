'''
This program takes a text file and replaces all the "." in fractional numbers with ";"
eg. 2.2 -> 2;2
This program can also be used to change the numbers other way round. For this "." and ";" in lines 25, 28 must be interchanged.
eg. 2;2 -> 2.2 
'''
import re 														#re module supports regex

def Change():
	with open('input.txt','r') as file:							#automatically closes file with the end of indentation
		output = open('ouput.txt','w')
		line = file.readline().strip()							#read line in input text file
		
		while True:
			if line == "~~~":									#"~~~" is used to indicate 'end of file' (eof)
				output.write(line+"\n")
				return 											#stop the program if eof is encountered
			elif line == '':									#if line in input file is blank then corresponding line in output will also be blank
				output.write("\n")
				line = file.readline().strip()					#read next line
			while line != '':									#if a line is not blank then proceed
				if line == "~~~":								#if eof file then write it in output file and end the program
					output.write(line+"\n")
					return
				old = re.findall(r'\d+\.\d+', line)				#find numbers like '2.2' using regex '\d+\.\d+' in the line and store in 'old' array
				old = list(set(old))							#remove repeated numbers in old i.e. in a single line
				for i in range(len(old)):
					new = ";".join(old[i].split("."))			#for each number, split using "." and join using ";" and store it in 'new' variable
					line = line.replace(old[i], new)			#replace the numbers in a line. they are found using old[i] and replaced by value in new
				output.write(line+"\n")							#write this changed line in new output file
				line = file.readline().strip()					#read next line
		output.close()											#close output file

Change()														#function call for Change() function