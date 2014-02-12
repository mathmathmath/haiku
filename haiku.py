import sys
import hyphenate
import random
import re

class HaikuGenerator:
	# global dictionary = []

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

		# hyph = hyphenate.Hyphenator()

		line1 = ""
		line2 = ""
		line3 = ""

		"""	while firstCount != 5
				add a new word
				get the syllables for the new word
					if firstCount + new word syllables <= 5
						firstCount += new word.SyllableCount
						add new word to the line
		"""
		while firstCount != 5:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			newSyll = len(hyphenate.hyphenate_word(newWord))
			
			if firstCount + newSyll <= 5:
				firstCount += newSyll
				firstLine.append(newWord)

		while secondCount != 7:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			newSyll = len(hyphenate.hyphenate_word(newWord))
			
			if secondCount + newSyll <= 7:
				secondCount += newSyll
				secondLine.append(newWord)

		while thirdCount != 5:
			newWord = dictionary[random.randrange(len(dictionary)-1)].rstrip('\n')
			newSyll = len(hyphenate.hyphenate_word(newWord))
			
			if thirdCount + newSyll <= 5:
				thirdCount += newSyll
				thirdLine.append(newWord)

		for word in firstLine:
			line1 += word + " "
		for word in secondLine:
			line2 += word + " "
		for word in thirdLine:
			line3 += word + " "

		print line1
		print line2
		print line3	

h = HaikuGenerator()
h.makeHaiku()