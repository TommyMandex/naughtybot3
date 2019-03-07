#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from title.util import *
from title.misc import *
from title.generators import *
from title.names import *
from title.people import *
from title.texttoimg import *



def LastNameBuilder(NotList = None):
	sLName = ""
	
	Names = []
	
	if NotList == None:
		NotList = []
	
	sName1 = LastNames().GetWord(NotList = NotList)
	sName2 = LastNames().GetWord(NotList = [sName1] + NotList)
	
	for _ in range(4):
		Names.append(sName1)
	
	Names.append(sName1 + "-" + sName2)
	
	sLName = Names[randint(0, len(Names) - 1)]
	
	return sLName
		
def AuthorBuilder(Gender = Gender.Neuter):
	sAName = ""
	
	Alphabet = "AAAABBBCCDDDEEEEFFFGGGGHHHIIJJJJKKLLLMNOOPPPQRRRRSSSSTTTTUVVWWWXYZ"
	
	FirstNames = []
	MaleNames = NamesMale()
	FemNames = NamesFemale()
	
	sName = ""
	for _ in range(2):
		sName += Alphabet[randint(0, len(Alphabet) - 1)] + "."
	FirstNames.append(sName)
	
	if Gender == Gender.Male or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(MaleNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(2):
			sName1 = MaleNames.FirstName()
			sName2 = MaleNames.FirstName()
			while sName2 in sName1:
				sName2 = MaleNames.FirstName()
			FirstNames.append(sName1 + " " + sName2)
			
		for _ in range(4):
			FirstNames.append(MaleNames.FirstName() + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
		
	if Gender == Gender.Female or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(FemNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(2):
			sName1 = FemNames.FirstName()
			sName2 = FemNames.FirstName()
			while sName2 in sName1:
				sName2 = FemNames.FirstName()
			FirstNames.append(sName1 + " " + sName2)
			
		for _ in range(4):
			FirstNames.append(FemNames.FirstName() + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
		
	sAName = FirstNames[randint(0, len(FirstNames) - 1)]
	
	sAName += " " + LastNameBuilder(NotList = [sAName])
	
	return sAName

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets
	
class TweetTxtGen():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def SetPriority(self, sText, List, iPriority):
		for x in range(iPriority):
			List.append(sText)
	
	def GenerateTweet(self):
		self.BookSeller = BookSellers()
		self.Hashtag = Hashtags()
		self.SexyAdj = SexyAdjs()
		
		return ""
		
class TweetTxtGen1(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	ID = 1
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "The " + self.SexyAdj.GetWord() + " " + WordList(["read", "book", "ebook"]).GetWord() + " that was " + WordList(["BANNED on", "TOO HOT for", "TOO FILTHY for", "too much for"]).GetWord() + " Amazon! Now available on " + self.BookSeller.GetWord(NotList = ["Amazon", "Kindle Unlimited"]) 
		if CoinFlip():
			sText += " (from " + AuthorBuilder() + ")"
		#=============================
		
		return sText
		
class TweetTxtGen2(TweetTxtGen):
	# Available soon on Amazon and Smashwords. By Ben Dover
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Coming soon on", "Available soon on", "Look for this soon on", "Get it now on", "Download it today on"]).GetWord() + " " + sBookSeller 
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		
		return sText
		
class TweetTxtGen3(TweetTxtGen):
	# Watch for this naughty ebook on Wattpad and Kobo. By Ben Dover 
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Watch for this", "Look for this", "Keep an eye out for this"]).GetWord() + " " + self.SexyAdj.GetWord() + " ebook on " + sBookSeller
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		#=============================
		
		return sText
		
class TweetTxtGen4(TweetTxtGen):
	# Coming soon to discerning readers on Amazon and Smashwords. By Ben Dover 
	ID = 4
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Available soon", "Coming soon", "On its way soon"]).GetWord() + " to " + WordList(["discerning", "discrete", "discriminating"]).GetWord() + " readers on " + sBookSeller 
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		
		return sText
		
class TweetTxtGen5(TweetTxtGen):
	# Ben Dover's Patreon supporters get instant access to all his filthy reads!
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		Supporters = WordList(["Patreon supporters", "supporters on Patreon"])
		Access = WordList(["instant access", "free access", "access"])
		Reads = WordList(["reads", "books", "stories"])
		
		if CoinFlip():
			# male
			sText = AuthorBuilder(Gender = Gender.Male) + "'s "
			sText += Supporters.GetWord() + " get " + Access.GetWord() + " to all his " + self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"
		else:
			# female
			sText = AuthorBuilder(Gender = Gender.Female) + "'s "
			sText += Supporters.GetWord() + " get " + Access.GetWord() + " to all her " + self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"

		
		return sText
		
class TweetTxtGen6(TweetTxtGen):
	# Get excited! The wait is over for Ben Dover's latest sexy release!
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["At last!","At last!","At last!", "Finally!","Finally!", "Get excited!", "It's here!"]).GetWord() + " The wait is over for " + AuthorBuilder() + "'s " + WordList(["newest", "latest"]).GetWord() + " " + self.SexyAdj.GetWord() + " " + WordList(["book","book","book","release","novel","ebook", "release"]).GetWord() + "!"
		
		return sText
		
class TweetTxtGen7(TweetTxtGen):
	# Out soon from Ben Dover
	ID = 7
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Available soon", "Coming soon", "On its way soon", "Out soon", "Arriving soon"]).GetWord() + " from " + AuthorBuilder() 
		
		return sText
		
class TweetTxtGen8(TweetTxtGen):
	# The fisting scene is really surprisingly tasteful!
	ID = 8
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "The " + WordList(["anal", "anal", "orgy", "gangbang", "fisting", "reverse gangbang", "double gangbang", "triple penetration", "deep throat", "incest", "foursome", "fivesome", "MILF orgy", "lesbian orgy", "gay bathhouse", "bukkake", "forced feminization", "choking", "twincest", "Dirty Sanchez", "pee drinking", "wife swapping"]).GetWord() + " scene is " 
		sText += WordList(["surprisingly", "actually surprisingly", "really surprisingly", "actually very", "really quite", "actually unexpectedly", "unexpectedly"]).GetWord() + " " 
		sText += WordList(["tasteful", "tasteful", "loving", "affectionate", "sweet", "heartfelt", "classy", "subdued", "discrete", "charming", "endearing", "thoughtful", "tactful", "wistful"]).GetWord() 
		
		return sText
		
class TweetTxtGen9(TweetTxtGen):
	# If you only read one book this year about clown bukkake, make sure it is this one!
	ID = 9
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "If you only read one book this " + WordList(["year", "year", "year", "month", "month", "decade", "week", "week", "century"]).GetWord() + " about "
		sText += WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat man", "dwarf", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur"]).GetWord() + " "
		sText += WordList(["nipple play", "incest", "threesomes", "fisting", "foursomes", "fivesomes", "bukkake", "bukkake", "forced feminization", "spanking", "rope play", "water-sports", "wife swapping", "69ing", "choking play", "orgies", "gangbangs", "reverse gangbangs", "harems", "lactation"]).GetWord() + ", " 
		sText += WordList(["it should be", "make sure it is", "I heartily recommend"]).GetWord() + " this one!" 

		
		return sText
		
class TweetTxtGen10(TweetTxtGen):
	# Who will Emily choose, the rodeo clown or her step-dad? I was on the edge of my seat! #teamstepdad
	ID = 10
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sSuitor1 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True).Desc.lower()
		sSuitor2 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True).Desc.lower()
		sText = "Who will " + NamesFemale().FirstName() + " choose, " + sSuitor1 + " or " + sSuitor2 + "? I was on the edge of my seat! " 
		if CoinFlip():
			if CoinFlip():
				sText += "#team" + sSuitor1.replace(" ", "").replace("the", "").replace("her", "").replace("-", "")
			else:
				sText += "#team" + sSuitor2.replace(" ", "").replace("the", "").replace("her", "").replace("-", "")
		
		return sText
		
class TweetTxtGen11(TweetTxtGen):
	# Include one little sumo wrestler fisting scene and they ban you from Amazon for life!
	ID = 11
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Include one little "
		sText += WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat-man", "dwarf", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur", "velociraptor", "pro-wrestler"]).GetWord() + " "
		sText += WordList(["anal", "double anal", "nipple play", "fisting", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "bukkake", "feminization", "paddling", "rope play", "water-sports", "wife swapping", "69", "choking", "orgy", "gangbang", "reverse gangbang", "lactation", "double penetration", "triple penetration", "pee-drinking", "Dirty Sanchez"]).GetWord() + " scene, " 
		sText += "and they ban you from Amazon" 
		if CoinFlip():
			sText += " for life"
		sText += "!"
		
		return sText
		
class TweetTxtGen12(TweetTxtGen):
	# Ben Dover is truly the Hemmingway of triple penetration!
	ID = 12
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = AuthorBuilder() + " is truly the " + WordList(["Stephen King", "J.K. Rowling", "Jane Austen", "William Shakespeare", "Shia Lebouf", "Charles Dickens", "Hemmingway", "Agatha Christie", "Maya Angelou", "Tolstoy", "Melville", "Harper Lee", "John Grisham", "Proust", "Emily Dickinson", "Truman Capote", "James Patterson", "Dean Koontz"]).GetWord() + " of "
		sText += WordList(["gay", "lesbian", "MILF", "unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dwarf", "dragon", "orc", "goat man", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur"]).GetWord() + " "
		sText += WordList(["anal", "nipple play", "incest", "fisting", "twincest", "threesomes", "foursomes", "fivesomes", "bukkake", "bukkake", "forced feminization", "spanking", "rope play", "water-sports", "wife swapping", "69", "choking", "orgy", "gangbang", "reverse gangbangs", "lactation", "double penetration", "triple penetration", "porn", "erotica", "edging", "BDSM", "bondage", "cuckolding"]).GetWord() + "!" 

		return sText
		
class TweetTxtGen13(TweetTxtGen):
	# Honestly, these books don't really get going until the 16th book in the series.
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["You know,", "Honestly,", "To tell the truth", "In my opinion", "They say that"]).GetWord() + " these books " + WordList(["really get going after", "really hit their stride after", "don't really get good until", "really take off after", "don't really take off until", "really get good after"]).GetWord() + " the " + str(randint(4, 20)) + "th book in the series"
		
		return sText
		
class TweetTxtGen14(TweetTxtGen):
	# CONTENT WARNING: book contains graphic depictions of veganism.
	ID = 14
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["WARNING", "CONTENT WARNING", "READER WARNING", "ALERT", "READER ALERT"]).GetWord() + ": book contains " 
		sText += WordList(["explicit", "explicit", "explicit", "graphic", "graphic", "vivid"]).GetWord() + " " + WordList(["depictions", "descriptions", "scenes"]).GetWord() + " of " 
		sText += WordList(["vaping", "80's hairstyles", "mullet haircuts", "sports talk radio", "the 1970's", "trips to IKEA", "Bronies", "ferret grooming", "juice cleanses", "large animal husbandry", "women ordering ham-and-pineapple pizza", "women consuming kale smoothies", "veganism", "crossword puzzle solving", "sporks", "fish being reheated in the microwave", "men listening to Nickleback", "tax preparation", "men recording a podcast", "older women discussing their colonoscopies", "Bitcoin investing", "Jazzercize", "essential oil use", "craft-brewed beer enthusiasts", "hipster beard hygene", "bitchy soccer moms", "the music of Ariana Grande"]).GetWord() + "!"
		
		return sText
		
class TweetTxtGen15(TweetTxtGen):
	# I honestly had no idea that I was into bald centaurs until I read this book.
	ID = 15
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "I honestly had no idea that I was into " + WordList(["sexy", "sexy", "sexy", "kinky", "well-hung", "well-endowed", "naughty", "naughty", "gay", "bisexual", "bearded", "bald", "short", "mustachioed", "constantly-aroused", "repressed", "stay-at-home", "stay-at-home", "blue-collar", "Asian", "cuckolded", "lactating", "submissive", "dominant", "well-dressed", "flannel-wearing", "vegan"]).GetWord() + " "
		sText += WordList(["unicorns", "centaurs", "werewolves", "mermen", "dwarves", "dragons", "orcs", "popes", "trolls", "goat-men", "futanari", "aliens", "tentacle monsters", "pirates", "lumberjacks", "trapeze artists", "clowns", "sumo wrestlers", "were-horses", "gorillas", "dinosaurs", "dinosaurs", "blacksmiths", "Japanese businessmen", "guys named Steve"]).GetWord() + " "
		sText += "until I read this book." 
		
		return sText
		
class TweetTxtGen16(TweetTxtGen):
	# SPOILER ALERT: Amber winds up deep-throating a biker
	ID = 16
	Priority = 300
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "SPOILER ALERT: at the end, " + NamesFemale().FirstName() + " " 
		sText += WordList(["has anal sex with", "gets fisted by", "has her toes sucked by", "tries nipple play with", "has a threesome", "has a foursome with", "has a fivesome with", "gets bukkaked by", "tries rope play with", "tries water-sports with", "becomes a cuck-quean for", "sixty-nines", "gets choked by", "rims", "joins an orgy with", "gets gangbanged by", "tries a reverse gangbang with", "tries a double gangbang with", "gets double penetrated by", "gets triple penetrated by", "films a porno with", "tries BDSM with", "gets tied up by", "gets dominated by", "gets a Dirty Sanchez from", "gets hot-wifed to", "lets the guys in the gym watch her with", "walks naked through Times Square with", "gets her ass eaten by", "spreads her legs for", "spreads her cheeks for", "bends over for", "deep-throats", "gets tea-bagged by"]).GetWord() + " "
		sText += WordList(["a lumberjack", "a fireman", "a policeman", "a lifeguard", "a stunt man", "a bull rider", "a park ranger", "a fighter pilot", "a Chippendales dancer", "an astronaut", "a Navy SEAL", "a Green Beret", "a cowboy", "a guitar player", "an olympic gold medalist", "a pro surfer", "a private eye", "a paramedic", "a mechanic", "a biker", "a life drawing model", "a pirate captain", "a highwayman", "a troubador", "a Viking warrior"]).GetWord() 
		
		return sText
		
class TweetTxtGen17(TweetTxtGen):
	# This was a good read, but was the lesbian anal scene really necessary?
	ID = 17
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Delightful and provcative", "Good book", "I enjoyed this", "This was a good read", "Pretty good read", "Fun book", "A real page-turner"]).GetWord() + ", but was the "
		sText += WordList(["tentacle", "unicorn", "centaur", "man-o-taur", "gargoyle", "werewolf", "merman", "dwarf", "dragon", "orc", "troll", "goat-man", "futa", "alien", "tentacle monster", "clown", "sumo wrestler", "were-horse", "t-rex", "velociraptor", "dinosaur", "reverse merman", "cyborg", "were-shark", "gay", "lesbian", "dinosaur", "gargoyle", "lumberjack", "SWAT team", "construction worker", "male stripper", "cowboy", "MMA fighter"]).GetWord() + " "
		sText += WordList(["anal", "fisting", "toe-sucking", "nipple play", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "rope play", "water-sports", "cuck-queaning", "69", "choking", "orgy", "gangbang", "reverse gangbang", "double gangbang", "double penetration", "triple penetration", "porn", "BDSM", "bondage", "Dirty Sanchez", "hot-wifing", "water-sports", "enema", "rimming", "analingus", "glory hole", "fellatio", "deep throat", "cuckolding"]).GetWord() + " "
		sText += "scene really necessary?"
		
		return sText
		
class TweetTxtGen18(TweetTxtGen):
	# 'Delightful & provactive!' raves Dwarf Fisting Magazine 
	ID = 18
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "'" + WordList(["Delightful & provactive", "Thoughtful & heart-warming", "Heart-warming & transcendant", "Complex yet satisfying", "A real rollercoaster ride", "An emotional rollercoaster", "An edge-of-your-seat, stand-up-and-cheer page-turner", "Kept me literally glued to my Kindle", "Kept me literally nailed to my seat", "Un-put-downable", "A grand slam", "A home-run", "A modern classic"]).GetWord() + "!' "
		sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
		sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
		sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Choking", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 
			
		return sText
		
class TweetTxtGen19(TweetTxtGen):
	# 'Ben Dover's latest is a triumph!' applauds Goat-man Foursome Magazine 
	ID = 19
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "'" + AuthorBuilder() + "'s latest is " + WordList(['a triumph', 'a triumph', 'a massive success', 'a masterpiece', 'an erotic masterpiece', 'a modern classic', 'a sexual classic', 'brilliant', 'a work of genius', 'an unmatched success', 'the next Harry Potter', 'the next 50 Shades of Gray', 'the next Hunger Games', 'un-put-downable', 'heart-warming and satisfying', 'very readable']).GetWord() + "!' "
		sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
		sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
		sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Choking", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 

		
		return sText
		
class TweetTxtGen20(TweetTxtGen):
	# Reply to this tweet and I'll tweet a randomly-generated naughty ebook title @ you!
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Reply to this tweet and " 
		if CoinFlip():
			sText += "I'll tweet a " + WordList(["randomly", "computer", "bot", "algorithmically"]).GetWord () + "-generated " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title @ you!"
		else:
			sText += "get a custom " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title of your very own in reply! " + GetEmoji()
		sText += " " + GetEmoji()

		
		return sText
		
class TweetTxtGen21(TweetTxtGen):
	# Follow my sister bot @bot_lust to read naughty excerpts from this book (warning: NSFW!) ;-)
	ID = 21
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + WordList([" my sister bot", " my bot-sibbling", ""]).GetWord() + " @bot_lust " + WordList(["to read what's inside", "to read " + self.SexyAdj.GetWord() + " excerpts from", "to see what's inside", "to read " + SexyAdjs().GetWord() + " bot-generated love scenes from"]).GetWord() + " this book (warning: NSFW!) " + GetEmoji()
		
		return sText
		
class TweetTxtGen22(TweetTxtGen):
	# Features a beautiful interracial relationship between a stegosaur and a reverse merman
	ID = 22
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		Creatures = WordList(["Unicorn", "Centaur", "Man-o-taur", "Gargoyle", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-horse", "T-Rex", "Velociraptor", "Stegosaur", "Plesiosaur", "Pterodactyl", "Reverse Merman", "Cyborg", "Vampire", "Zombie", "Were-shark", "Demon", "Incubus"])
		sSpecies1 = Creatures.GetWord().lower()
		sSpecies2 = Creatures.GetWord(NotList = [sSpecies1]).lower()
		
		sText = "Features a " + WordList(['beautiful', 'tender', 'loving', 'sweet', 'touching', 'heartfelt', 'heart-warming']).GetWord() + " interracial relationship between a " + sSpecies1 + " and a " + sSpecies2 
		
		return sText
		
class TweetTxtGen23(TweetTxtGen):
	# The edging scene goes on for 97 pages
	ID = 23
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "The " + WordList(["anal", "double anal", "lesbian orgy", "reverse gangbang", "Dirty Sanchez", "fisting", "nipple play", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "rope play", "pee-drinking", "cuckolding", "69", "choking", "orgy", "gangbang", "double gangbang", "double penetration", "triple penetration", "BDSM", "bondage", "wife-swapping", "voyeurism", "water-sports", "public humiliation", "lactation", "age play", "mutual masturbation", "edging", "forced orgasm", "domination", "submission"]).GetWord() + " scene goes on for " + str(randint(3,119)) + " pages"
		
		return sText
		
class TweetTxtGen24(TweetTxtGen):
	# I had some trouble keeping the characters straight. Is Gary the blonde fireman with the 7" schlong or the brunette fireman with the 8" schlong?
	ID = 24
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "I had " + WordList(["a hard time", "some trouble", "a bit of a problem", "some difficulty"]).GetWord() + " keeping the characters straight. "
		if CoinFlip():
			sName = NamesFemale().FirstName()
			Lady = WordList(title.misc.TropesBadFemale().List + title.misc.TropesGoodFemale().List + title.misc.ProfFemale().List).GetWord().lower()
			iLength = WordList([32,34,36]).GetWord()
			sCupSize = WordList(['D', 'DD']).GetWord()
			BoobNames = WordList(['boobs', 'tits', 'gazongas', 'coconuts', 'melons', 'bazookas', 'hooters', 'tatas', 'jugs', 'rack', 'titties', 'cantalopes', 'grapefruits', 'pom-poms'])
			sBoobName = BoobNames.GetWord()
			
			sText += "Was " + sName + " the blonde " + Lady + " with the " + str(iLength) + sCupSize + " " + sBoobName + " or the brunette " + Lady + " with the " + str(iLength + 2) + sCupSize + "D " + sBoobName + "?"
		else:
			sName = NamesMale().FirstName()
			Dude = WordList(title.misc.SpeciesMale().List + title.misc.ProfMale().List + title.misc.TropesMale().List).GetWord().lower()
			iLength = randint (6, 12)
			PenisNames = WordList(['schlong', 'dick', 'bagpipe', 'rod', 'pole', 'willy', 'johnson', 'dingus', 'dong', 'package', 'prick', 'sausage', 'slim jim', 'stiffy', 'swizzle stick', 'tool', 'trouser snake', 'wiener'])
			sPenisName = PenisNames.GetWord()
			
			sText += "Was " + sName + " the blonde " + Dude + " with the " + str(iLength) + "\" " + sPenisName + " or the brunette " + Dude + " with the " + str(iLength + 1) + "\" " + sPenisName + "?"
		return sText
		
class TweetTxtGen25(TweetTxtGen):
	# Why don't I ever meet any horny, well-hung lumberjacks in real life?
	ID = 25
	Priority = 50
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Why don't I ever meet any " + WordList(["horny", "desperate", "lonely", "steamy", "single", "sensual", "bereft", "tragically widowed", "lustful", "sexually repressed", "loner", "bachelor", "naked"]).GetWord() + ", "
		sText += WordList(["sexy", "hot", "hunky", "handsome", "shirtless", "brawny", "virile", "clean-cut", "stylish", "suave", "alluring", "gruff", "chiseled", "strapping", "attractive", "erotic", "stunning", "well-hung", "well-endowed", "girthy", "hugely erect"]).GetWord() + " "
		sText += WordList(["lumberjacks", "firemen", "cops", "lifeguards", "stunt men", "bull riders", "park rangers", "pilots", "Chippendales dancers", "astronauts", "attorneys", "Navy SEALs", "Green Berets", "heart surgeons", "cowboys", "guitar players", "olympic gold medalists", "private eyes", "professional surfers", "private eyes"]).GetWord() + " in real life?"
		return sText
		
class TweetTxtGen26(TweetTxtGen):
	# Experts recommend wearing a condom while you read this book
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Experts", "Doctors", "Medical professionals", "Scientists", "Studies"]).GetWord() + " recommend " 
		sText += WordList(["wearing a condom", "using birth control", "using protection", "avoiding pregnancy", "that women remain on the pill", "not operating heavy machinery", "that men discontinue the use of Viagra or Cialis"]).GetWord() + " "
		sText += "while reading this book"
		
		return sText
		
class TweetTxtGen27(TweetTxtGen):
	# I mean, who among us hasn't had a secret affair with our curvaceous cheerleader step-daughter?
	ID = 27
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Really", "I mean", "Honestly", "Let's get real", "Seriously", "For real though"]).GetWord() + ", "
		sText += "who among us hasn't " + WordList(["had a secret affair with", "secretly impregnated", "started a secret family with", "had a secret baby with", "accidentally showered with", "mistaken our girlfriend for", "gotten drunk and gotten a handjob from", "gotten drunk and eaten the ass of", "masturbated in the dressing room with", "played doctor with", "helped fertilize the eggs of", "spooned naked with", "watched a porno with"]).GetWord() + " "
		sText += "our " + title.misc.PhysCharFemale().GetWord().lower() + " " + title.misc.ProfGoodFemale().GetWord().lower() + " "
		sText += WordList(["step-daughter", "step-mom", "step-sister", "cousin", "sister-in-law", "daughter-in-law", "aunt", "niece", "neighbor", "MILF", "teacher"]).GetWord() + "?"
		
		return sText

class TweetTxtGen28(TweetTxtGen):
	# Of course in real life you should never attempt centaur bukkake without strict medical supervision.
	ID = 28
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Of course in real life you should never attempt " 
		sText += WordList(["tentacle", "unicorn", "centaur", "man-o-taur", "gargoyle", "werewolf", "merman", "dwarf", "dragon", "orc", "troll", "goat-man", "futanari", "alien", "tentacle monster", "clown", "sumo wrestler", "were-horse", "t-rex", "velociraptor", "dinosaur", "reverse merman", "cyborg", "were-shark"]).GetWord() + " "
		sText += WordList(["anal", "double anal", "fisting", "nipple play", "incest", "twincest", "cum-swapping", "bukkake", "rope play", "pee-drinking", "cuckolding", "69", "choking", "double gangbang", "double penetration", "triple penetration", "BDSM", "bondage", "water-sports", "public humiliation", "lactation", "age play", "edging", "forced orgasm", "domination", "submission"]).GetWord() + " "
		sText += "without " + WordList(["strict medical supervision", "a note from your doctor", "waiting at least two hours after eating", "guidance from a trained professional", "help from a licensed dominatrix", "the buddy system", "regular checkups", "notifying the police", "an ambulance standing by", "a certified SCUBA instructor", "a friend that you can trust", "telling someone where you are", "paramedics on hand", "medical training", "power of attorney"]).GetWord()
		
		return sText

class TweetTxtGen29(TweetTxtGen):
	# I was hoping that Emily would hook up with Brad, but then SURPRISE! anal threesome with Jack!
	ID = 29
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sHerName = NamesFemale().FirstName()
		sHisName = NamesMale().FirstName()
		sTheirName = ""
		
		if CoinFlip():
			sTheirName = NamesFemale().FirstName()
		else:
			sTheirName = NamesMale().FirstName()
			
		sText = "I was rooting for " + sHerName + " " 
		sText += WordList(["to hook up with", "to get with", "to get together with", "to wind up with"]).GetWord() + " "
		sText += sHisName + ", but then " 
		sText += WordList(["SURPISE!", "nope, boom!", "watch out!", "*WOW!*", "nuh uh!", "guess what?", "*oh snap!!*", "PLOT TWIST!", "what the fuck??", "*SHOCKER!*"]).GetWord() + " "
		sText += WordList(["she does anal", "she does lesbian anal", "anal threesome", "fisting", "toe sucking", "she tries nipple play", "it's a threesome", "it's a foursome", "it's a fucking fivesome", "bukkake", "rope play", "she tries water-sports", "she becomes a cuck-quean", "she sixty-nines", "she gets choked", "she does rimming", "she joins an orgy", "gangbang", "reverse gangbang", "she does a double gangbang", "double penetration", "triple penetration", "she films a porno", "she does bondage", "a Dirty Sanchez", "hot-wifing", "she lets the guys in the gym watch her", "she walks naked through Times Square", "she gets her ass eaten", "analingus", "she spreads her legs", "a footjob"]).GetWord() + " with "
		if CoinFlip():
			sText += sTheirName + "!!"
		else:
			sText += "a " + WordList(["Unicorn", "Centaur", "Man-o-taur", "Gargoyle", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-horse", "T-Rex", "Velociraptor", "Stegosaur", "Plesiosaur", "Pterodactyl", "Reverse Merman", "Cyborg", "Vampire", "Zombie", "Were-shark", "Demon", "Incubus"]).GetWord().lower() + "!!"
		
		return sText

class TweetTxtGen30(TweetTxtGen):
	# I was stunned when it was revealed that Jack the handsome Cowboy was actually a gazillionaire!
	ID = 30
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sHisName = NamesMale().FirstName()
		
		sText = "I was " + WordList(["stunned", "shocked", "flabbergasted", "floored", "blown away", "so surprised"]).GetWord() + " when it was revealed that "
		sText += sHisName + " the " + WordList(["sexy", "hot", "hunky", "handsome", "shirtless", "brawny", "virile", "clean-cut", "stylish", "suave", "smooth-talking", "gruff", "chiseled", "strapping", "attractive", "erotic", "stunning", "well-hung", "well-endowed", "girthy", "gentlemanly", "charming", "blonde", "brunette", "redheaded", "taciturn", "rakish", "heart-throb", "beefcake", "tattooed", "bearded"]).GetWord() + " " 
		sText += WordList(["lumberjack", "fireman", "policeman", "lifeguard", "stunt man", "bull rider", "park ranger", "pilot", "Chippendales dancer", "astronaut", "Navy SEAL", "Green Beret", "cowboy", "guitar player", "olympic gold medalist", "pro surfer", "private eye", "paramedic", "mechanic", "biker", "life drawing model", "pirate captain", "highwayman", "troubador", "Viking warrior", "family man"]).GetWord() + " "
		sText += "was " + WordList(["really", "actually", "in fact"]).GetWord() + " a " + WordList(["millionaire", "multi-millionaire", "billionaire", "trillionaire", "gazillionaire", "king", "prince", "duke", "marquis", "manor lord", "sheikh", "pope", "crown prince", "CEO"]).GetWord() + "!"
		
		return sText

class TweetTxtGen31(TweetTxtGen):
	# ME YELLING AT THE MAIN CHARACTER: No Emily! You can't sleep with Jack! He's your long-lost twin brother!
	ID = 31
	Priority = 5
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sHerName = NamesFemale().FirstName()
		sHisName = NamesMale().FirstName()
		
		sHerName2 = NamesFemale().FirstName()
		sHisName2 = NamesMale().FirstName()
		
		sText = "ME, " + WordList(["YELLING", "YELLING", "SCREAMING"]).GetWord() + " AT THE " + WordList(["BOOK", "BOOK", "PAGE", "MAIN CHARACTER"]).GetWord() + ": No " + sHerName + "! You can't " + WordList(["sleep with", "sleep with", "have sex with", "hook up with"]).GetWord () + " " + sHisName + "! "
		sText += "He " + WordList(["is your long lost twin brother", 
									"is secretly married to " + sHerName2, 
									"used to be a woman named " + sHerName2, 
									"is the serial killer that's been terrorizing " + WordList(["Tulsa", "Tuscaloosa", "Scranton", "Hull", "Livepool", "Huddersfield", "Jacksonville", "Plano", "Fort Wayne", "Calgary"]).GetWord(),
									"just wants you for your " + WordList(["millions", "billions", "bitcoin", "successful fondue restaurant", "enormous titties"]).GetWord(), 
									"is the brother your parents hid from you", 
									"has a secret family with " + sHerName2, 
									"is the mysterious man in black that shot your father",
									"is an imposter named " + sHisName2 + " and he's really from " + WordList(["Alabama", "Hull", "Essex", "Sussex", "Florida", "Arkansas", "Scranton", "Northampton", "Jacksonville", "Liverpool", "Plano", "Cardiff", "New Jersey"]).GetWord(),
									"is your brother whom you forgot about due to your amnesia",
									"is secretly a " + WordList(["werewolf", "were-horse", "were-shark", "were-gorilla", "were-dinosaur"]).GetWord(),
									"is being mind-controlled by Majestic 12",
									"is an evil clone",
									"is the father you've never met",
									"is a hitman for the " + WordList(["Italian", "Irish", "Russian", "French", "Canadian", "French-Canadian", "Sicilian", "Japanese", "Hawaiian", "Belgian"]).GetWord() + " mafia",
									"has a secret prosthetic " + WordList(["nose", "nose", "ear", "nipple", "ass", "penis", "dick", "cock"]).GetWord(),
									"is secretly from " + WordList(["Alabama", "Canada", "Essex", "Sussex", "Florida", "Arkansas", "Scranton", "Northampton", "Cardiff", "New Jersey"]).GetWord(),
									"is in love with " + sHerName2,
									"is in love with " + sHisName2,
									"is blackmailing your " + WordList(["brother", "dad", "mom", "step-brother", "sister", "sister-in-law", "step-dad"]).GetWord(),
									"has no sense of smell"]).GetWord() + "!"
		
		return sText

class TweetTxtGen32(TweetTxtGen):
	# Ben Dover is definitely the best erotica author working in Tuscaloosa!
	ID = 32
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sAuthor = AuthorBuilder()
		sSuper = WordList(["best", "premier", "finest", "#1"]).GetWord()
		sType = WordList(["erotica", "erotica", "smut", "erotic romance", "naughty romance", "adult romance", "adult erotic romance", "fetish-friendly romance", "kink-friendly erotica", "erotic space opera", "erotic detective fiction", "kink-friendly LitRPG", "lesbian cozy mystery", "fetish cozy mystery", "erotic cookbook"]).GetWord()
		
		sPlace = ""
		if CoinFlip():
			sPlace += "in " 
			if CoinFlip():
				sPlace += WordList(["north", "south", "east", "west"]).GetWord() + " "
			sPlace += WordList(["Tulsa", "Tuscaloosa", "Scranton", "Hull", "Huddersfield", "Jacksonville", "Plano", "Fort Wayne", "Calgary", "Liverpool", "Northampton", "Sussex", "Essex", "Cardiff"]).GetWord()
		else:
			sPlace += "from " 
			if CoinFlip():
				sPlace += WordList(["north", "south", "east", "west"]).GetWord() + " "
			sPlace += WordList(["Alabama", "Arkansas", "Canada", "Liverpool", "Northampton", "Sussex", "Essex", "New Jersey", "Florida", "West Virginia"]).GetWord()
			
		sText = WordList(["There's no question that " + sAuthor + " is the ",
						  sAuthor + " is absolutely the ",
						  "There's no doubt in my mind that " + sAuthor + " is the ",
						  "There can be no debate that " + sAuthor + " is the ",
						  "No one can deny that " + sAuthor + " is the "]).GetWord()
		sText += sSuper + " " + sType + " writer " + sPlace
		
		return sText

class TweetTxtGen33(TweetTxtGen):
	# "A wild fuckfest!" -Abraham Lincoln
	ID = 33
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		Adjs = WordList(["thrilling", "wild", "sensual", "perverted", "raunchy", "tasteless", "lascivious", "erotic", "horny", "delightful", "sinful", "arousing", "naughty", "depraved", "lustful", "wicked", "outrageous", "delicious", "stimulating", "sexy", "provocative"])
		Celebs = WordList(["Abraham Lincoln", "Winston Churchill", "Barak Obama", "Mother Theresa", "Martin Luther King, Jr.", "Nelson Mandela", "Salman Rushdie", "Albert Einstein", "Hillary Clinton", "Maya Angelou", "Isaac Asimov", "Jonathan Franzen", "Cormac McCarthy", "Ghandi", "Boutros Boutros-Ghali", "Bob Dylan", "The Dalai Lama"])
		
		if CoinFlip():
			sAdj1 = Adjs.GetWord()
			sAdj2 = Adjs.GetWord(NotList = [sAdj1])
			sText = "\"" + sAdj1.title() + " and " + sAdj2 + "!\"\n"
		elif CoinFlip():
			sAdj = Adjs.GetWord()
			if sAdj[0] in ('a','e','i','o','u'):
				sText = "\"An " + sAdj + " fuckfest!\"\n"
			else: 
				sText = "\"A " + sAdj + " fuckfest!\"\n"
		elif CoinFlip():
			sAdj = Adjs.GetWord()
			sText = "\"" + sAdj.title() + " AF!\"\n"
		elif CoinFlip():
			sText = "\"I'm so horny for this!\"\n" 
		elif CoinFlip():
			sText = "\"I got off on this!\"\n" 
		else:
			sText = "\"What the fuck did I just read??\"\n" 
			
		sText += " ~" + Celebs.GetWord()
		
		return sText

# class TweetTxtGen34(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 34
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText

# class TweetTxtGen35(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 35
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText

# class TweetTxtGen36(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 36
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText		

class TweetTxtGenSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in TweetTxtGen.__subclasses__():
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
					

		
def GetImgTweetText(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetTxtHistoryQ = None):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	Generator = None
	GenType = None 
	HistoryQ = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	# print("GetImgTweetText() Generator Type is " + str(GenType))
	# print("GetImgTweetText() Generator # is " + str(iGeneratorNo))
	
	if not TweetTxtHistoryQ is None:
		HistoryQ = TweetTxtHistoryQ
	
	GenSel = TweetTxtGenSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
		while not HistoryQ.PushToHistoryQ(gen.ID):
			gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
	
	if not gen is None:
		sText = gen.GenerateTweet()
	else:
		print("Generator not found.")
		sText = ""

	# bots using hashtags can lead to shadowbans. so we have to use sparingly.
	if randint(1,5) == 5:
		sText += " #" + Hashtags().GetWord()
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	# else:
		# sText = TweetText[randint(0, len(TweetText) - 1)] 
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] 
	
	return sText 
	
