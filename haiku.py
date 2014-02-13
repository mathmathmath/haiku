import sys
# import hyphenate
import random
# from hyphen import Hyphenator, dict_info
# from hyphen.dictools import *
import re

class HaikuGenerator:
	def __init__(self):
		dictFile = open('2of12.txt')
		global dictionary 
		dictionary = dictFile.readlines()
		dictFile.close()

	def makeHaiku(self):
		firstLine = []
		secondLine = []
		thirdLine = []

		firstCount = 0
		secondCount = 0
		thirdCount = 0

		# h_en = Hyphenator('en_US')

		line1 = ""
		line2 = ""
		line3 = ""

		while firstCount != 5:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			# print h_en.syllables(newWord)
			# newSyll = len(h_en.syllables(newWord))
			newSyll = self.countSylls(newWord)
			
			if firstCount + newSyll <= 5:
				firstCount += newSyll
				firstLine.append(newWord)

		while secondCount != 7:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			# print h_en.syllables(newWord)
			# newSyll = len(h_en.syllables(newWord))
			newSyll = self.countSylls(newWord)
			
			if secondCount + newSyll <= 7:
				secondCount += newSyll
				secondLine.append(newWord)

		while thirdCount != 5:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			# print h_en.syllables(newWord)
			# newSyll = len(h_en.syllables(newWord))
			newSyll = self.countSylls(newWord)
			
			if thirdCount + newSyll <= 5:
				thirdCount += newSyll
				thirdLine.append(newWord)

		for word in firstLine:
			line1 += word + " "
		for word in secondLine:
			line2 += word + " "
		for word in thirdLine:
			line3 += word + " "

		print "\n"
		print line1
		print line2
		print line3	


	def countSylls(self, word):
		vowels = ['a', 'e', 'i', 'o', 'u']
		currentWord = []
		currentWord.extend(word)
		numVowels = 0

		lastWasVowel = False
		firstLetter = True

		for wc in currentWord:

			foundVowel = False
			for v in vowels:

				if v == wc and lastWasVowel:
					foundVowel = True
					lastWasVowel = True
					break
				elif v == wc and not lastWasVowel:
					numVowels += 1
					foundVowel = True
					lastWasVowel = True
					break
				elif wc == 'y' and not lastWasVowel and not firstLetter:
					numVowels += 1
					foundVowel = True
					lastWasVowel = True
					break

			if not foundVowel:
				lastWasVowel = False

			firstLetter = False

		if len(currentWord) > 2 and word[len(currentWord)-2:len(currentWord)-1] == "es":
			numVowels += -1
		elif len(currentWord) > 1 and word[len(currentWord)-1] == "e":
			numVowels += -1	
		elif len(currentWord) > 1 and word[len(currentWord)-1] == "y" and word[len(currentWord)-3] in vowels:
			numVowels += -1	

		return numVowels



h = HaikuGenerator()
h.makeHaiku()