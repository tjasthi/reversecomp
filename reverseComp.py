import sys

#Reading the file
try:
	filename = sys.argv[1]
except:
	raise Exception("Did not specify a filename argument on the command line")
try:
	read_from = open(filename, 'r')
	write_to = open('output.txt','w')
except:
	raise Exception("File does not exist, or is not readable")

def main():
	#Getting the first line of classification
	line = read_from.readline()
	if ((line[0] == ';') or (line[0] == '>')):
			write_to.write(infoLine(line) + '\n')
	else:
		raise Exception("Not in FASTA format")

	#Looping through the file, line by line
	sequence = ''
	translated = ''
	for line in read_from:
		if ((line[0] == ';') or (line[0] == '>')):
			translateWrite(sequence)
			sequence = ''
			write_to.write(infoLine(line) + '\n')
		elif ((line[0] == 'A') or (line[0] == 'T') or (line[0] == 'U') or (line[0] == 'G') or (line[0] == 'C') or (line[0] == 'M') or (line[0] == 'R') or (line[0] == 'W') or (line[0] == 'S') or (line[0] == 'Y') or (line[0] == 'K') or (line[0] == 'V') or (line[0] == 'H') or (line[0] == 'D') or (line[0] == 'B') or (line[0] == 'N') or (line[0] == 'a') or (line[0] == 't') or (line[0] == 'u') or (line[0] == 'g') or (line[0] == 'c') or (line[0] == 'm') or (line[0] == 'r') or (line[0] == 'w') or (line[0] == 's') or (line[0] == 'y') or (line[0] == 'k') or (line[0] == 'v') or (line[0] == 'h') or (line[0] == 'd') or (line[0] == 'b') or (line[0] == 'n') or (line[0] == '\n')):
			sequence = sequence + line
		else:
			raise Exception("Not in FASTA format")
	
	#Translates the final DNA
	translateWrite(sequence)

	#Exit and save
	read_from.close()
	write_to.close()

"""
Takes a sequence and reverses it.
Translates all the letters and writes the translation in groups of 80.
"""
def translateWrite(sequence):
	sequence = sequence[::-1]
	translated = ''
	for x in sequence:
		letter = translate(x)
		translated = translated + letter
	while len(translated) > 80:
		write_to.write(translated[:80] + '\n')
	 	translated = translated[80:]
	write_to.write(translated + '\n')	

"""
Takes in a line and shortens it so only the relevent info is included.
Keeps all info except the parts after the last '|' 
"""
def infoLine(line):
	write_line = ''
	count = 0
	for x in line:
		if x == '|':
			count += 1
			if count == 4:
				write_line = write_line + x
				break
		write_line = write_line + x
	return write_line


"""
Takes a letter and returns the complement.
Works for lowercase and throws an exception if the letter is not recognized.
"""
def translate(letter):
	if letter == 'A':
		return 'T'
	elif letter == 'T' or letter == 'U':
		return 'A'
	elif letter == 'G':
		return 'C'
	elif letter == 'C':
		return 'G'
	elif letter == 'M':
		return 'K'
	elif letter == 'R':
		return 'Y'
	elif letter == 'W':
		return 'W'
	elif letter == 'S':
		return 'S'
	elif letter == 'Y':
		return 'R'
	elif letter == 'K':
		return 'M'
	elif letter == 'V':
		return 'B'
	elif letter == 'H':
		return 'D'
	elif letter == 'D':
		return 'H'
	elif letter == 'B':
		return 'V'
	elif letter == 'N':
		return 'N'
	elif letter == 'a':
		return 't'
	elif letter == 't' or letter == 'u':
		return 'a'
	elif letter == 'g':
		return 'c'
	elif letter == 'c':
		return 'g'
	elif letter == 'm':
		return 'k'
	elif letter == 'r':
		return 'y'
	elif letter == 'w':
		return 'w'
	elif letter == 's':
		return 's'
	elif letter == 'y':
		return 'r'
	elif letter == 'k':
		return 'm'
	elif letter == 'v':
		return 'b'
	elif letter == 'h':
		return 'd'
	elif letter == 'd':
		return 'h'
	elif letter == 'b':
		return 'v'
	elif letter == 'n':
		return 'n'
	elif letter == '\n':
		return ''
	else:
		raise Exception("Contains sequences that are not DNA")

if __name__== "__main__":
	main()