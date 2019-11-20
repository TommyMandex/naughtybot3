#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
MAX_SEARCH_LOOPS = 20
TWIT_CONTROLLER = 'zadieblack'

Q_SIZE = 40

TweetHistoryQ = None
	
class Gender(Enum):
	Male = 1
	Female = 2
	Neuter = 3
	
class Tense(Enum):
	Present = 1
	Past = 2
	Gerund = 3
	
class LocInOutType(Enum):
	Indoors = 1
	Outdoors = 2
	Either = 3
	
class LocPubPrivType(Enum):
	Public = 1
	Private = 2
	Either = 3
	
class GeneratorType(Enum):
	Normal = 1
	Promo = 2
	Test = 3
	BookTitle = 4
	
class GirlType(Enum):
	Good = 1
	Bad = 2
	Neutral = 3

HeartEmoji = ['\U00002764','\U0001F49A','\U0001F499','\U0001F49C','\U0001F49B','\U0001F9E1','\U0001F5A4']

def GetHeartEmoji(iNum = 1):
	sHearts = ""
	
	for i in range(0, iNum):
		sHearts += HeartEmoji[randint(0, len(HeartEmoji) - 1)]
		
	return sHearts
	
Emoji = ['\U0001F346','\U0001F525','\U0001F923','\U0001F916','\U0001F618','\U00002B50','\U0001F601','\U0001F603','\U0001F604','\U0001F609','\U0001F61C','\U0001F643','\U0001F60E','\U0001F607','\U0001F920','\U0001F608','\U0001F31E','\U0001F351',GetHeartEmoji()]

def GetEmoji(iNum = 1):
	sEmoji = ""
	
	for i in range(0, iNum):
		sEmoji += Emoji[randint(0, len(Emoji) - 1)]
		
	return sEmoji
	
#combined version
def AddArticles(sNounPhrase, bMakeUpper = False):
	sArticle = ""
	sNPNounPhrase = "" #Noun phrase without any 'decoration' characters
	
	# Find first alphanumeric character
	iFirstAlphaPos = 0
	for x in range(0, len(sNounPhrase) - 1):
		iFirstAlphaPos = x 
		if sNounPhrase[x].isalpha():
			break
			
	sNPNounPhrase = sNounPhrase[x:]
			
	bDoArticle = True 
	
	#print(" - sNPNounPhrase is " + sNPNounPhrase + "\n")
	# Make sure we haven't created an empty string
	if len(sNPNounPhrase) == 0:
		bDoArticle = False
	
	# Check for words that look plural but aren't (such as 'ass')
	if sNPNounPhrase[-2:].lower() == 'ss':
		#print(" - sNPNounPhrase[-2:] is " + sNPNounPhrase[-2:] + "\n")
		bDoArticle = True 
	elif sNPNounPhrase[-1:].lower() == 's':
		#print(" - sNPNounPhrase[-1:] is " + sNPNounPhrase[-1:] + "\n")
		bDoArticle = False 
	else:
		bDoArticle = True 
	
	if bDoArticle:
		# check for words that start with a vowel but actually have a consonant sound
		if sNPNounPhrase[0:2].lower() in ['f.','h.','l.','m.','n.','r.','s.','x.']:
			#print(" - sNPNounPhrase[0:2] is " + sNPNounPhrase[0:2] + "\n")
			sArticle = 'an'
		if sNPNounPhrase[0:3].lower() in ['uni','one','uro']:
			#print(" - sNPNounPhrase[0:3] is " + sNPNounPhrase[0:3] + "\n")
			sArticle = 'a'
		elif sNPNounPhrase[0:4].lower() in ['hour']:
			#print(" - sNPNounPhrase[0:4] is " + sNPNounPhrase[0:4] + "\n")
			sArticle = 'an'
		elif sNPNounPhrase[0:5].lower() in ['honor']:
			#print(" - sNPNounPhrase[0:5] is " + sNPNounPhrase[0:5] + "\n")
			sArticle = 'an'
		elif sNPNounPhrase[0].lower() in ['a','e','i','o','u']:
			#print(" - sNPNounPhrase[0] " + sNPNounPhrase[0] + "\n")
			sArticle = 'an'
		else:
			sArticle = 'a'
				
	if len(sArticle) > 0 and bMakeUpper:
		if sArticle == 'a':
			sArticle = 'A'
		else:
			sArticle = 'An'
				
	if len(sArticle) > 0:
		sUpdatedPhrase = sArticle + " " + sNounPhrase
	else:
		sUpdatedPhrase = sNounPhrase
			
	return sUpdatedPhrase

def CoinFlip():
	bHeads = True 

	if randint(1,2) == 2:
		bHeads = False
		
	return bHeads 
	
def GenerateFileName():
	# if bot uses same filename every time, twitter might think its spamming. this function randomizes the filename.
	sFileName = ""
	sFileType = "png"
	
	#append current time in seconds, remove '.' that seperates miliseconds
	sFileName += str(time.time()).replace(".", "")
	
	#first part of filename is 5-12 alphanumeric chars
	sAlphaNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	
	for i in range(5, randint(7,13)):
		sFileName += sAlphaNum[randint(0, len(sAlphaNum) - 1)]
		
	sFileName += "." + sFileType
	
	return sFileName
	
def IsTweetTooLong(sTweet):
	bTooLong = True
	
	if len(sTweet) <= MAX_TWITTER_CHARS:
		bTooLong = False 
	
	return bTooLong
		
class HistoryQ():
	def __init__(self, iQSize = Q_SIZE):
		self.MaxQSize = iQSize
		self.HistoryQ = []
	
	def PushToHistoryQ(self, item):
		bPushOK = False 

		if not self.IsInQ(item):
			self.HistoryQ.insert(0,item)
			bPushOK = True
			
			while len(self.HistoryQ) > self.MaxQSize:
				self.HistoryQ.pop()
		
		return bPushOK
		
	def IsInQ(self, item):
		bIsInQ = True 
		
		if len(self.HistoryQ) == 0 or not item in self.HistoryQ:
			bIsInQ = False

		return bIsInQ
			
class HistoryQWithLog(HistoryQ):
	def __init__(self, sLogFileName, iQSize = Q_SIZE):
		super().__init__(iQSize)
		self.LogFileName = sLogFileName
		#print("LogFileName is " + self.LogFileName)
		
		try:
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		except FileNotFoundError:
			open(self.LogFileName, 'w')
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		#print("Loaded HistoryQ:")
		#print(self.HistoryQ)
			
	def LogHistoryQ(self):
		with open(self.LogFileName, 'w') as WriteHistoryQ:
			for item in self.HistoryQ:
				WriteHistoryQ.write(str(item) + "\n")
		#print("Wrote HistoryQ:")
		#print(self.HistoryQ)
	
def FoundIn(sWord, SearchTarget):
	bFound = False 
	
	if isinstance(SearchTarget,str):
		SearchTarget = [SearchTarget]
	
	if isinstance(sWord, str) and isinstance(SearchTarget,list):
		if len(SearchTarget) > 0:
			for s in SearchTarget:
				if isinstance(s, str):
					if s.lower() in sWord.lower() or sWord.lower() in s.lower():
						bFound = True
						break
			
	return bFound 
		
class WordList:
	def __init__(self, NewList = None):
		if NewList == None:
			self.List = []
		else:
			self.List = NewList
			
		self.DefaultWord = ""
		
	def AddWord(self, word):
		self.List.append(word)
	
	def GetWord(self, sNot = "", NotList = None, SomeHistoryQ = None):
		sWord = ""
		
		if NotList is None:
			NotList = []
			
		if sNot != "":
			NotList.append(sNot)
			
		if not self.List == None and len(self.List) > 0:
			sWord = self.List[randint(0, len(self.List) - 1)]
			
			if SomeHistoryQ is None:
				i = 0
				while FoundIn(sWord, NotList) and i < MAX_SEARCH_LOOPS:
					#print("Collision! '" + sWord + "' in NotList, trying again.")
					sWord = self.List[randint(0, len(self.List) - 1)]
					i += 1
			else:
				i = 0
				while (not SomeHistoryQ.PushToHistoryQ(sWord) or FoundIn(sWord, NotList)) and i < MAX_SEARCH_LOOPS:
					#print("Collision! '" + sWord + "' in NotList, trying again.")
					sWord = self.List[randint(0, len(self.List) - 1)]
					i += 1
				
		return sWord
		
	def Length(self):
		iLen = 0
		
		if isinstance(self.List, list):
			iLen = len(self.List)
			
		return iLen
		
	def IsEmpty(self):
		bIsEmpty = True 
		
		if self.Length() > 0:
			bIsEmpty = False 
		
		return bIsEmpty
		
	def GetWordList(self):
		return self.List
		
class NounAdjList:
	def __init__(self, NewNounList = None, NewAdjList = None):
		if NewNounList == None:
			self.NounList = []
		else:
			self.NounList = NewNounList
			
		if NewAdjList == None:
			self.AdjList = []
		else:
			self.AdjList = NewAdjList
			
		self.NounHistoryQ = HistoryQ(3)
		self.AdjHistoryQ = HistoryQ(3)
			
		self.DefaultNoun = ""
		self.DefaultAdj = ""
	
	def GetNoun(self, NotList = None):
		sNoun = ""
		
		if NotList is None:
			NotList = []
		
		if not self.NounList == None and len(self.NounList) > 0:
			sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
			while not self.NounHistoryQ.PushToHistoryQ(sNoun) or sNoun in NotList:
				sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
			
		return sNoun
		
	def GetAdj(self, NotList = None):
		sAdj = ""
		
		if NotList is None:
			NotList = []
		
		if not self.AdjList == None and len(self.AdjList) > 0:
			sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
			while not self.AdjHistoryQ.PushToHistoryQ(sAdj) or sAdj in NotList:
				sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
			
		return sAdj
	
	def GetWord(self, NotList = None):
		sWord = ""
		
		if NotList is None:
			NotList = []
					
		sWord = self.GetAdj(NotList) + " " + self.GetNoun(NotList)
		
		return sWord
		
def SmartLower(phrase):
	sResult = phrase
	if isinstance(sResult,str):
		aOldPhrase = sResult.split()
		aNewPhrase = []
		for item in aOldPhrase:
			#print("Item is " + item + ", length is " + str(len(item)) + ", and item[1].isupper() = " + str(item[1].isupper()))
			if len(item) > 1 and not item[1].isupper():
				aNewPhrase.append(item.lower())
			else:
				aNewPhrase.append(item)
		sResult = ' '.join(aNewPhrase)
		
	return sResult

	
class Sound():
	def __init__(self, newlist):
		self._SoundList = sorted(newlist)
		
	def SoundsLike(self, word):
		bSoundsLike = False 
		
		if isinstance(self._SoundList, list) and isinstance(word,str):
			for item in self._SoundList:
				iSoundLen = len(item)
				if item.lower()[0:iSoundLen] == word.lower()[0:iSoundLen]:
					bSoundsLike = True 
	
		return bSoundsLike
				

def MatchedSound(word1,word2):
	sounds = []
	sounds.append(Sound(['b']))
	sounds.append(Sound(['bl']))
	sounds.append(Sound(['br']))
	sounds.append(Sound(['bw']))
	sounds.append(Sound(['c','k']))
	sounds.append(Sound(['ch']))
	sounds.append(Sound(['cl','kl']))
	sounds.append(Sound(['cr','kr']))
	sounds.append(Sound(['cw','kw','qu']))
	sounds.append(Sound(['d']))
	sounds.append(Sound(['dr']))
	sounds.append(Sound(['dw']))
	sounds.append(Sound(['f']))
	sounds.append(Sound(['fl']))
	sounds.append(Sound(['fr']))
	sounds.append(Sound(['g','gh']))
	sounds.append(Sound(['gl']))
	sounds.append(Sound(['gn','kn','n']))
	sounds.append(Sound(['gr']))
	sounds.append(Sound(['gw']))
	sounds.append(Sound(['h','wh']))
	sounds.append(Sound(['j']))
	sounds.append(Sound(['l',]))
	sounds.append(Sound(['m']))
	sounds.append(Sound(['n']))
	sounds.append(Sound(['p']))
	sounds.append(Sound(['pl']))
	sounds.append(Sound(['pr']))
	sounds.append(Sound(['ps','s']))
	sounds.append(Sound(['r','wr']))
	sounds.append(Sound(['sc','sch','sk']))
	sounds.append(Sound(['sl']))
	sounds.append(Sound(['sm']))
	sounds.append(Sound(['sn']))
	sounds.append(Sound(['sp']))
	sounds.append(Sound(['squ','scw','skw']))
	sounds.append(Sound(['st']))
	sounds.append(Sound(['sw']))
	sounds.append(Sound(['t']))
	sounds.append(Sound(['th']))
	sounds.append(Sound(['tw']))
	sounds.append(Sound(['v']))
	sounds.append(Sound(['w','jua']))
	sounds.append(Sound(['x','z']))

def GetRhymingPair(list1, list2):
	resultpair = [None,None]
	
	shufflist1 = random.shuffle(list1)
	for item1 in shufflist1:
		for item2 in list2:
			if MatchedSound(item1,item2):
				resultpair = [item1,item2]
				break 
				
	return resultpair