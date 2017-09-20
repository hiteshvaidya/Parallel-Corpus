'''
This program takes text file and separates all the sentences in it. These sentences are then written in a new file such that each sentence is on a new line.
'''
import time 															#time module is used just to check if the program has entered into infinite loop															

class Align:
	def __init__(self):													#constructor used to declare all the variables to be used within the class
		self.para = ""													#it collects all the sentences in this variable
		self.titleFlag = False 											#self.titleFlag is used to indicate if a line is a title/heading eg. chapter name
		self.delim = "। "												#self.delim stores full stop of a language. It is "." for english and "।" for Hindi
		self.marks = {'?',',','!',self.delim[0]}
		self.file = open('hin1-6.txt','r')
		self.output = open('hin1-6-converted.txt','w')

	def Write(self):													#this function writes all the sentences collected till a point
		if self.para == "":
			return
		if self.titleFlag != True:										#if it is not a title/heading
			self.para = self.para.split(self.delim)						#split all the sentences using a delimiter
			for index in self.para:										#for each sentence in collection of sentences
				index = index.strip()
				if index[len(index)-1] != "?" and "?" in index:			#if there are multiple questions concatenated
					index = index.split("? ")							#split them using "?" and write each question on new line
					for count in range(len(index)-1):
						self.output.write(index[count].strip()+"?\n")
					index = index[len(index)-1].split(self.delim)		#split the sentences using a delimiter
					for count in index:
						if count[len(count)-1] == self.delim[0]:		#if the sentence already has delimiter at the end, directly write it
							self.output.write(count.strip()+"\n")
						else:											#if the sentence does not have delimiter at end, add it and write
							self.output.write(count.strip()+self.delim[0]+"\n")
				elif index[len(index)-1] == "?" or index[len(index)-1] == "!" or index[len(index)-1] == self.delim[0]:
					self.output.write(index.strip()+"\n")				#if the sentence has one of the signs in previous line, don't add delimiter at the end
				else:													#only if not then add a delimiter
					self.output.write(index.strip()+self.delim[0]+"\n")
		else:															#if it is a title/heading
			if self.para[len(self.para)-1] == "?" or self.para[len(self.para)-1] == "!" or self.para[len(self.para)-1] == self.delim[0]:
				self.output.write(self.para+"\n")
			else:
				self.output.write(self.para+self.delim[0]+"\n")
		self.para = ""													#clear self.para
		self.titleFlag = False 											#set the title flag to false again

				

	def Convert(self):
		while True:
			line = self.file.readline().strip()
			if line == "~~~":
				self.Write()
				self.file.close()
				self.output.close()
				return
			while line != '':											#if the line is not blank
				if line == "~~~":
					self.Write()
					self.file.close()
					self.output.close()
					return
				elif line[0] == '$' and line[len(line)-1] == '$':		#if a sentence has markers in beginning and end
					self.Write()
					signs = {self.delim[0], '?', ':', '!', ',', ';', '-'}
					if line[len(line)-2] in signs: #== self.delim[0] or line[len(line)-2] == '?' or line[len(line)-2] == ':' or line[len(line)-2] == '!' or line[len(line)-2] == ',' or line[len(line)-2] == ';' or line[len(line)-2] == '-':
						self.output.write(line[1:len(line)-1]+'\n')		#if the sentence ends with any of the symbols in 'signs', don't add delimiter
					else:
						self.output.write(line[1:len(line)-1]+self.delim[0]+'\n')
				elif line[0] == '$' and line[len(line)-1] != '$':		#collect all the sentences between $ marks
					self.Write()
					self.para += line[1:]
					line = self.file.readline().strip()
					while line[len(line)-1] != '$':
						self.para += " "+line
						line = self.file.readline().strip()
					self.para += " "+line[:len(line)-1]
					self.titleFlag = True
					self.Write()
				else:
					self.para += " "+line
				line = self.file.readline().strip()





aln = Align()
time0 = time.clock()
aln.Convert()
time1 = time.clock()
print("Total processing time = ",time1-time0)