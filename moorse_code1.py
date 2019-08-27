# r/dailyprogrammer 
# easy #380
# Smooshed Morse Code 1
# write Moorse code generator

def smorse(text):

	code = {
	  'a' : '.-',
	  'b' : '-...',
	  'c' : '-.-.',
	  'd' : '-..',
	  'e' : '.',
	  'f' : '..-.',
	  'g' : '--.',
	  'h' : '....',
	  'i' : '..',
	  'j' : '.---',
	  'k' : '-.-',
	  'l' : '.-..',
	  'm' : '--',
	  'n' : '-.',
	  'o' : '---',
	  'p' : '.--.',
	  'q' : '--.-',
	  'r' : '.-.',
	  's' : '...',
	  't' : '-',
	  'u' : '..-',
	  'v' : '...-',
	  'w' : '.--',
	  'x' : '-..-',
	  'y' : '-.--',
	  'z' : '--..'
 	}
	text = text.lower()
	print(text, "==> ", end='')
	'''
	#first version
	for t in text:
		for key, value in code.items():
			if t in key:
				print(value, end = '')
	print('')
	'''
	for t in range(len(text)):
		print(code[text[t]], end = '')
	
	print('')

smorse("sos")
smorse("daily")
smorse("programmer")
smorse("bits")
smorse("three")
