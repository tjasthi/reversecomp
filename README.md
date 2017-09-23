The program reverseComp.py pens a file, whose filename is specified by the user as a command-line argument. That is, if the name of your Python script is programname and the name of the file is filename, then the script should be run by typing the following at the Unix command line: programname filename
Reads the contents of the file, assuming it is a FASTA file of DNA sequences.
Prints (to standard output) the name and reverse-complemented sequence of every DNA sequence in the file, in FASTA format (80 characters/line).

When doing so, it must:
Correctly handle IUPAC degenerate characters (for example, R is complemented to Y)
Preserve case

Your program should exit gracefully (that is, report an error and stop execution, e.g. by raising a Python exception) if any of the following error conditions are met:
The user did not specify a filename argument on the command line
The file named by the user does not exist, or is not readable
The file named by the user is not in FASTA format
The file named by the user contains sequences that are not DNA

Where possible, you should recover from other "typical" errors with minimal disruption to the user of your script (for example, if the format is not strict FASTA because it exceeds 120 characters per line in the sequence sections, your script should still accept it, but it should output strict 80-character-per-line FASTA).
