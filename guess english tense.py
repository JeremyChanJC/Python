#Enter a word for detection
#Check if the word contains 'ed', or ing.
#If the word contains 'ed', it is a past tense.
#If the word contains 'ing', it is a prgressive form.
#If the word contains none of 'ed' or 'ing', it is a prgressive form.
#Enter the word list for irregular verbs to exclude them for detection.

print("Enter a word.")

verb = input()

if 'ed' in verb or verb == 'xxx' or 'yyy' or 'zzz':
	verbType = 'past tense'
elif 'ing' in verb :
	verbType = 'prgressive form'
else:verbType = 'base form'

print ("I think the verb " + verb + " is a "+ verbType + ".")