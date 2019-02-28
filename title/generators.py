#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from title.util import *
from title.misc import *
from title.names import *
from title.people import *
from title.texttoimg import *

PromoHistoryQ = HistoryQ(2)

class Generator():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def SetPriority(self, sText, List, iPriority):
		for x in range(iPriority):
			List.append(sText)
		
	def _getFMs_(self):
		FMs = ""
		
		iRandLen = randint(4,10)
		for x in range(1, iRandLen):
			iRandChoice = randint(1,3)
			if iRandChoice == 1:
				FMs += "F"
			else:
				FMs += "M"
				
		if "M" not in FMs:
			FMs += "M"
		elif "F" not in FMs:
			FMs += "F"
		
		return FMs
	
	def GenerateTweet(self):
		#self.Girls = BookGirls()
		#self.GirlsBasic = BookGirlsBasic()
		#self.GirlAdjs = BookGirlAdjs()
		#self.GirlCompAdjs = BookGirlCompAdjs()
		#self.Masters = BookMasters()
		#self.MastersBasic = BookMastersBasic()
		#self.MasterGangs = BookMasterGangs()
		#self.MasterAdjs = BookMasterAdjs()
		#self.MasterCompAdjs = BookMasterCompAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()
		self.Gerunds = BookGerunds()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		self.SubtitleCoda = SubtitleCoda()
		
		return ""

def GetTweet(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
	gen = None
	GenType = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	#print("GetTweet() Generator Type is " + str(GenType))
	
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if gen == None:
			gen = Generator()
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
		
	return gen
	
class GeneratorPromo(Generator):
	ID = 0
	Priority = 0
	Type = GeneratorType.Promo
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#sTweet = "Blue Diamond: \U0001F539 Eggplant: \U0001F346 Fire: \U0001F525 Laughing: \U0001F923 Robot: \U0001F916 Green Heart: \U0001F49A Blue Heart: \U0001F499 Purple Heart: \U0001F49C No one under 18: \U0001F51E Winking kiss face: \U0001F618 Star: \U00002B50"

		iRand = randint(1,7)
		while not PromoHistoryQ.PushToHistoryQ(iRand):
			iRand = randint(1,7)

		if iRand == 1:
			sTweet = "Reply to " + WordList(["one of my tweets", "an @bot_lust tweet", "a Flaming Lust Bot tweet"]).GetWord() + " for a fun surprise! " + GetEmoji()
			sTweet += "\n\n\U0001F539Reply \"#book\" and I'll respond with a made-up smutty book title."
			sTweet += "\n\U0001F539Reply \"#lovescene\" to get your own custom love scene!"
		elif iRand == 2:
			sTweet = "Tell your family, friends and lovers to follow " + WordList(["@bot_lust", "Flaming Lust Bot", "me", "this bot"]).GetWord() + " for all the steamy, sweaty, silly action!\n" + GetEmoji(randint(1,3))
		elif iRand == 3:
			sTweet = WordList(["@bot_lust", "Flaming Lust Bot", "this bot"]).GetWord() + " is very naughty, and NOT appropriate for anyone under 18! \U0001F51E\n\nThat includes you, " + WordList(["kid who is hiding their phone behind their math book while they check twitter", str(randint(6,11)) + "th grader who is supposed to be doing homework", str(randint(6,11)) + "th grader who is supposed to be reading"]).GetWord() + "!"
			if CoinFlip(): 
				sTweet += " \U0001F928"
		elif iRand == 4:
			sTweet = "I am a twitter bot\U0001F916 designed to automatically generate " + WordList(["hot", "sexy", "naughty", "steamy"]).GetWord() + "\U0001F525, " + WordList(["filthy", "dirty"]).GetWord() + "\U0001F346, and " + WordList(["funny", "hilarious", "ridiculous", "silly"]).GetWord() + "\U0001F923 scenes from the world's worst smutty romance novel!\n\nReply to one of my tweets " + WordList(["and get a surprise!", "if you want more.", "if you're impatient for my next terrible love scene!"]).GetWord()
		elif iRand == 5:
			if CoinFlip():
				sTweet = "Full disclosure: "
			sTweet += "I am a bot\U0001F916!\n\nBut not the Russian kind of bot, the " + WordList(["funny", "sexy", "naughty", "silly", "dirty"]).GetWord() + " kind of bot!" 
			if CoinFlip():
				sTweet += " " + GetEmoji()
			if CoinFlip():
				sTweet += "\n#botlife #twitterbot"
		elif iRand == 6:
			sTweet = "Look what " + WordList(["my followers are", "people are ", "other twitter users are", "the internet is"]).GetWord() + " saying:\n\n\U00002B50'I am hooked on this ridiculous account!'\n\U00002B50'The stuff this bot comes up with is hysterical. XD'\n\U00002B50'[S]imultaneously hilarious, nauseating, and inspiring'\n\n" + WordList(["Thank you!", "Thanks!", "Thank you all!", "Big bot love to everyone!"]).GetWord() 
			sTweet += " " + GetEmoji(randint(1,3))
		else:
			sTweet = WordList(["I love you", "You're the best", "Big Bot Love", "I \U00002764 you"]).GetWord() + ", followers!"
			if CoinFlip():
				sTweet = "*" + sTweet + "*"
			sTweet += "\n\n" + GetHeartEmoji(randint(1,5))
			
		return sTweet
		
class Generator1(Generator):
	# Blackmailed by the Billionaire Mountain Man 
	ID = 1
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
	
		sTweet = self.VerbsBy.GetWord() + " By\n" + Master.Desc
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace"]) + " by\n" + Master.Desc
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "My")
			
		sTweet = self.VerbsTo.GetWord() + " To " + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "An Erotic"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 2
	
	Master = MaleChar()
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ['BDSM'])
		Master = MaleChar(iNumMaxCBits = 2, NotList = ['BDSM'], bAllowGang = False)
			
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM " + self.SubtitleCoda.GetWord()
			else:
				sTweet += ":\nA Hot Ménage"
		
		return sTweet
		
class Generator6(Generator):
	# Seduced in the Bed of the Billionaire	
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", "Gifted", "Pledged", "Bed", "Sex Dungeon"]
		
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = NotList, bAddArticle = True)
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		else:
			sTweet = self.VerbsBy.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		
		return sTweet
		
class Generator7(Generator):
	# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master1 = MaleChar(iNumMaxCBits = 2, bAllowGang = False)
		Master2 = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		Girl = FemaleChar(iNumMaxCBits = 2)
		sTweet = "The " + Girl.Desc + ",\nThe " + Master1.Desc + ",\n& " + Master2.Desc + ":\n"
		if CoinFlip():
			sTweet += "A Hot Ménage"
		else:
			sTweet += "A " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator8(Generator):
	# My Boyfriend is a Secret Daddy Dom 
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single"])
		sTweet = "My " + WordList(["Boyfriend", "Hot Date", "Fiancé", "Blind Date", "Kidnapper"]).GetWord() + " is a\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + AddArticles(Girl.Desc) + " " + self.SubtitleCoda.GetWord()
		else:
			sTweet += "!"
			
		return sTweet
		
class Generator9(Generator):
	# The Secretary and the Space Werewolf 
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ["BDSM"], bAllowRelate = True)
		Master = MaleChar(iNumMaxCBits = 2, NotList = ["BDSM"], bAllowRelate = True)
		
		sTweet = "The " + Girl.Desc + "\nand\nThe " + Master.Desc 
		sTweet += ":\nA " + WordList([self._getFMs_(), "BDSM", title.misc.SexyAdjs().GetWord().capitalize()]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, bAllowRelate = True)

		sTweet = "Baby For " + Master.Desc

		return sTweet
		
class Generator11(Generator):
	# The Millionaire Sherrif's Virgin
	ID = 11
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, bAllowRelate = True)
		Master = MaleChar(iNumMaxCBits = 2)
		
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc

		return sTweet
		
class Generator12(Generator):
	# Babysitter to the Billionaire Uniporn
	ID = 12
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		sTweet = Girl.Desc + "\nto\n" + Master.Desc
		
		return sTweet
		
class Generator13(Generator):	
	# Babysitter for the Billionaire Uniporn
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		sTweet = Girl.Desc + "\nfor\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(),"A BDSM","A Forbidden"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirl1 = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowSexuality = False)
		GoodGirl2 = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAllowClothing = False, bAllowSexuality = False, bAllowTitle = False)
		BadGirl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = True)
		MasterGang = MaleGangChar(iNumMaxCBits = 3, NotList = ["Gang-Bang"])
		
		Tweets = []

		Tweets.append(GoodGirl1.Desc + "'s\nGang Bang:\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord())
		Tweets.append(BadGirl.Desc + "'s\n" + title.misc.SexyAdjs().GetWord().capitalize() + " Gang Bang:\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord())
		Tweets.append("Gang-Banged By\nThe " + MasterGang.Desc + ":\nA " + GoodGirl2.Desc + " " + self.SubtitleCoda.GetWord())
		Tweets.append("Shared By\nThe " + MasterGang.Desc + ":\nA " + GoodGirl2.Desc + " " + self.SubtitleCoda.GetWord())
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]
		
		return sTweet
		
class Generator15(Generator):
	# The Small-Town Virgin's First Porno
	ID = 15
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowSexuality = False, bAllowTitle = False)
		
		sTweet = Girl.Desc + "'s\nFirst Porno"
		if CoinFlip():
			sTweet += ":\nAn " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator16(Generator):
	# The Small-Town Virgin's First Time
		
	ID = 16
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["MILF", "Concubine", "Wife", "Pregnant", "Mom", "Sex", "Divorced", "Virgin"], bAddArticle = True, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False)

		sTweet = Girl.Desc + " " + WordList(["Virgin", "Virgin", "Virgin", "Anal Virgin"]).GetWord() + "'s\nFirst Time"
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Secret", "An S&M", "A Rough Sex", "An Anal", "A Gang-Bang"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Mountain Man Biker Gang 
	ID = 17
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Subtitles = []
		
		Master = MaleChar(iNumMaxCBits = 2)
		Gang = MaleGangChar(iNumMaxCBits = 3)
		
		sTweet = self.VerbsBy.GetWord() + ":\n"
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Gang.Desc)
		Girl = FemaleChar()
		Subtitles.append("The " + Master.Desc + "'s\n" + Girl.Desc)
		Subtitles.append(AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord())
		
		sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["Sex", "Lesbian","BDSM", "Anal", "MILF"], bAddEndNoun = False, bAllowMaritalStatus = False, bAllowClothing = False, bAllowSexuality = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet += "\"" + WordList(["S@*#!", "Oh No!", "Uh Oh!", "Whoops!", "WTF?!?", "Oh F*@%!"]).GetWord() + " " 
		sTweet += "My\n" + Girl.Desc + " " + WordList(["Girlfriend", "Bride", "Wife", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Step-Sister", "Twin Sister", "Mom", "Baby Momma", "One True Love"]).GetWord() + "\nIs " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", "An Anal Porn Star", "An Erotic Model", "A Fetish Model", "A Slut", "A Butt Slut"]).GetWord() + "!\""
		
		return sTweet
		
class Generator19(Generator):
	# Full Frontal for the Shy Amish Virgin: A BDSM Romance
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["Naked", "Nude", "Nudist"], bAddArticle = True)
		Master = MaleChar(iNumMaxCBits = 3)
		
		if CoinFlip():
			sTweet = "Full Frontal Nudity for\n" + Girl.Desc
		else:
			if CoinFlip():
				sTweet = WordList(["Naked in Public", "Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["For\nThe", "For\nMy"]).GetWord() + " " + Master.Desc
			else:
				sTweet = WordList(["Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["By\nThe", "By\nMy"]).GetWord() + " " + Master.Desc
		
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "A Submissive"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, bAddArticle = True)
		Gang = MaleGangChar(iNumMaxCBits = 3, bAddArticle = True)
		
		sTweet = ""

		sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
		sTweet = "\"I Was " + sVerbBy
		if not "in public" in sVerbBy.lower():
			sTweet += " By\n"
			if CoinFlip():
				sTweet += Master.Desc
			else:
				sTweet += Gang.Desc
		sTweet += ",\nAnd I Liked It\""

		return sTweet
		
class Generator21(Generator):
	# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
	ID = 21
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = self.VerbsBy.GetWord()  + " By\n"
		sTweet += Master.Desc + ":\nA " + Girl.Desc + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
	ID = 22
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlGood = FemaleChar(iNumMaxCBits = 2, Type = GirlType.Good)
		GirlLes = LesbianChar(iNumMaxCBits = 3)
		GirlBad = LesbianChar(iNumMaxCBits = 3, Type = GirlType.Bad)

		
		if CoinFlip():
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlLes.Desc
		else:
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlBad.Desc
		sTweet += ":\n" + WordList(["A Lesbian","A Secret Lesbian","A Taboo Lesbian","A Forbidden",  "An FF",]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator23(Generator):
	# The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
	ID = 23
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = title.names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar(iNumMaxCBits = 2).Desc)
		GayTitles.append("The " + GayChar(iNumMaxCBits = 2).Desc + "\nand\nThe " + GayChar().Desc) 
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + GayChar().Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret Gay","A Taboo","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator24(Generator):
	# Deflowered Live on the Internet: An Amish Futa Princess Experience 
	ID = 24
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Pregnant", "Mom", "MILF", "Concubine", "Wife", "Divorced"])
		
		sTweet = "Deflowered Live"
		if CoinFlip():
			sTweet += "!\n"
		else:
			if CoinFlip():
				sTweet += " on the Interet:\n"
			else:
				sTweet += " on Television:\n"
		sTweet += AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord()
		return sTweet
		
class Generator25(Generator):
	# Greg Gets Pounded In The Butt By The Motorcycle Gang
	ID = 25
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = title.names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("Pounded In The Butt By\nThe Gay " + MaleGangChar().Desc)
		GayTitles.append("Pounded In The Butt By\n" + GayChar(bAddArticle = True).Desc)
		GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + WordList(["Well-Hung", "Well-Endowed"]).GetWord() + " " + GayChar(iNumMaxCBits = 2, NotList = ["Well-Hung", "Well-Endowed"]).Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret","A Taboo Gay","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator26(Generator):
	# Hotwife for Daddy: A BDSM Romance 
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		
		sTweet = AddArticles(Girl.Desc) + "\nFor Daddy:\n"
		sTweet += WordList(["A BDSM","An " + self._getFMs_() + "", "A Taboo", "A Forbidden", "A Forbidden", "A Naughty"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator27(Generator):
	# The Shy Lesbian Gymnast Wore Black
	ID = 27
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"], bAddArticle = True, bAllowRelate = True)
		
		sTweet = Girl.Desc + "\nWore " + WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "A Strap-On"]).GetWord() + ":\n"
		sTweet += "A " + WordList(["FemDom", "Dominatrix", "BDSM", "Cuckold"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet

class Generator28(Generator):
	#Cuckolded By My Amish Maiden Hotwife
	ID = 28
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(bAddEndNoun = False, bAllowMaritalStatus = False, NotList = ['Single', 'Divorced'])
		
		if CoinFlip():
			sTweet = "Cuckolded By My\n" + Girl.Desc + " " + WordList(['Wife', 'Wife', 'Hotwife', 'Fiancé', 'Girlfriend', 'Mistress']).GetWord()
		else:
			sTweet = "My " + WordList(['Wife', 'Wife', 'Hotwife']).GetWord() + " And The\n" + MaleChar(bAllowMaritalStatus = False).Desc + ":\nA Cuckold " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator29(Generator):
	# Blackmailing My Step-Dad's Busty Ballerina
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False, NotList = ["Girlfriend", "Mom", "Dad", "Sister", "Divorced", "Single", "Hotwife", "Virgin"])
		
		sTweet = WordList(["Dating", "Sleeping With", "Blackmailing", "Secretly Dating", "Sharing", "Watching", "Filming", "Claiming", "Spanking", "Tying Up", "Dominating", "Exposing", "Undressing", "Hypnotizing", "Impregnating", "Owning", "Punishing", "Spanking", "Paddling", "Training", "Pleasuring"]).GetWord() + " "
		sTweet += "My " + WordList(["Father's", "Dad's", "Step-Dad's", "Best Friend's", "Neighbor's", "Boss's", "Son's", "Step-Son's"]).GetWord() + "\n"
		sTweet += Girl.Desc + " " + WordList(["Wife", "Girlfriend", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Hotwife"]).GetWord()

		return sTweet
		
class Generator30(Generator):
	# Hot Ménage a Trois: Dick and Lily and The Well-Hung Bodyguard Sumo-Wrestler
	ID = 30
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName1 = NamesMale().FirstName()
		sHisName2 = NamesMale().FirstName()
		sHerName1 = NamesFemale().FirstName()
		sHerName2 = NamesFemale().FirstName()
		sLastName = LastNames().GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		Lesbo = LesbianChar(iNumMaxCBits = 3)
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
		Gay = GayChar(iNumMaxCBits = 3)
		
		Menages = []
		
		sTweet = SexyAdjs().GetWord().capitalize() + " " + WordList(["Ménage", "Ménage a Trois", "Threesome", "Three-Way"]).GetWord() + ":\n"
		
		Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Girl.Desc)
		Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Master.Desc)
		Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Lesbo.Desc)
		Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Master.Desc)
		Menages.append(sHisName1 + " and " + sHisName2 + "\nand\nthe " + Gay.Desc)
		Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Girl.Desc)
		Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Master.Desc)
		
		sTweet += Menages[randint(0, len(Menages) -1)]

		return sTweet
		
class Generator31(Generator):
	#Wanton & Willing: My Naked Lesbian Futa Princess
	ID = 31
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ListAdjs = WordList(title.misc.AttitudeFemale().List + title.misc.PhysCharFemale().List)
		sAdj1 = ListAdjs.GetWord()
		sAdj2 = ListAdjs.GetWord(NotList = [sAdj1])
		sHerName = NamesFemale().FirstName()
		
		sTweet = sAdj1 + " & " + sAdj2 + ":\n"
		
		if CoinFlip():
			Girl = FemaleChar(iNumMinCBits = 2)
			sTweet += "My " + Girl.Desc
		else:
			Girl = FemaleChar()
			sTweet += sHerName + " the " + Girl.Desc

		return sTweet
		
class Generator32(Generator):
	#Stripping For My Best Friend's Cocky Coal-Miner Brother 
	ID = 32
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		#print(misc.RelateMale().List + misc.MaritalStatusMale().List)
		if CoinFlip():
			Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ['Single', 'Man', 'Dad', 'Father', 'Brother', 'Son'], bAllowMaritalStatus = False, bAllowRelate = False)
			if Master.Desc[-3:] == "Man":
				sMaster = Master.Desc[0:-4]
			else:
				sMaster = Master.Desc
			sTweet = WordList(["Sleeping With", "Hooking Up With", "Tempting", "Seducing", "Bedding", "Stripping For", "Secretly Watching", "Showering With", "Spying On", "Sharing", "Playing With", "Claimed By", "Taken By", "Deflowered By", "Dominated By", "Blackmailed By", "Stripped By", "Tied to the Bed By", "Pleasured By", "Spanked By", "Ravished By", "Taken Hard By", "Massaged By", "Going Down On", "Impregnated By"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Daughter", "Sister", "Step-Sister", "Step-Daughter"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Boyfriend", "Fiancé", "Husband", "Hubby"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Step-Mom", "Mom", "Mother"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Brother", "Boyfriend", "Boyfriend", "Step-Brother"]).GetWord()
			else:	
				sTweet += "My Best Friend's\n"
				sTweet += sMaster + " " + WordList(["Son", "Brother", "Boyfriend", "Fiancé", "Husband", "Dad", "Father", "Hubby", "Step-Dad"]).GetWord()
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, NotList = ['Single','Virgin', 'Girl', 'Woman', 'Mom', 'Sister', 'Mother', 'Daughter', 'Lesbian', 'Maiden', 'Wife'], bAllowMaritalStatus = False, bAllowRelate = False, bAllowTitle = False)
			if Girl.Desc[-4:] == "Girl":
				sGirl = Girl.Desc[0:-5]
			elif Girl.Desc[-5:] == "Woman":
				sGirl = Girl.Desc[0:-6]
			else:
				sGirl = Girl.Desc
			sTweet = WordList(["Sleeping With", "Seducing", "Massaging", "Bedding", "Undressing", "Secretly Watching", "Spying On", "Sharing", "Showering With", "Stripping", "Playing With", "Claiming", "Spanking", "Punishing", "Deflowering", "Going Down On", "Blackmailing", "Pleasuring", "Impregnating"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Brother", "Step-Brother", "Step-Son", "Son"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Girlfriend", "Fiancé", "Wife"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Father", "Dad", "Step-Dad"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Girlfriend", "Step-Sister"]).GetWord()
			else:
				sTweet += "My Best Friend's\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Step-Sister", "Daughter", "Step-Daughter", "Fiancé", "Wife", "Step-Mom", "Mom", "Mother"]).GetWord()
			
		return sTweet
		
class Generator33(Generator):
	#Milking Marie: A Pan-sexual Cheerleader Affair
	ID = 33
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = sVerb + " " + self.HerName + ":\n"
		sTweet += "A " + Girl.Desc + "\n" + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator34(Generator):
	ID = 34
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True)
			sTweet = sVerb + " " + Girl.Desc
		else:
			sTweet = sVerb + " " + self.HerName
		
		sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 'Twin Sister', 'Best Friend', 'Lesbian Lover']).GetWord()

		return sTweet
		
class Generator35(Generator):
	ID = 35
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = WordList(['Arousing',
			'Bedding',
			'Bending Over For',
			'Cuckolding',
			'Deep-Throating',
			'Dominating',
			'Fellating',
			'Gagging On',
			'Going Down On',
			'Massaging',
			'Playing With',
			'Pleasing',
			'Riding',
			'Rimming',
			'Seducing',
			'Sharing',
			'Showering With',
			'Smothering',
			'Stripping For',
			'Submitting To',
			'Swallowing',
			'Teaching',
			'Teasing',
			'Tempting',
			'Touching Myself For',
			'Whipping']).GetWord()
		
		Master = MaleChar(iNumMinCBits = 2, bAllowGang = False)
		sTweet = sVerb + " Mr. " + LastNames().GetWord() + ":\n"
		sTweet += "My " + self.SubtitleCoda.GetWord(NotList = ['Story']) + " With A\n" + Master.Desc

		return sTweet
		
class Generator36(Generator):
	#Turned Gay
	ID = 36
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAllowSexuality = False)
			
			if CoinFlip():
				Lesbian = LesbianChar(bAddArticle = True, NotList = ['wife','girlfriend', 'married'])
				sTweet = "Turned Lesbo by " + Lesbian.Desc
			else:
				Lesbian = LesbianChar(NotList = ['wife','girlfriend', 'married', 'lesbian'])
				sTweet = "Straight " + Girl.Desc + "\nfor the \nLesbian " + Lesbian.Desc 
			
		else:
			Man = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
			
			if CoinFlip():
				Gay = GayChar(bAddArticle = True, NotList = ['husband','boyfriend', 'married'])
				sTweet = "Turned Gay by " + Gay.Desc
			else:
				Gay = GayChar(NotList = ['husband','boyfriend', 'married', 'gay'])
				sTweet = "Straight " + Man.Desc + "\nfor the\nGay " + Gay.Desc 

		return sTweet
		
class Generator37(Generator):
	# Showering With My Step-Mom
	ID = 37
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		
		Relations = title.misc.RelateFemale()
		Gerunds = self.Gerunds
		
		Tweets.append("My " + FemaleChar(bAddEndNoun = False).Desc + " " + Relations.GetWord(NotList = ['Girlfriend', 'Wife', 'Mistress']) + ":\n" + AddArticles(WordList(['Taboo', 'Taboo', 'Naughty', 'Forbidden', 'Secret', 'Erotic', 'Steamy']).GetWord()) + " " + self.SubtitleCoda.GetWord())
		Tweets.append(Gerunds.GetWord() + " My " + FemaleChar(bAddEndNoun = False).Desc + " " + Relations.GetWord(NotList = ['Girlfriend', 'Wife', 'Mistress']))
		Tweets.append("My " + Relations.GetWord() + "\nIs A\n" + FemaleChar(bAddEndNoun = True).Desc)
		Tweets.append(Gerunds.GetWord() + " "  + self.HerName + ":\n" + AddArticles(Relations.GetWord(NotList = ['Wife','Girlfriend', 'Mistress'])) + " " + self.SubtitleCoda.GetWord())
		
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]

		return sTweet
		
class Generator38(Generator):
	# My New Step-Dad Is A Visibly-Erect Centaur
	ID = 38
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		
		NotList = ['Husband', 'Boyfriend', 'Hubby', 'Widower', 'Fiancé']
		Relations = title.misc.RelateMale()
		Gerunds = self.Gerunds
		
		Tweets.append("Me And My\n" + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList) + ":\n" + AddArticles(WordList(['Taboo', 'Taboo', 'Naughty', 'Forbidden', 'Secret', 'Erotic', 'Steamy']).GetWord()) + " " + self.SubtitleCoda.GetWord())
		Tweets.append(self.VerbsBy.GetWord() + " By My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList))
		Tweets.append(self.VerbsTo.GetWord() + " To My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList))
		Tweets.append("My New " + Relations.GetWord() + "\nIs A\n" + MaleChar(bAddEndNoun = True, bAllowGang = False, bAllowMaritalStatus = False).Desc)
		Tweets.append(self.VerbsBy.GetWord() + " By My " + Relations.GetWord(NotList = NotList) + ":\n" + AddArticles(MaleChar(bAllowGang = False, bAllowMaritalStatus = False).Desc) + " " + self.SubtitleCoda.GetWord())
		Tweets.append("\"Oh No! " + WordList(["I'm In Love With", "I Have A Crush On", "I Slept With", "I'm Being Blackmailed By", "I'm Horny For", "I'm Turned On By"]).GetWord() + " My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList) + "\"!")
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]

		return sTweet
		
class Generator39(Generator):
	# Taken Hard By My Big Black Biker 
	ID = 39
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		NotList = ["Big", "Black", "BBC"]
		
		Tweets.append(self.VerbsBy.GetWord() + " by the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.VerbsTo.GetWord() + " to the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Gets " + self.VerbsBy.GetWord() + "\nby the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Gets " + self.VerbsTo.GetWord() + "\nto the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " and the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Goes Black for the\n" + MaleChar(NotList = NotList, bAddEndNoun = False, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc + " BBC")
		Tweets.append(FemaleChar(Type = GirlType.Good, bAddArticle = True, NotList = ["Black", "Ebony"]).Desc + "\nGoes Black")

		sTweet = Tweets[randint(0, len(Tweets) - 1)]
		
		return sTweet

class Generator40(Generator):
	# I Was Ridden Bareback By A Burly Lumberjack Businessman, And He's Not My Husband!
	ID = 40
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotVerbs = ['Tempted', 'Beaten', 'Broken', 'Captured', 'Caught', 'Charmed', 'Cuddled', 'Hotwifed', 'Ruled', 'Seduced', 'Tamed', 'Trained']
		
		Master = MaleChar(iNumMaxCBits = 4, bAllowGang = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False)
		if CoinFlip():
			sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nAnd He's Not Her Husband!"
		else:
			sTweet = "I Was " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nWho Was Not My Husband!"

		return sTweet
		
class Generator41(Generator):
	#Seducing Sheryl: The Virginal Nurse and the Big Titty Dominatrix
	ID = 41
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirl = FemaleChar(Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowGenMod = False, bAllowPregState = False, bAllowMaritalStatus = False, bAllowSexuality = False, bAllowSpecies = False)
		BadGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = True, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet = WordList(["Seducing", "Tempting", "Corrupting", "Degrading", "Debauching", "Perverting"]).GetWord() + " " + self.HerName + ":\n"
		sTweet += GoodGirl.Desc + "\nand\n" + BadGirl.Desc 

		return sTweet
		
class Generator42(Generator):
	# Charmed by the Hot Italian Count
	ID = 42
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]
		Nation = title.misc.NationMale()
		Title = title.misc.TitlesMale()
		
		Master = MaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowRelate = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowTitle = False, bAllowAge = False, bAllowProf = False)
		
		Tweets = []
		
		Tweets.append(self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]) + "\nby the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())
		Tweets.append("In the " + WordList(["Bed", "Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem"]).GetWord() + " of the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())
		Tweets.append(self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Public"]) + "\nin the " + WordList(["Bed", "Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem"]).GetWord() + " of the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())

		return Tweets[randint(0, len(Tweets) - 1)]

class Generator43(Generator):
	# Secret Baby for the Well-Hung Italian Count 
	ID = 43
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Nation = title.misc.NationMale()
		Title = title.misc.TitlesMale()
		
		Master = MaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowRelate = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowTitle = False, bAllowAge = False, bAllowProf = False)
		sTweet = WordList(["Secret Baby", "Illegal Baby", "Baby", "Twin Babies", "Secret Twin Babies", "Fertile Surrogate", "Secret Surrogate", "Pregnant", "Secretly Pregnant", "Illegally Pregnant"]).GetWord() + " for the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord()
		
		return sTweet
		
class Generator44(Generator):
	# The Amish French Maid Goes Dogging 
	ID = 44
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 4, bAddArticle = True, bAllowRelate = True, bAllowSexuality = False, bAllowSpecies = False)
		Suffixes = WordList(["Spreads Her Legs", "Spreads Her Legs", "Rides Again", "Puts Out", "Takes It Deep", "Rides A Big One", "Spreads Her Cheeks", "Takes A Roll In The Hay", "Assumes the Position", "Goes Down", "Has a Quickie", "Bends Over", "Goes Dogging", "Gets Laid", "Knocks Boots", "Does the Rumpy Pumpy", "Gets Off", "Goes All The Way", "Drops Her Pants"])

		sTweet = Girl.Desc + "\n" + Suffixes.GetWord()
		
		return sTweet
		
class Generator45(Generator):
	# Naked in the Park: A Sweet Wholesome Cheerleader Adventure
	ID = 45
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NudeActions = WordList(["Naked", "Flashing", "Streaking", "Topless", "Pantsless", "Exposing Herself", "Nude"])
		Places = WordList(["in the Park", "on Main Street", "at the Bank", "at the Bar", "in the Pub", "at the Grocery Store", "at the Gym", "at the Beach", "on Campus", "at the Museum"])
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Nudist"], bAllowClothing = False, bAllowSpecies = False, bAllowSexuality = False)
		
		sTweet = NudeActions.GetWord() + " " + Places.GetWord() + ":\nA " + Girl.Desc + " Adventure"
		return sTweet

class Generator46(Generator):
	ID = 46
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			Master = MaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["boyfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False)
			Relations = title.misc.RelateMale()
			Prefix = WordList(["Secretly In Love With"])
			sTweet = Prefix.GetWord() + "\nMy " + Master.Desc + " " + Relations.GetWord(NotList = ["Boyfriend", "Husband", "Hubbie", "Widower", "Fiancé"])
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["girlfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False)
			Relations = title.misc.RelateFemale()
			Prefix = WordList(["Secretly In Love With"])
			sTweet = Prefix.GetWord() + "\nMy " + Girl.Desc + " " + Relations.GetWord(NotList = ["Girlfriend", "Mistress", "Wife"])
		return sTweet
		
class Generator47(Generator):
	# My Step-Dad Transforms Into A Cocky Gentleman Mer-Man!
	ID = 47
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Relate = title.misc.RelateMale()
		Species = title.misc.SpeciesMale()
		VerbTrans = WordList(["Transforms", "Transforms", "Changes", "Shifts", "Morphs", "Metamorphs"])
		
		Master = MaleChar(bAddEndNoun = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowRelate = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet = "My " + Relate.GetWord() + " " + VerbTrans.GetWord() + "\ninto a\n" + Master.Desc + " " + Species.GetWord() + "!"

		return sTweet
		
class Generator48(Generator):
	# Lusting For the Wicked Blonde Fetish Model
	ID = 48
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		HairTropes = WordList(["Fiery Redhead", "Wholesome Blonde", "Clueless Blonde", "Nerdy Asian", 
			"Asian Schoolgirl", "Spicy Latina", "Haughty Redhead", "Hot-Blooded Italian", "Submissive Asian",
			"Brainy Brunette", "Sassy Black", "Bootylicious Black", "Wicked Blonde", "Shy Brunette",
			"Muscular Blonde", "Snooty French", "Hot-Blooded Gypsy", "Sensual Russian", "Mysterious Geisha",
			"Athletic Brunette"])
		Girl = FemaleChar(iNumMaxCBits = 2, bAllowAge = False, bAllowAttitude = False, bAllowMaritalStatus = False, bAllowPhysChar = False, bAllowRelate = False, bAllowNation = False, bAllowSkinHairColor = False, bAllowSpecies = False)
		
		sTweet = self.Gerunds.GetWord() + " the " + HairTropes.GetWord() + " " + Girl.Desc 

		return sTweet		
		
class Generator49(Generator):
	ID = 49
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		PublicPlaces = WordList(["at the Bowling Alley", 
			"in the Produce Section", 
			"in the Baked Goods Section",
			"in the Bakery",
			"at the Wine Tasting",
			"on the Coffee Table", 
			"in the Restroom at Chiopotle", 
			"Behind the Chic-fil-a", 
			"in the Ball Pit", 
			"in the Whole Foods Parking Lot",
			"in the Men's Restroom",
			"in the Women's Restroom",
			"in the Park",
			"at the Beach",
			"on the Eliptical Machine at the Gym",
			"at the Seafood Restaurant",
			"at the Museum",
			"at the Library",
			"at the Farmer's Market",
			"next to the Duck Pond",
			"in the Window of a Shoe Store",
			"in the Hunting Section at a Wal-Mart",
			"in the Church Graveyard",
			"in the Old Castle Ruins",
			"at the Old Manor House",
			"in the Abandoned Mansion",
			"at the Construction Site",
			"next to the Assembly Line",
			"on a Hotel Balcony"
			])
		
		Verbs = WordList(["Claimed", "Claimed",
			"Mounted",
			"Pleasured",
			"Ravished",
			"Taken","Taken","Taken"])
			
		Adverbs = WordList(["Hard","Hard","Hard",
			"Forcefully",
			"Passionately",
			"Roughly",
			"Ruthlessly",
			"Vigorously"])
			
		Master = MaleChar(bAddArticle = True)
		
		if CoinFlip():
			sTweet = Verbs.GetWord()
		else:
			sTweet = Verbs.GetWord() + " " + Adverbs.GetWord() 

		sTweet += "\n" + PublicPlaces.GetWord() + " by\n" + Master.Desc

		return sTweet
		
class Generator50(Generator):
	ID = 50
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Adjective = WordList(["Light ","Light ",
			"Friendly ",
			"Gentle ",
			"Mild ",
			"","","","","","",""])
		
		NaughtinessStraight = WordList(["Anal", 
			"Anal Sex",
			"Ass-Eating",
			"BDSM",
			"Blowjob",
			"Bondage",
			"Bukkake",
			"Butt Sex",
			"Butt Stuff",
			"Creampie",
			"Cunnilingus",
			"Deep Throat",
			"Dry-Humping",
			"Dogging",
			"Edging",
			"Fellatio",
			"Fingering",
			"Footjob",
			"Foreplay",
			"Fucking",
			"Hand-Job",
			"Jerking Off",
			"Masturbation",
			"Mutual Masturbation",
			"Nipple Play",
			"Pegging",
			"Rape Play",
			"Rimming",
			"Sex",
			"Spanking",
			"Spooning Naked",
			"Striptease",
			"Tantric Sex",
			"Tea-bagging",
			"Titty Fuck",
			"69ing",
			"Water Sports",
			"Wife-Swapping"])
			
		NaughtinessGay = WordList(["Anal", 
			"Anal Sex",
			"Ass-Eating",
			"Butt Sex",
			"Butt Stuff",
			"Deep Throat",
			"Edging",
			"Fellatio","Fellatio",
			"Gay Sex", "Gay Sex", "Gay Sex",
			"Hand-Job",
			"Jerking Off",
			"Masturbation",
			"Mutual Masturbation",
			"Nipple Play",
			"Rimming",
			"Spanking",
			"Spooning Naked",
			"Striptease",
			"Tea-bagging",
			"69ing",
			"Water Sports"])
			
		NaughtinessLez = WordList(["Ass-Eating",
			"BDSM",
			"Bondage",
			"Butt Stuff",
			"Cunnilingus",
			"Dry-Humping",
			"Finger Bang",
			"Fingering",
			"Fisting",
			"Masturbation",
			"Mutual Masturbation",
			"Tit Play",
			"Pegging",
			"Rimming",
			"Rug Munching",
			"Spanking",
			"69ing",
			"Water Sports"])
			
		FriendsGen = WordList(["Brother and Sister",
			"Colleagues",
			"Cousins","Cousins",
			"Co-workers","Co-workers",
			"Good Friends",
			"Friends",
			"Platonic Friends",
			"Roommates",
			"Siblings",
			"Step-Siblings",
			"Study Buddies",
			"Teacher and Student",
			"Teammates"])
			
		FriendsGay = WordList(["Boys",
			"Bros",
			"Brothers",
			"Buddies",
			"Cellmates",
			"Cowboys",
			"Dads",
			"Dudes",
			"Good Friends",
			"Fraternity Brothers",
			"Friends",
			"Lumberjacks",
			"Married Men",
			"Monks",
			"Priests",
			"Roommates",
			"Sailors",
			"Step-Brothers",
			"Straight Friends",
			"Twin Brothers"])
		
		FriendsLez = WordList(["Cellmates",
			"Cheerleaders",
			"Cousins","Cousins",
			"Coworkers",
			"Girls",
			"Girlfriends",
			"Married Women",
			"Moms",
			"Nuns",
			"Nurses",
			"Sisters",
			"Sorority Sisters",
			"Step-Sisters",
			"Twin Sisters"])
		
		sTweet = "What's a Little " + Adjective.GetWord()
		
		if CoinFlip():
			#straight
			sTweet += NaughtinessStraight.GetWord() + " Between " + FriendsGen.GetWord()
		else:
			if CoinFlip():
				#gay
				sTweet += NaughtinessGay.GetWord() + " Between " + FriendsGay.GetWord()
			else:
				#lesbian
				sTweet += NaughtinessLez.GetWord() + " Between " + FriendsLez.GetWord()
				
		sTweet += "?"
		return sTweet

class Generator51(Generator):
	ID = 51
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sName = self.HerName 
		Girl = None
		
		Places = WordList(["Land", "Kingdom", "Planet", "World", "Lost Land", "Lost World", "Forgotten Kingdom", "Island", "Lost Island", "Empire", "Zone", "Forbidden Zone"])
		Beings = WordList(["Penisaurs", "Dong-o-saurs", "Fuck Men", "Ass-Eaters", "Ass Apes", "Cock-o-saurus Rex", "Tri-cock Men", "Sex Robots", "Dildo-Bots", "Uniporns", "Girthy Griffons", "Boner Beasts", "Homo Erectus", "Horny Mermen", "Barewolves", "Lepra-dongs", "Semen Centaurs", "Cum Imps", "Dick Dwarves", "Anal Elves", "Anal Aliens", "Naked Barbarians", "Naked Cowboys", "Massive Martians", "Engorged Energy Beings", "Cum Commandos", "Knob Goblins", "Turgid Trolls"])
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
			
		sTweet = sName + " the " + Girl.Desc + " in:\n"	
		sTweet += "The " + Places.GetWord() + " of the " + Beings.GetWord()

		return sTweet
		
# class Generator58(Generator):
	# ID = 58
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator59(Generator):
	# ID = 59
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet		
		

				
class GeneratorSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in Generator.__subclasses__():
			item = subclass()
			for x in range(0, item.Priority):
				self.GeneratorList.append([item.ID, item])
			
	def RandomGenerator(self, bAllowPromo = True, Type = None):
		Generator = None
		AllowedTypes = []
		
		if not Type is None:
			AllowedTypes = [Type] 
		else:
			AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(GeneratorType.Promo)
			
		#print("RandomGenerator() Allowed types: " + str(AllowedTypes))
		if len(self.GeneratorList) > 0:

			Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
			while not Generator.Type in AllowedTypes:
				Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
				
		return Generator 
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		