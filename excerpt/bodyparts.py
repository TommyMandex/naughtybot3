#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from random import *
from util import *


class BodyParts:
	def __init__(self):
		self._NounList = WordList([])
		self._AdjList = WordList([])
		self._ColorList = WordList([])
		self._DefaultNoun = ""
		self._DefaultAdj = "naked"
		
		self.NounHistoryQ = HistoryQ(3)
		self.AdjHistoryQ = HistoryQ(3)
		
	def NounList(self, NewNounList = None):
		if NewNounList == None:
			SetNounList = []
		else:
			SetNounList = NewNounList 
			
		self._NounList = WordList(SetNounList)
		
	def AdjList(self, NewAdjList = None):
		if NewAdjList == None:
			SetAdjList = []
		else:
			SetAdjList = NewAdjList
			
		self._AdjList = WordList(SetAdjList)
		
	def ColorList(self, NewColorList = None):
		if NewColorList == None:
			SetColorList = []
		else:
			SetColorList = NewColorList
			
		self._ColorList = WordList(SetColorList)
		
	def DefaultNoun(self, NewNoun = None):
		if NewNoun == None:
			NewNoun = ""
			
		self._DefaultNoun = NewNoun 
	
	def DefaultAdj(self, NewAdj = None):
		if NewAdj == None:
			NewAdj = ""
			
		self._DefaultAdj = NewAdj 
		
	def GetDefaultNoun(self, NotList = None):
		sDefaultNoun = ""
		
		if NotList == None:
			NotList = []

		if self._DefaultNoun not in NotList:
			sDefaultNoun = self._DefaultNoun
			
		return sDefaultNoun
		
	def GetDefaultAdj(self, NotList = None):
		sDefaultAdj = ""
		
		if NotList == None:
			NotList = []

		if self._DefaultAdj not in NotList:
			sDefaultAdj = self._DefaultAdj
			
		return sDefaultAdj
	
	def GetNoun(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._NounList.GetWord(sNot = sNot, NotList = NotList)
	
	def GetAdj(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._AdjList.GetWord(sNot = sNot, NotList = NotList)
		
	def GetColor(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._ColorList.GetWord(sNot = sNot, NotList = NotList)
		
	def GetNounList(self):
		return self._NounList.List 
		
	def GetAdjList(self):
		return self._AdjList.List
		
	def GetColorList(self):
		return self._ColorList.List
		
	def HasColors(self):
		bHasColors = False 
		
		if len(self._ColorList.List) > 0:
			bHasColors = True
			
		return bHasColors

	#noun only ("hair")
	def ShortDescription(self, sNot = "", NotList = None):
		#print("ShortDesc sNot = " + str(sNot))
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		return self.GetNoun(sNot = sNot, NotList = NotList)
	
	#adjective noun ("red hair")
	def MediumDescription(self, sNot = "", NotList = None):
		sMediumDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if self.HasColors() and CoinFlip():
			sMediumDesc = self.GetColor(sNot = sNot, NotList = NotList)
		else:
			sMediumDesc = self.GetAdj(sNot = sNot, NotList = NotList)
		sMediumDesc += " " + self.GetNoun(sNot = sNot, NotList = NotList)
			
		return sMediumDesc
	
	#adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
	def FloweryDescription(self, sNot = "", NotList = None):
		sFloweryDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		iNumAdjs = randint(1, 3)
		
		sAdj1 = ""
		sAdj2 = ""
			
		if iNumAdjs == 3:
			sAdj1 = self.GetAdj(sNot = sNot, NotList = NotList)
			sAdj2 = self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1])
			sAdj3 = ""
			if self.HasColors():
				sAdj3 += self.GetColor(sNot = sNot, NotList = NotList + [sAdj1,sAdj2])
			else:
				sAdj3 += self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1,sAdj2])
			sFloweryDesc += sAdj1 + ", " + sAdj2 + ", " + sAdj3
		elif iNumAdjs == 2:
			sAdj1 += self.GetAdj(sNot = sNot, NotList = NotList) 
			if self.HasColors():
				sAdj2 += self.GetColor(sNot = sNot, NotList = NotList + [sAdj1])
			else: 
				sAdj2 += self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1]) 
			sFloweryDesc += sAdj1 + ", " + self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1])
		else:
			if self.HasColors() and CoinFlip():
				sFloweryDesc += self.GetColor(sNot = sNot, NotList = NotList)
			else:
				sFloweryDesc += self.GetAdj(sNot = sNot, NotList = NotList)
				
		sFloweryDesc += " " + self.GetNoun(sNot = sNot, NotList = NotList)
			
		return sFloweryDesc
	
	def RandomDescription(self, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True):
		sRandomDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		iRand = randint(0, 12)
		
		if iRand in range(0, 3):
		#short desc if allowed 
			if bAllowShortDesc:
				#use noun from the list or default noun
				if CoinFlip():
					sRandomDesc = self.ShortDescription(sNot = sNot, NotList = NotList)
				else:
					sRandomDesc = self.GetDefaultNoun(NotList = NotList)
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
		elif iRand in range(3,6):
		#medium desc 
			sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
		else:
		#flowery desc if allowed
			if bAllowLongDesc:
				sRandomDesc = self.FloweryDescription(sNot = sNot, NotList = NotList)
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
			
		return sRandomDesc

class Face(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['face',
			'face',
			'face',
			'features'])
		
		self.AdjList(['adorable',
			'angelic',
			'beaming',
			'beautiful',
			'cute',
			'delicate',
			'elegant',
			'excited',
			'gentle',
			'gorgeous',
			'flushed',
			'freckled',
			'heart-shaped',
			'innocent',
			'lovely',
			'oval',
			'pale',
			'pretty',
			'radiant',
			'rosy',
			'round',
			# 'sculpted',
			'smiling',
			'startled',
			# 'surprised',
			'sweet',
			'warm',
			'wide-eyed'])
			
		self.DefaultNoun('face')
		
class Skin(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['skin','skin','skin','skin',
			'flesh'])
			
		self.ColorList(['almond-colored',
						'brown',
						'bronzed',
						'chocolate',
						'chocolate-colored',
						'coffee-colored',
						'dark',
						'fresh pink',
						'honeyed',
						'pale',
						'pink',
						'porcelain',
						'sun-browned',
						'sun-kissed'])
		self.AdjList([
			'bare',
			'delicate',
			'exposed',
			'freckled',
			'gentle',
			'gleaming',
			'glistening',
			'glowing',
			'gossamer',
			'luscious',
			'naked',
			'perfect',
			'silken',
			'soft',
			'smooth',
			'supple',
			'sweet',
			'tender',
			'un-blemished',
			'un-sullied',
			'warm',
			'yielding',
			'youthful'])
		
		self.DefaultNoun('skin')
		self.IsPlural = False
		
class Mouth(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['mouth',
						 'mouth',
						 'mouth',
						 'mouth',
						 'mouth-hole'])
			
		self.AdjList(['eager',
			'greedy',
			'hungry',
			'insatiable',
			'insolent',
			'lewd',
			'open',
			'wanting',
			'willing'])
		
		self.DefaultNoun("mouth")
		self.DefaultAdj("insatiable")
		self.IsPlural = False
		
class Lips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['lips'])
			
		self.AdjList(['collagen-injected',
			'full',
			'inviting',
			'insolent',
			'luscious',
			'sensual',
			'sweet'])
			
		self.ColorList(['candy-colored',
						'red','red',
						'rose-colored',
						'rouge',
						'painted black'
					  ])
		
		self.DefaultNoun("lips")
		self.DefaultAdj("full")
		
class Eyes(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['eyes'])
			
		self.AdjList(['alluring',
			'beautiful',
			'bewitching',
			'brown',
			'captivating',
			'dark',
			'dazzling',
			'earnest',
			'electric',
			'electrifying',
			'enchanting',
			'mischievous',
			'soulful',
			'sweet'])
			
		self.AdjList(['blue','blue',
					  'brown',
					  'gray',
					  'green',
					  'hazel'])
		
		self.DefaultNoun("eyes")
		self.DefaultAdj("bewitching")
		
class Hips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['hips'])
			
		self.AdjList(['curvy',
			'curvaceous',
			'bare',
			'fertile',
			'rounded',
			'sensual',
			'shapely',
			'slinky',
			'sultry',
			'tantalizing',
			'voluptuous',
			'wanton',
			'wide',
			'womanly'])
		
		self.DefaultNoun("hips")
		
class Hair(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['hair',
			'hair',
			'hair',
			'locks'])
			
		self.AdjList(['curly',
			'glossy',
			'long',
			'luxuriant',
			'silken',
			'short',
			'vibrant',
			'wavy'])
			
		self.ColorList(['black','black',
						'blonde','blonde',
						'blue-dyed',
						'brunette',
						'dark',
						'dyed green',
						'flaming-red',
						'golden',
						'kinky black-girl',
						'platinum blonde',
						'punk blue',
						'sandy',
						'red'])
						
		
		self.DefaultNoun("hair")
		self.DefaultAdj("flowing")
		
class Legs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['legs'])
			
		self.AdjList(['athletic',
			'coltish',
			'elegant',
			'graceful',
			'lithe',
			'limber',
			'lissome',
			'lithesome',
			'long','long',
			'long, sexy',
			'toned',
			'sexy',
			'shapely',
			'shaved',
			'smooth',
			'smooth-shaven'])
		
		self.DefaultNoun("legs")
		
class Thighs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['thighs'])
			
		self.AdjList(['bare',
			'bronzed',
			'chubby',
			'comely',
			'delectable',
			'full',
			'girlish',
			'heavy',
			'inviting',
			'luscious',
			'nubile',
			'pale',
			'powerful',
			'porcelain',
			'ripe',
			'rounded',
			'sensual',
			'sexy',
			'shapely',
			'silken',
			'smooth',
			'soft',
			'tanned',
			'tender',
			'thick','thick',
			'un-sullied',
			'wide',
			'womanly',
			'youthful'])
		
		self.DefaultNoun("thighs")
		
class Nipples(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['nipples',
			'nipples',
			'nipples',
			'nips',
			'teats'])
			
		self.AdjList(['blossoming',
			'budding',
			'dainty',
			'enormous',
			'erect',
			'exposed',
			'inch-long',
			'long',
			'luscious',
			'petite',
			'pert',
			'pokey',
			'puffy',
			'ripe',
			'sensitive',
			'shameless',
			'stiff',
			'succulent',
			'suckable',
			'swollen',
			'tasty',
			'tender',
			'tiny',
			'wide'])
			
		self.ColorList(['chocolate',
						'dark',
						'pink',
						'rosebud',
						'rose-colored'
						])
		
		self.DefaultNoun("nipples")
		self.DefaultAdj("erect")
		
class Breasts(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Nipples = []
		
		self.NounList(['boobies',
			'boobs',
			'bosoms',
			'bosoms',
			'breasts',
			'breasts',
			'breasts',
			'breasts',
			'buds',
			'bust',
			'coconuts',
			'dumplings',
			'gazongas',
			'globes',
			'jugs',
			'knockers',
			'mammaries',
			'melons',
			'orbs',
			'teats',
			'tits',
			'tits',
			'titties'])
			
		self.AdjList(['bouncy',
			'bountiful',
			'budding',
			'buxom',
			'delicious',
			'double-D',
			'full',
			'fulsome',
			'generous',
			'gentle',
			'girlish',
			'glorious',
			'gorgeous',
			'heaving',
			'heavy',
			'impressive',
			'jiggling',
			'juicy',
			'luscious',
			'lush',
			'luxuriant',
			'magnificent',
			'nubile',
			'pale',
			'pendulous',
			'perky',
			'pert',
			'petite',
			'plump',
			'proud',
			'quivering',
			'ripe',
			'round',
			'sensual',
			'shapely',
			'smooth',
			'soft',
			'statuesque',
			'stunning',
			'succulent',
			'sumptuous',
			'supple',
			'surgically-enhanced',
			'swaying',
			'sweet',
			'swollen',
			'tender',
			'voluptuous'])
		
		self.DefaultNoun("breasts")
		self.Nipples = Nipples() 
		
class Clitoris(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['clit',
			'clit',
			'clitoris',
			'clitoris',
			'love-button',
			'love-nub',
			'magic button',
			'nub',
			'pearl'])
			
		self.AdjList(['delicate',
			'engorged',
			'engorged',
			'erect',
			'exposed',
			'fevered',
			'pink',
			'pulsating',
			'pulsing',
			'secret',
			'sensitive',
			'shy little',
			'swollen',
			'tender',
			'throbbing',
			'tingling'])
		
		self.DefaultNoun("clit")
		self.IsPlural = False

class VaginaInner(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['cherry',
				'cleft',
				'chamber',
				'chasm',
				'cock-sock',
				'cunt-hole',
				'fuck-tunnel',
				'fuckhole',
				'furrow',
				'gash',
				'hole',
				'honey hole',
				'honeypot',
				'keyhole',
				'love-channel',
				'love-tunnel',
				'passage',
				'slit',
				'tunnel',
				'vagina',
				'vaginal canal',
				'vestibule',
				'womanhood'])
				
		self.AdjList(['cherry',
				'cherry red',
				'clenched',
				'deep',
				'deep',
				'dripping',
				'glazed',
				'gushing',
				'hungry',
				'juicy',
				'lewd',
				'lustful',
				'pink',
				'pink',
				'pink',
				'secret',
				'silken',
				'slick',
				'slick',
				'snug',
				'sopping',
				'spread',
				'succulent',
				'sweet',
				'tender',
				'tight',
				'velvet',
				'velvet',
				'wanton',
				'well-used'])
			
		self.DefaultNoun("vaginal canal")
		self.IsPlural = False
	
class VaginaOuterLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['labia',
							 'lips',
							 'mons pubis',
							 'mound',
							 'nether lips',
							 'outer labia',
							 'outer pussy lips',
							 'pussy lips',
							 'vulva'])
		self.AdjList(['bare',
							'dewy',
							'downy',
							'down-thatched',
							'dripping',
							'fat',
							'fat',
							'flushed',
							'fur-lined',
							'girlish',
							'gleaming wet',
							'glistening',
							'hairless',
							'honeyed',
							'juicy',
							'lickable',
							'luscious',
							'lush',
							'moist',
							'naked',
							'peach-fuzzed',
							'pink',
							'plump',
							'puffy',
							'shameless',
							'shaved',
							'shaven',
							'silken',
							'slick',
							'smooth',
							'succulent',
							'suckable',
							'supple',
							'sweet',
							'swollen',
							'tender',
							'trim',
							'wet'])
			
		self.DefaultNoun("mons pubis")

class VaginaInnerLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['beef-curtains',
							 'butterfly wings',
							 'cunt-lips',
							 'cunt-flaps',
							 'flaps',
							 'flower petals',
							 'folds',
							 'fringe',
							 'inner labia',
							 'labia',
							 'lips',
							 'meat curtains',
							 'meat-flaps',
							 'nether-lips',
							 'petals',
							 'piss-flaps',
							 'pussy-flaps',
							 'pussy lips',
							 'sex flaps',
							 'sex-lips',
							 'wizard sleeve'])
		self.AdjList(['beefy',
							'chewy',
							'dangling',
							'dark',
							'delicate',
							'dewy',
							'dewy',
							'dripping',
							'drooping',
							'droopy',
							'gleaming wet',
							'glistening',
							'gossamer',
							'honeyed',
							'juicy',
							'lickable',
							'little',
							'long',
							'lush',
							'meaty',
							'moist',
							'pink',
							'purple',
							'ruffled',
							'secret',
							'shameless',
							'silken',
							'shy',
							'sticky',
							'sticky',
							'succulent',
							'suckable',
							'tender',
							'trim',
							'velvet'])
		self.DefaultNoun("inner labia")
			
class Vagina(BodyParts):
	InnerVag = []
	InnerLabia = []
	OuterLabia = []
	Clitoris = []
	
	def __init__(self):
		super().__init__()
		
		self.NounList(['cherry pie',
					'cock-sock',
					'cooch',
					'coochie',
					'cunny',
					'cunt',
					'cunt-hole',
					'flower',
					'fuckhole',
					'fur-burger',
					'honey-hole',
					'honeypot',
					'love-muffin',
					'muff',
					'muffin',
					'peach',
					'pie',
					'pussy',
					'quim',
					'sex',
					'snatch',
					'twat',
					'vagina',
					'womanhood'])
					   
		self.AdjList(['bare',
					'cherry',
					'clenched',
					'delightful',
					'dewy',
					'down-thatched',
					'dripping',
					'exposed',
					'fuckable',
					'fur-lined',
					'girlish',
					'gleaming wet',
					'glistening',
					'gushing',
					'hairless',
					'honeyed',
					'horny',
					'hungry',
					'juicy',
					'leaky',
					'lewd',
					'lickable',
					'luscious',
					'lush',
					'lustful',
					'moist',
					'naked',
					'peach-fuzzed',
					'pink',
					'pink',
					'puffy',
					'shameless',
					'silken',
					'slick',
					'smooth',
					'sopping',
					'succulent',
					'suckable',
					'supple',
					'sweet',
					'swollen',
					'tender',
					'tight',
					'trim',
					'unsullied',
					'velvet',
					'wanton',
					'well-used',
					'willing'])
		
		self.DefaultNoun("vagina")
		self.IsPlural = False
		self.InnerVag = VaginaInner()
		self.OuterLabia = VaginaOuterLabia()
		self.InnerLabia = VaginaInnerLabia()
		self.Clitoris = Clitoris()


class AnusFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['anus',
			'anus',
			'anus',
			'arse-cunt',
			'asshole',
			'back orifice',
			'back passage',
			'backdoor',
			'bowels',
			'bunghole',
			'butthole',
			'butt hole',
			'corn hole',
			'dirt-pipe',
			'fart blaster',
			'heinie hole',
			'knot',
			'poop-chute',
			'poop-trap',
			'pooper',
			'rear orifice',
			'rectum',
			'rosebud',
			'sphincter',
			'sphincter',
			'starfish',
			'starfish'])
			
		self.AdjList(['clenched',
			'forbidden',
			'fuckable',
			'gaping',
			'knotted',
			'lewd',
			'little',
			'loose',
			'nasty',
			'naughty',
			'pert',
			'puckered',
			'shy',
			'smooth',
			'snug',
			'taboo',
			'tender',
			'tight',
			'wanton',
			'well-used',
			'willing',
			'winking'])
		
		self.DefaultNoun("anus")
		self.IsPlural = False
		
class AssFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Anus = AnusFemale()
		
		self.NounList(['ass',
			'backside',
			'behind',
			'booty',
			'bottom',
			'bum',
			'buns',
			'butt',
			'buttocks',
			'cheeks',
			'heinie',
			'rump',
			'tush',
			'tushy'])
			
		self.AdjList(['ample',
			'bountiful',
			'broad',
			'bubble-shaped',
			'chubby',
			'curvaceous',
			'curvy',
			'fuckable',
			'generous',
			'glistening',
			'honeyed',
			'juicy',
			'lush',
			'luscious',
			'nubile',
			'pert',
			'plump',
			'ripe',
			'rosy',
			'rotund',
			'round',
			'shameless',
			'shapely',
			'smooth',
			'succulent',
			'supple',
			'sweet',
			'tender',
			'thick',
			'trim',
			'voluptuous',
			'womanly'])
		
		self.DefaultNoun("ass")
		
class BodyFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['anatomy',
			'body',
			'body',
			'body',
			'body',
			'curves',
			'figure',
			'form',
			'physique'])
			
		self.AdjList(['beautiful',
			'busty',
			'buxom',
			'curvaceous',
			'curvy',
			'feminine',
			'gorgeous',
			'leggy',
			'little',
			'lush',
			'luxuriant',
			'model-esque',
			'nubile',
			'pale',
			'ravishing',
			'ripe',
			'sensual',
			'sexy',
			'shameless',
			'shapely',
			'slender',
			'statuesque',
			'stunning',
			'sultry',
			'sweet',
			'teenage',
			'tight',
			'voluptuous',
			'womanly',
			'young',
			'youthful'])
			
		self.ColorList(['black',
						'brown',
						'coffee-colored',
						'mocha',
						'pale',
						'pink',
						'tanned'
					   ])
		
		self.DefaultNoun("body")
		self.DefaultAdj("nubile")
		self.IsPlural = False
		self.Hair = Hair()
		self.Face = Face()
		self.Eyes = Eyes()
		self.Lips = Lips()
		self.Mouth = Mouth()
		self.Hips = Hips()
		self.Legs = Legs()
		self.Skin = Skin()
		self.Thighs = Thighs()
		self.Breasts = Breasts()
		self.Vagina = Vagina()
		self.Ass = AssFemale()
		
	# woman random body parts used by gen 8 (one instance), 18,21,31,38,60,72
	# man random body parts used by gen 19, 20, 22,38
	
	def GetClothedBodyPartDesc(self, part, bAllowLongDesc):
		sPartDesc = ""
		
		PartNotList = ['naked','nude','bare','exposed']
		bAddArticles = True
		
		if isinstance(part, Skin):
			PartNotList.append(['warm','tender'])
			bAddArticles = False 
		elif isinstance(part, Hair): 
			bAddArticles = False 
		elif isinstance(part, Eyes):
			bAddArticles = False 
		elif isinstance(part, Mouth):
			bAddArticles = True 
			PartNotList.append(['mouth-hole','lewd','insatiable','willing'])
		elif isinstance(part, Lips):
			bAddArticles = False 
		elif isinstance(part, Hips):
			bAddArticles = False 
		elif isinstance(part, Legs):
			bAddArticles = False 
		
		sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		if bAddArticles:
			sPartDesc = AddArticles(sPartDesc)
		
		return sPartDesc
	
	def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True):
		sBodyDesc = ""
		
		if iNum < 3:
			iNum = 3
		if iNum > 5:
			iNum = 5
			
		hair = self.Hair
		face = self.Face 
		eyes = self.Eyes 
		if CoinFlip():
			mouth = self.Lips 
		else:
			mouth = self.Mouth 
		hips = self.Hips 
		legs = self.Legs 
		skin = self.Skin
		thighs = self.Thighs 
		boobs = self.Breasts 
		pussy = self.Vagina 
		innerlabia = self.Vagina.InnerLabia
		outerlabia = self.Vagina.OuterLabia
		cunthole = self.Vagina.InnerVag 
		ass = self.Ass 
		asshole = self.Ass.Anus 
		body = self
		
		PartPriorities = [[hair,1],
						  [eyes,2],
						  [face,3],
						  [mouth,4],
						  [legs,5],
						  [hips,5],
						  [skin,6],
						  [body,6]]
		
		PartGroups = []
		
		if iNum == 3:
			for part1 in PartPriorities: #skin 6
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] == part1[1] and not part2[0] == part1[0]:
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								PartGroups.append([part1[0],part2[0],part3[0]])
					
			# PartGroups.append([hair,eyes,face])
			# PartGroups.append([hair,eyes,mouth])
			# PartGroups.append([hair,eyes,body])
			# PartGroups.append([hair,face,eyes])
			# PartGroups.append([hair,face,mouth])
			# PartGroups.append([hair,face,body])
			# PartGroups.append([hair,mouth,legs])
			# PartGroups.append([hair,mouth,hips])
			# PartGroups.append([hair,mouth,legs])
			# PartGroups.append([hair,mouth,skin])
			# PartGroups.append([hair,mouth,body])
			# PartGroups.append([eyes,face,mouth])
			# PartGroups.append([eyes,face,hips])
			# PartGroups.append([eyes,face,legs])
			# PartGroups.append([eyes,face,skin])
			# PartGroups.append([eyes,face,body])
			# PartGroups.append([face,eyes,mouth])
			# PartGroups.append([face,eyes,hips])
			# PartGroups.append([face,eyes,legs])
			# PartGroups.append([face,eyes,skin])
			# PartGroups.append([face,eyes,body])
			# PartGroups.append([face,eyes,mouth])
			# PartGroups.append([face,eyes,mouth])
			# PartGroups.append([skin,hips,legs])
			# PartGroups.append([skin,legs,hips])
			# PartGroups.append([skin,hips,body])
			# PartGroups.append([skin,legs,body])
			# PartGroups.append([body,legs,hips])
			# PartGroups.append([body,legs,skin])
			# PartGroups.append([body,hips,legs])
			# PartGroups.append([body,hips,skin])
			# PartGroups.append([body,hair,eyes])
			# PartGroups.append([body,hair,mouth])
			# PartGroups.append([body,eyes,hair])
			# PartGroups.append([body,eyes,mouth])
		elif iNum == 4:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
			# PartGroups.append([hair,eyes,face,mouth])
			# PartGroups.append([hair,eyes,face,hips])
			# PartGroups.append([hair,eyes,face,legs])
			# PartGroups.append([hair,eyes,face,skin])
			# PartGroups.append([hair,eyes,face,body])
			# PartGroups.append([hair,eyes,mouth,hips])
			# PartGroups.append([hair,eyes,mouth,legs])
			# PartGroups.append([hair,eyes,mouth,skin])
			# PartGroups.append([hair,eyes,mouth,body])
			# PartGroups.append([hair,face,eyes,mouth])
			# PartGroups.append([hair,face,eyes,hips])
			# PartGroups.append([hair,face,eyes,legs])
			# PartGroups.append([hair,face,eyes,mouth])
			# PartGroups.append([hair,face,eyes,skin])
			# PartGroups.append([hair,face,mouth,hips])
			# PartGroups.append([hair,face,mouth,legs])
			# PartGroups.append([hair,face,mouth,skin])
			# PartGroups.append([hair,mouth,legs,hips])
			# PartGroups.append([hair,mouth,legs,skin])
			# PartGroups.append([hair,mouth,hips,legs])
			# PartGroups.append([hair,mouth,hips,skin])
			# PartGroups.append([eyes,face,mouth,hips])
			# PartGroups.append([eyes,face,mouth,legs])
			# PartGroups.append([eyes,face,mouth,skin])
			# PartGroups.append([eyes,face,skin,hips])
			# PartGroups.append([eyes,face,skin,legs])
			# PartGroups.append([eyes,face,skin,body])
			# PartGroups.append([eyes,mouth,hips,legs])
			# PartGroups.append([eyes,mouth,hips,skin])
			# PartGroups.append([eyes,mouth,hips,body])
			# PartGroups.append([eyes,mouth,legs,hips])
			# PartGroups.append([eyes,mouth,legs,skin])
			# PartGroups.append([eyes,mouth,legs,body])
			# PartGroups.append([eyes,skin,hips,legs])
			# PartGroups.append([eyes,skin,hips,body])
			# PartGroups.append([eyes,skin,legs,hips])
			# PartGroups.append([eyes,skin,legs,body])
			# PartGroups.append([skin,legs,hips,body])
			# PartGroups.append([skin,hips,legs,body])
			# PartGroups.append([body,skin,hips,legs])
			# PartGroups.append([body,skin,legs,hips])
		else:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
											if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
												PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
			# PartGroups.append([hair,eyes,face,mouth,hips])
			# PartGroups.append([hair,eyes,face,mouth,legs])
			# PartGroups.append([hair,eyes,face,mouth,skin])
			# PartGroups.append([hair,eyes,face,mouth,body])
			# PartGroups.append([hair,eyes,face,hips])
			# PartGroups.append([hair,eyes,face,legs])
			# PartGroups.append([hair,eyes,face,skin])
			# PartGroups.append([hair,eyes,face,body])
			# PartGroups.append([hair,eyes,mouth,hips])
			# PartGroups.append([hair,eyes,mouth,legs])
			# PartGroups.append([hair,eyes,mouth,skin])
			# PartGroups.append([hair,eyes,mouth,body])
			# PartGroups.append([hair,face,eyes,mouth])
			# PartGroups.append([hair,face,eyes,hips])
			# PartGroups.append([hair,face,eyes,legs])
			# PartGroups.append([hair,face,eyes,mouth])
			# PartGroups.append([hair,face,eyes,skin])
			# PartGroups.append([hair,face,mouth,hips])
			# PartGroups.append([hair,face,mouth,legs])
			# PartGroups.append([hair,face,mouth,skin])
			# PartGroups.append([hair,mouth,legs,hips])
			# PartGroups.append([hair,mouth,legs,skin])
			# PartGroups.append([hair,mouth,hips,legs])
			# PartGroups.append([hair,mouth,hips,skin])
			# PartGroups.append([eyes,face,mouth,hips])
			# PartGroups.append([eyes,face,mouth,legs])
			# PartGroups.append([eyes,face,mouth,skin])
			# PartGroups.append([eyes,face,skin,hips])
			# PartGroups.append([eyes,face,skin,legs])
			# PartGroups.append([eyes,face,skin,body])
			# PartGroups.append([eyes,mouth,hips,legs])
			# PartGroups.append([eyes,mouth,hips,skin])
			# PartGroups.append([eyes,mouth,hips,body])
			# PartGroups.append([eyes,mouth,legs,hips])
			# PartGroups.append([eyes,mouth,legs,skin])
			# PartGroups.append([eyes,mouth,legs,body])
			# PartGroups.append([eyes,skin,hips,legs])
			# PartGroups.append([eyes,skin,hips,body])
			# PartGroups.append([eyes,skin,legs,hips])
			# PartGroups.append([eyes,skin,legs,body])
			# PartGroups.append([skin,legs,hips,body])
			# PartGroups.append([skin,hips,legs,body])
			# PartGroups.append([body,skin,hips,legs])
			# PartGroups.append([body,skin,legs,hips])
		
		SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
		
		iLoops = 0
		while iLoops < iNum:
			sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc)
			if iLoops == iNum - 2:  
				sBodyDesc += sDivideChar + " and "
			elif iLoops < iNum - 2:
				sBodyDesc += sDivideChar + " "
			iLoops = iLoops + 1
			
		return sBodyDesc
		
	
	def GetRandomBodyParts(self, iNum, bIncludeInners = False, bIncludeIntimate = True, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		elif bIncludeIntimate:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		#print(AllParts)
		return Parts
		
	def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
	def GetHoles(self, bIncludeMouth = True):
		Holes = []
		
		if bIncludeMouth:
			Holes = [3]
		
			Holes[0] = self.Mouth.RandomDescription()
			Holes[1] = self.Vagina.RandomDescription()
			Holes[2] = self.Ass.Anus.RandomDescription()
		else:
			Holes = [2]
			
			Holes[0] = self.Vagina.RandomDescription()
			Holes[1] = self.Ass.Anus.RandomDescription()
		
		return Holes
		
	def GetRandomHole(self, bIncludeMouth = True, bAllowShortDesc = True, bAllowLongDesc = True):
		sHole = ""
		Holes = []
		if bIncludeMouth:		
			Holes.append(self.Mouth.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
		else:
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
		
		iRand = randint(0, len(Holes) - 1)
		sHole = Holes[iRand]
		
		return sHole
		
class PenisHead(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['cock-head',
			'head',
			'head',
			'head',
			'helmet',
			'knob',
			'knob',
			'mushroom',
			'tip',
			'tip'])
			
		self.AdjList(['bulging',
			'dripping',
			'engorged',
			'glistening',
			'pulsating',
			'purple',
			'smooth',
			'swollen',
			'throbbing',
			'tumescent'])
			
		self.ColorList(['black',
			'brown',
			'purple',
			'red'])
		
		self.DefaultNoun("head")
		self.IsPlural = False
		
class Testicles(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['balls',
			'ballsack',
			'bollocks',
			'gonads',
			'nutsack',
			'sack',
			'silk purse',
			'scrotum',
			'testicles'])
			
		self.AdjList(['dangling',
			'downy',
			'down-covered',
			'fleshy',
			'hairy',
			'heavy',
			'hefty',
			'pendulous',
			'round',
			'satin',
			'silken',
			'soft',
			'smooth',
			'swaying',
			'swinging',
			'tender',
			'wrinkled'])
		
		self.DefaultNoun("testicles")

class Penis(BodyParts):
	def BuildAPenis(self):
		sPenis = ""
		
		iRandFront = 0
		iRandBack = 0
		
		iRandFront = randint(0,len(self.PenisFrontPart) - 1)
		iRandBack = randint(0,len(self.PenisBackPart) - 1)
		sFrontPart = self.PenisFrontPart[iRandFront]
		sBackPart = self.PenisBackPart[iRandBack]
		
		while sFrontPart in sBackPart:
			iRandFront = randint(0,len(self.PenisFrontPart) - 1)
			iRandBack = randint(0,len(self.PenisBackPart) - 1)
			sFrontPart = self.PenisFrontPart[iRandFront]
			sBackPart = self.PenisBackPart[iRandBack]
			
		sPenis = sFrontPart + "-" + sBackPart
		
		while sPenis in self.GetNounList():
			iRandFront = randint(0,len(self.PenisFrontPart) - 1)
			iRandBack = randint(0,len(self.PenisBackPart) - 1)
			sFrontPart = self.PenisFrontPart[iRandFront]
			sBackPart = self.PenisBackPart[iRandBack]
			
			while sFrontPart in sBackPart:
				iRandFront = randint(0,len(self.PenisFrontPart) - 1)
				iRandBack = randint(0,len(self.PenisBackPart) - 1)
				sFrontPart = self.PenisFrontPart[iRandFront]
				sBackPart = self.PenisBackPart[iRandBack]
				
			sPenis = sFrontPart + "-" + sBackPart
			
		return sPenis
		
	def __init__(self):
		super().__init__()
		
		self.NounList(['boner',
			'cock',
			'cock',
			'cock',
			'cock meat',
			'cocksicle',
			'dick',
			'erection',
			'girth',
			'goo-gun',
			'hardness',
			'hard-on',
			'hot-rod',
			'joystick',
			'lady-dagger',
			'love-gun',
			'meat',
			'member',
			'organ',
			'package',
			'penis',
			'penis',
			'penis',
			'phallus',
			'pole',
			'popsicle',
			'prick',
			'ramrod',
			'rod',
			'schlong',
			'serpent',
			'shaft',
			'snake',
			'stalk',
			'stem',
			'thing',
			'tool',
			'wood'])
			
		self.AdjList(['beautiful',
			'beefy',
			'bulging',
			'burning',
			'carefully man-scaped',
			'engorged',
			'enormous',
			'enormously erect',
			'erect',
			'erect',
			'fat',
			'fat',
			'fevered',
			'fully erect',
			'hairy',
			'hairless',
			'hard',
			'hardening',
			'hardened',
			'huge',
			'hugely erect',
			'impressive',
			'lengthy',
			'long',
			'lovingly man-scaped',
			'magnificient',
			'massive',
			'massively erect',
			'meaty',
			'pulsating',
			'raging',
			'rampant',
			'rigid',
			'rock-hard',
			'silken',
			'smooth',
			'stiff',
			'swollen',
			'tall',
			'tasty',
			'thick',
			'throbbing',
			'towering',
			'tumescent',
			'turgid',
			'unfurled',
			'veiny',
			'virile'])
			
		self.PenisFrontPart = ['beef',
			'flesh',
			'fuck',
			'love',
			'man',
			'meat']
			
		self.PenisBackPart = ['bayonette',
			'bone',
			'hammer',
			'lance',
			'meat',
			'missile',
			'pipe',
			'pistol',
			'pole',
			'popsicle',
			'python',
			'rocket',
			'rod',
			'rifle',
			'sausage',
			'serpent',
			'shaft',
			'snake',
			'stack',
			'stalk',
			'stick',
			'sword',
			'tool',
			'tube',
			'weapon',
			'worm']
		
		self.DefaultNoun("cock")
		self.IsPlural = False
		self.Head = PenisHead()
		self.Testicles = Testicles()
		
		for i in range(0, int(len(self.GetNounList()) * (2/3))):
			self.GetNounList().append(self.BuildAPenis())
	
	def GetRandomPenisPart(self, sNot = None, NotList = None, bAllowShortDesc = False):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		iRand = randint(1,3)
		
		if iRand == 1:
			return self.Head.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
		elif iRand == 2: 
			return self.Testicles.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
		else:
			return self.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
			
	def GenerateLength(self):
		sLength = ""
		
		sLength = str(randint(6, 13))
		if CoinFlip():
			sLength += " 1/2"
		sLength += "\""
		
		return sLength
			
	def ShortDescription(self, sNot = "", NotList = None, bAddLen = False):
		sDesc = super().ShortDescription(sNot = "", NotList = NotList)
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)

		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc
		
	def MediumDescription(self, sNot = "",  NotList = None, bAddLen = False):
		sDesc = super().MediumDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
			
		return sDesc 
		
	def FloweryDescription(self, sNot = "", NotList = None, bAddLen = False):
		sDesc = super().FloweryDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
		
	def RandomDescription(self, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False):
		sDesc = super().RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
	
class Semen(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['cock milk',
			'cock-snot',
			'cream',
			'cum',
			'jizm',
			'jizz',
			'load',
			'lotion',
			'man-custard',
			'man-jam',
			'man-milk',
			'man-seed',
			'sauce',
			'seed',
			'semen',
			'sperm',
			'splooge',
			'spunk'])
			
		self.AdjList(['creamy',
			'delicious',
			'glossy',
			'gooey',
			'nasty',
			'nourishing',
			'oozing',
			'ropy',
			'salty',
			'silken',
			'silky',
			'sloppy',
			'sticky',
			'tasty',
			'thick',
			'warm',
			'white-hot',
			'yummy'])
			
		self.ColorList(['cream-colored',
						'milky',
						'pearly',
						'pearlescent',
						'white'
					  ])
		
		self.DefaultNoun("semen")
		self.DefaultAdj("gooey")
		
class AssMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['ass',
			'backside',
			'behind',
			'bottom',
			'bum',
			'buns',
			'butt',
			'butt cheeks',
			'buttocks',
			'glutes',
			'gluteous maximus',
			'rump',
			'tush'])
			
		self.AdjList(['beefy',
			'broad',
			'bronzed',
			'chiseled',
			'compact',
			'hairy',
			'lean',
			'manly',
			'masculine',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'rock-hard',
			'smooth',
			'strapping',
			'supple',
			'taut',
			'tight',
			'trim',
			'virile',
			'well-defined'])
		
		self.DefaultNoun("buttocks")
		
class SkinMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['skin',
			'skin',
			'skin',
			'flesh',
			'hide'])
			
		self.AdjList(['bare',
			'cream-colored',
			'exposed',
			'freckled',
			'glistening',
			'hairy',
			'naked',
			'rough',
			'rugged',
			'smooth',
			'supple',
			'tough',
			'warm',
			'youthful'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'pale',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("skin")
		self.DefaultAdj("rugged")
		
class ShouldersMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['shoulders'])
			
		self.AdjList(['bare',
			'brawny',
			'broad',
			'freckled',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rugged',
			'strong',
			'sturdy',
			'well-built',
			'wide'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("shoulders")
		self.DefaultAdj("broad")
		
class ChestMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['chest',
			'chest',
			'chest',
			'chest',
			'pectorals'])
			
		self.AdjList(['bare',
			'brawny',
			'broad',
			'burly',
			'compact',
			'dark-thatched',
			'expansive',
			'hairy',
			'lusty',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'ripped',
			'rugged',
			'strapping',
			'strong',
			'sturdy',
			'toned',
			'wide',
			'uncovered',
			'virile',
			'well-built',
			'well-defined',
			'well-oiled'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("chest")
		self.DefaultAdj = "broad"
		
class ArmsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['arms',
			'arms',
			'arms',
			'arms',
			'limbs'])
			
		self.AdjList(['athletic',
			'bare',
			'brawny',
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'protective',
			'rippling',
			'ripped',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry'])
		
		self.DefaultNoun("arms")
		self.DefaultAdj("muscular")
		
class EyesMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['eyes'])
			
		self.AdjList(['beautiful',
			'brooding',
			'captivating',
			'dazzling',
			'deep',
			'kind',
			'mischievous',
			'penetrating',
			'soulful',
			'steely',
			'stern',
			'youthful'])
			
		self.ColorList(['blue',
						'brown',
						'dark',
						'gray',
						'green',
						'hazel',
						'icy-blue',
						'steely-blue'
					   ])
		
		self.DefaultNoun("eyes")
		self.DefaultAdj("penetrating")
		
class LegsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['legs',
			'legs',
			'legs',
			'calves',
			'limbs',
			'thighs'])
			
		self.AdjList(['athletic',
			'bare',
			'brawny',
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rangy',
			'rippling',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry'])
		
		self.DefaultNoun("legs")
		self.DefaultAdj("sinewy")
		
class JawMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['jaw'])
			
		self.AdjList(['bearded',
			'chiseled',
			'commanding',
			'decisive',
			'dominant',
			'forceful',
			'handsome',
			'powerful',
			'rugged',
			'scruffy',
			'sharp',
			'striking'])
		
		self.DefaultNoun("jaw")
		self.DefaultAdj("chiseled")
		
class BodyMale(BodyParts):	
	def __init__(self):
		super().__init__()
		
		self.NounList(['body',
			'form',
			'physique',
			'anatomy',
			'bulk',
			'build',
			'body',
			'physique',
			'build',
			'form',
			'body'])
			
		self.AdjList(['beefy',
			'brawny',
			'broad',
			'bronzed',
			'burly',
			'commanding',
			'compact',
			'dark-thatched',
			'handsome',
			'hung',
			'lean',
			'limber',
			'manly',
			'masculine',
			'massive',
			'muscular',
			'powerful',
			'rugged',
			'sinewy',
			'smooth',
			'strapping',
			'striking',
			'strong',
			'sturdy',
			'supple',
			'tall',
			'taut',
			'tight',
			'toned',
			'towering',
			'trim',
			'virile',
			'well-built',
			'well-hung',
			'well-oiled',
			'wiry',
			'youthful'])
		
		self.DefaultNoun("body")
		self.IsPlural = False
		#self.Hair = Hair()
		self.Eyes = EyesMale()
		self.Jaw = JawMale()
		self.Legs = LegsMale()
		self.Skin = SkinMale()
		self.Shoulders = ShouldersMale()
		self.Chest = ChestMale()
		self.Arms = ArmsMale()
		self.Ass = AssMale()
		self.Penis = Penis()
		
	def GetRandomBodyParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
	def GetRandomIntimateParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts