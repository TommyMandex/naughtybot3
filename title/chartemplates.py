#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import *
from util import *

# === Female templates ===

# Good Female Profession
class FemTemplate1(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfGoodFemale(),
							 id = 1, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],6),
										  CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)
		
# Bad Female Profession		
class FemTemplate2(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale(),
							 id = 2, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],9),
										  CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)
					
# Good (Pregnant) Female Profession					
class FemTemplate3(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfGoodFemale(),
							 id = 3, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([NationFemale, SkinHairColorFemale],3),
										  CTEntry([PregState],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)
				
# Bad (Pregnant) Female Profession				
class FemTemplate4(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale(),
							 id = 4, 
							 adjlist = 	[ CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)
						
# Good Female Royalty						
class FemTemplate5(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = TitlesFemale(),
							 id = 5, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],6),
										  CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)

# Bad Female Royalty
class FemTemplate6(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = TitlesFemale(),
							 id = 7, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],9),
										  CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)

# Good Female Relation					
class FemTemplate8(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = RelateFemale(),
							 id = 8, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							bpersonal = True,
							girltype = GirlType.Good)

# Bad Female Relation 
class FemTemplate9(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun =  RelateFemale(),
							 id = 9, 
							 adjlist = 	[ CTEntry([GenModFemale],7),
										  CTEntry([AttitudeBadFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							bpersonal = True,
							girltype = GirlType.Bad
							)

# Female Good Profession + Bad Profession 			
class FemTemplate10(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale(),
							 id = 10, 
							 adjlist = 	[ CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],3),  
										  CTEntry([SpeciesFemale],2),
										  CTEntry([ProfGoodFemale],1),
										], 
							girltype = GirlType.Bad)

# Good Female of a Certain Age
class FemTemplate11(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale(),
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)
			
# Bad Female of a Certain Age 			
class FemTemplate9(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale(),
							 id = 9, 
							 adjlist = 	[ CTEntry([GenModFemale],6),
										  CTEntry([AttitudeBadFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([ClothingFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([SexualityFemale],1),  
										], 
							girltype = GirlType.Bad)

# Good Female of a Certain Age
class FemTemplate11(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale(),
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)
							
# Bad Female of a Fantasy Species 			
class FemTemplate12(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = SpeciesFemale(),
							 id = 12, 
							 adjlist = 	[ CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfBadFemale,ProfGoodFemale],1)
										], 
							girltype = GirlType.Bad)

# Good Female of a Fantasy Species
class FemTemplate13(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = SpeciesFemale(),
							 id = 13, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["succubus"])
							
# === Good Trope templates ===

class FemGoodTropeTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Amish Maiden"),
							 id = 101, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([SkinHairColorFemale,PregState],2),
										  CTEntry([PregState],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["amish","maiden"])
							
class FemGoodTropeTemplate2(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("BBW"),
							 id = 102, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([ProfGoodFemale],1),  
										  CTEntry([SpeciesFemale],0),
										], 
							girltype = GirlType.Good,
							NotList = ["athletic","bikini","flat-chested","leggy","little","slender","sporty","tight"])
							
class FemGoodTropeTemplate3(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Beauty"),
							 id = 103, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["beauty"])
							
class FemGoodTropeTemplate4(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Beauty Queen"),
							 id = 104, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),   
										], 
							girltype = GirlType.Good,
							NotList = ["beauty","queen"])

class FemGoodTropeTemplate5(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Bride"),
							 id = 105, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),   
										], 
							bpersonal = True,
							girltype = GirlType.Good)
							
class FemGoodTropeTemplate6(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Catholic School-girl"),
							 id = 106, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["Catholic","school"])
							
class FemGoodTropeTemplate7(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Chaste Nun"),
							 id = 107, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([NationFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["chaste","sexy","bikini","mormon"])
							
class FemGoodTropeTemplate8(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Cheer-Squad Captain"),
							 id = 108, 
							 adjlist = 	[CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["cheer"])
							
class FemGoodTropeTemplate9(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Damsel-in-Distress"),
							 id = 109, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["damsel"])
							
class FemGoodTropeTemplate10(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Farmer's Daughter"),
							 id = 110, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["farmer","daughter"])
							
class FemGoodTropeTemplate11(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Hippy Chick"),
							 id = 111, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good)
							
class FemGoodTropeTemplate12(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("HuCow"),
							 id = 112, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["athletic","flat-chested","slender","sporty","tight"])
							
class FemGoodTropeTemplate13(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Kitten"),
							 id = 113, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["mom"])
							
class FemGoodTropeTemplate14(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Pastor's Wife"),
							 id = 114, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2)
										], 
							bpersonal = True,
							girltype = GirlType.Good,
							NotList = ["tanned"])
							
class FemGoodTropeTemplate15(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Pixie"),
							 id = 115, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["marm","mommy","Amish","Mormon","Christian"])
							
class FemGoodTropeTemplate16(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Princess"),
							 id = 116, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([NationFemale],2), 
										  CTEntry([SpeciesFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["mom"])

class FemGoodTropeTemplate17(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Prom Queen"),
							 id = 117, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["queen","shy","kind","gentle","bashful","lactating","nursing"])
							
class FemGoodTropeTemplate18(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("School-girl"),
							 id = 118, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale,PregState],2),
										  CTEntry([SpeciesFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["school"])
							
class FemGoodTropeTemplate19(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Single Mom"),
							 id = 119, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([PregState],2),
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["single","mom","asian","japanese","amish","russian","columbian","bronzed","tanned","czech","brazillian","swedish"])
							
class FemGoodTropeTemplate20(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Slave Girl"),
							 id = 120, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([ProfBadFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["black","ebony","dark-skinned","town","American","porn","fashion","queen","housewife","nurse","country"])
							
class FemGoodTropeTemplate21(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Small-town Girl"),
							 id = 121, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([SkinHairColorFemale,PregState],2),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["schoolgirl"])
							
class FemGoodTropeTemplate22(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Snow Bunny"),
							 id = 122, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale,],3),
										  CTEntry([NationFemale,],2),
										], 
							girltype = GirlType.Good,
							NotList = ["mom","town","straight-laced","amish","mormon","christian","modest","shy","demure","conservative","virtuous","uptight","bashful","sheltered"])
							
class FemGoodTropeTemplate23(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Soccer Mom"),
							 id = 123, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([SkinHairColorFemale],3),
										], 
							girltype = GirlType.Good,
							NotList = ["single"])
							
class FemGoodTropeTemplate24(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Southern Bell"),
							 id = 124, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([SkinHairColorFemale],2),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["fishy"])
							
class FemGoodTropeTemplate25(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Tomboy"),
							 id = 125, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["Gentle","Kind","Statuesque","Stacked","Bashful","Shy","Big Bottomed","Ditzy",
									   "Juicy","Demure","Tender","Soft","boob","plump","chubby","curvy"])
							
class FemGoodTropeTemplate26(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Virgin"),
							 id = 126, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([SkinHairColorFemale,AgeAdjFemale],4),
										  CTEntry([NationFemale,SpeciesFemale],3),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["mom","virgin","MILF","wife","succubus","nymph"])
							
						

# === Bad Trope templates ===

class FemBadTropeTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Bad Girl"),
							 id = 201, 
							 adjlist = 	[ CTEntry([GenModFemale],10),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([AgeAdjFemale],3),
										  CTEntry([SexualityFemale],2)
										], 
							girltype = GirlType.Bad,
							NotList = ["MILF","Mature","Older"])
							
class FemBadTropeTemplate2(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Beach Bunny"),
							 id = 202, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale,NationFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],2)
										], 
							girltype = GirlType.Bad,
							NotList = ["braless","stylish","leather","latex","country","modest","bashful","conservative",
										"straight-laced","shy","chaste","sheltered","uptight","pale","fetish"])
										
class FemBadTropeTemplate3(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Bitch"),
							 id = 203, 
							 adjlist = 	[ CTEntry([PhysCharFemale],7),
										  CTEntry([AgeAdjFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],5),
										  CTEntry([SexualityFemale],3),
										  CTEntry([ProfFemale,RelateFemale,TitlesFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["Maiden","Tender","Soft"])
							
class FemBadTropeTemplate4(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Brat"),
							 id = 204, 
							 adjlist = 	[ 
										  CTEntry([AttitudeBadFemale],9),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],2),
										  CTEntry([RelateFemale,TitlesFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["fashionable","stylish","willing","attractive","gorgeous","soft","queen","mom","marm",
										"statuesque"])
										
class FemBadTropeTemplate5(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Anal Bimbo"),
							 id = 205, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale],4),
										  CTEntry([NationFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfBadFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["anal","BDSM"])
							
class FemBadTropeTemplate6(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Bimbo"),
							 id = 206, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale],4),
										  CTEntry([NationFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfBadFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["BDSM"])

class FemBadTropeTemplate7(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Cougar"),
							 id = 207, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([SkinHairColorFemale],3)
										], 
							girltype = GirlType.Bad,
							NotList = ["young","skinny","slender"])
							
class FemBadTropeTemplate8(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Femme Fatale"),
							 id = 208, 
							 adjlist = 	[ 
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["anal","BDSM","Porn Star","Mormon","Christian","Country","cheer","small-town",
									   "chubby","soft","single","mom","wild","yoga","thick","braless","co-ed","teen",
									   "elvish","intern","curious","nudist"])
							
class FemBadTropeTemplate9(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Goth Girl"),
							 id = 209, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfBadFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["Penthouse","Centerfold","cheerleader","housewife","marm","hooter",
										"sporty""tender","soft","nudist","gymnast"])

class FemBadTropeTemplate10(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Harem Princess"),
							 id = 210, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeGoodFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([PregState],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3)
										], 
							girltype = GirlType.Bad,
							NotList = [])
							
class FemBadTropeTemplate20(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Porn Star"),
							 id = 220, 
							 adjlist = 	[ 
										  CTEntry([GenModFemale],11),
										  CTEntry([GenModFemale],10),
										  CTEntry([AttitudeBadFemale],9),
										  CTEntry([PhysCharFemale],8),
										  CTEntry([ClothingFemale],7),
										  CTEntry([NationFemale,SkinHairColorFemale],6),
										  CTEntry([AgeAdjFemale],5),
										  CTEntry([PregState],4),
										  CTEntry([SexualityFemale],3),  
										  CTEntry([SpeciesFemale],2),
										  CTEntry([ProfBadFemale,ProfGoodFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["virgin","stripper","dancer","lingerie","soft","braless","revealing"])
							
class FemBadTropeTemplate21(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Sex Kitten"),
							 id = 221, 
							 adjlist = 	[CTEntry([GenModFemale],7),
										  CTEntry([AttitudeBadFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([PregState],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad,
							NotList = ['Christian','Mormon'])	
				
# === Species templates ===

class FemGoodSpeciesTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Elf"),
							 id = 301, 
							 adjlist = 	[CTEntry([AttitudeFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2)
										], 
							girltype = GirlType.Neutral,
							NotList = ["Bashful","Shy","Big Bottomed","Ditzy","Juicy","boob","plump","chubby","curvy"])
							
class FemGoodSpeciesTemplate2(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Elf Princess"),
							 id = 302, 
							 adjlist = 	[CTEntry([AttitudeFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2)
										], 
							girltype = GirlType.Neutral,
							NotList = ["Bashful","Shy","Big Bottomed","Ditzy","Juicy","boob","plump","chubby","curvy"])
							
class FemGoodSpeciesTemplate3(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Fairy"),
							 id = 303, 
							 adjlist = 	[CTEntry([AttitudeFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([TitlesFemale],1)
										], 
							girltype = GirlType.Neutral,
							NotList = ["MILF","heiress"])

class FemGoodSpeciesTemplate4(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Futa"),
							 id = 304, 
							 adjlist = 	[CTEntry([AttitudeFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([DickCharMale],4),
										  CTEntry([ClothingFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([TitlesFemale,ProfBadFemale,ProfGoodFemale],1)
										], 
							girltype = GirlType.Neutral,
							NotList = ["MILF"])
							
class FemGoodSpeciesTemplate5(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Green-Skinned Alien"),
							 id = 305, 
							 adjlist = 	[CTEntry([AttitudeFemale],6),
										  CTEntry([PhysCharFemale],5),	
										  CTEntry([AgeAdjFemale,MaritalStatusFemale],4),	
										  CTEntry([ClothingFemale],3),
										  CTEntry([SexualityFemale],2)
										], 
							girltype = GirlType.Neutral,
							NotList = ["Skin","wet"])

class FemGoodSpeciesTemplate6(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Mermaid"),
							 id = 306, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale,AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),	
										  CTEntry([AgeAdjFemale,MaritalStatusFemale],5),	
										  CTEntry([ClothingFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfFemale,TitlesFemale],1)
										], 
							girltype = GirlType.Neutral,
							NotList = ["Skin"])
							
class FemGoodSpeciesTemplate7(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Nymph"),
							 id = 307, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale,AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),		
										  CTEntry([ClothingFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Neutral,
							NotList = ["big","mom","nymph"])

class FemGoodSpeciesTemplate8(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Succubus"),
							 id = 308, 
							 adjlist = 	[CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),		
										  CTEntry([ClothingFemale],5),
										  CTEntry([AgeAdjFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfFemale],1)
										], 
							girltype = GirlType.Bad,
							NotList = ["succubus","virgin","amish","christian","mormon","jewish"])

class FemGoodSpeciesTemplate9(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Vampire"),
							 id = 309, 
							 adjlist = 	[CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),		
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										], 
							girltype = GirlType.Bad,
							NotList = ["vampire","virgin","amish","christian","mormon","jewish","amish"])

class FemGoodSpeciesTemplate10(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Vampire Queen"),
							 id = 310, 
							 adjlist = 	[CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),		
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),
										], 
							girltype = GirlType.Bad,
							NotList = ["vampire","virgin","amish","christian","mormon","jewish","queen","amish"])						
# Adj:		AgeAdjFemale, AttitudeGoodFemale, AttitudeBadFemale, AttitudeFemale,
# 			ClothingFemale, GenModFemale, MaritalStatusFemale, NationFemale, PhysCharFemale
#			PregState, SexualityFemale, SkinHairColorFemale, SpeciesFemale
# Nouns: 	AgeNounFemale, SpeciesFemale, ProfGoodFemale, ProfBadFemale, ProfFemale, RelateFemale,TitlesFemale						
	

# === Male templates ===		

# Male Profession
class MaleTemplate1(MaleCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfMale(),
							 id = 1, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([PhysCharMale,DickCharMale],8),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale,MaritalStatusMale],5),
										  CTEntry([SkinHairColorMale,NationMale],3),
										  CTEntry([SpeciesMale,ProfMale],1)
										])

# Male Relative 
class MaleTemplate2(MaleCharTemplate):
	def __init__(self):
		super().__init__(	noun = RelateMale(),
							 id = 2, 
							 adjlist = 	[ CTEntry([GenModMale],11), 
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([PhysCharMale,DickCharMale],8),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],5),
										  CTEntry([SkinHairColorMale,NationMale],3),
										  CTEntry([SpeciesMale],2),
										  CTEntry([ProfMale],1)
										],
							bpersonal = True)

# Male Royalty
class MaleTemplate3(MaleCharTemplate):
	def __init__(self):
		super().__init__(	noun = TitlesMale(),
							 id = 3, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([NationMale],3),
										  CTEntry([SpeciesMale],1)
										])
# Male of some Nation
class MaleTemplate4(MaleCharTemplate):
	def __init__(self):
		super().__init__(	noun = NationNounMale(),
							 id = 4, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([TypeModMale],6)
										])
# Male Millionaire
class MaleTemplate5(MaleCharTemplate):
	def __init__(self):
		super().__init__(	noun = TropesWealthyMale(),
							 id = 5, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale,MaritalStatusMale],5),
										  CTEntry([SpeciesMale],1),
										  CTEntry([ProfMale],1)
										])

# === Male tropes ===	
										
class MaleTropeTemplate1(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Alpha"),
							 id = 101, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],5),
										  CTEntry([NationMale],4),
										  CTEntry([SpeciesMale,ProfMale],2),
										  CTEntry([ProfMale],1),
										],
							NotList = ["male","fashionable","dapper","gentlemanly"])	

class MaleTropeTemplate2(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Alpha Male"),
							 id = 102, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],5),
										  CTEntry([NationMale],4),
										  CTEntry([SpeciesMale,ProfMale],2),
										  CTEntry([ProfMale],1),
										],
							NotList = ["male","fashionable","dapper","gentlemanly"])

class MaleTropeTemplate3(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Bachelor"),
							 id = 103, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale,NationMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],5),
										  CTEntry([SpeciesMale],2)
										],
							NotList = ["teen","taboo","savage"])	


class MaleTropeTemplate4(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Bad Boy"),
							 id = 104, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale,NationMale],7),
										  CTEntry([TypeModMale],6)
										],
							NotList = ["mature","bald"])		

class MaleTropeTemplate5(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Barbarian"),
							 id = 105, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale,MaritalStatusMale],5),
										  CTEntry([SpeciesMale],2)
										],
							NotList = ["dapper","gentlemanly","stay-at-home"])	
							
class MaleTropeTemplate6(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("BBC"),
							 id = 106, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],5),
										  CTEntry([ProfMale],1),
										],
							NotList = ["black","frat"])	

class MaleTropeTemplate7(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Biker"),
							 id = 107, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],4),
										  CTEntry([ProfMale,SpeciesMale],2)
										],
							NotList = ["motorcycle","stay-at-home"])	

class MaleTropeTemplate8(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Biker"),
							 id = 108, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([AgeAdjMale],4),
										  CTEntry([ProfMale,SpeciesMale],2)
										],
							NotList = ["motorcycle","stay-at-home"])							

class MaleTropeTemplate9(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Boss"),
							 id = 109, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([ClothesMale],6),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale],3),
										  CTEntry([SpeciesMale],2),
										  CTEntry([TropesWealthyMale],1)
										],
							bpersonal = True,
							NotList = ["teen","stay-at-home","college","young"])

class MaleTropeTemplate10(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Breeding Stud"),
							 id = 110, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],7),
										  CTEntry([TypeModMale],6),
										  CTEntry([SpeciesMale],2),
										],
							NotList = ["teen","stay-at-home","college","young"])

class MaleTropeTemplate11(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Casanova"),
							 id = 111, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale,DickCharMale],8),
										  CTEntry([ClothesMale],7),
										  CTEntry([AgeAdjMale],6),
										  CTEntry([NationMale],5),
										  CTEntry([TypeModMale],4),										  
										  CTEntry([SpeciesMale,TropesWealthyMale],1)
										],
							NotList = ["american","stay-at-home"])

class MaleTropeTemplate12(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Criminal"),
							 id = 112, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale],3)
										],
							NotList = ["teen","stay-at-home","college","black","african","barbarian","bdsm""mature"
										])

class MaleTropeTemplate13(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Daddy"),
							 id = 113, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([ClothesMale],6),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale],3),
										  CTEntry([TropesWealthyMale],1)
										],
							bpersonal = True,
							NotList = ["teen","college","young"])

class MaleTropeTemplate14(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Daddy Dom"),
							 id = 114, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([ClothesMale],6),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale],3),
										  CTEntry([TropesWealthyMale],1)
										],
							NotList = ["teen","college","young"])	

class MaleTropeTemplate15(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("DILF"),
							 id = 115, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale,DickCharMale],9),
										  CTEntry([SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale,MaritalStatusMale],3)
										],
							NotList = ["teen","college","young","tattoo","taboo","raunchy","brazen","bronzed",
									   "tanned","savage","mysterious","masked","barbarian","bdsm","brooding",
									   "studly","bachelor","S.W.A.T.","hard-drinking","rakish","sly","slick",
									   "roguish","renegade","rebel","eligible","sex addict","thrill-seeking",
									   "powerful","dapper","smooth","fashionable","stylish"])	

class MaleTropeTemplate16(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Dirty Old Man"),
							 id = 116, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([SkinHairColorMale],5),
										],
							NotList = ["teen","college","young","tattoo","taboo","bronzed",
									   "barbarian","bdsm","studly","bachelor","S.W.A.T.",
									   "renegade","rebel","eligible","sex addict","powerful",
									   "dapper","smooth","fashionable","stylish","red-headed",
									   "black-bearded","sensual","suave","athletic","blonde",
									   "clean-cut","handsome","sensitive","seductive",
									   "clean-shaven"])	

class MaleTropeTemplate17(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Don Juan"),
							 id = 117, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale,DickCharMale],8),
										  CTEntry([ClothesMale],7),
										  CTEntry([AgeAdjMale],6),
										  CTEntry([NationMale],5),
										  CTEntry([TypeModMale],4),										  
										  CTEntry([SpeciesMale,TropesWealthyMale],1)
										],
							NotList = ["american","stay-at-home","barbarian"])

class MaleTropeTemplate18(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Ex-con"),
							 id = 118, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale],3)
										],
							NotList = ["teen","stay-at-home","college","black","african","barbarian","bdsm",
										"young","S.W.A.T.","eligible","dapper","stylish","fashionable",
										"space","christian"])

class MaleTropeTemplate19(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Family Man"),
							 id = 119, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale,DickCharMale],9),
										  CTEntry([SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([AgeAdjMale,],3),
										  CTEntry([MaritalStatusMale],2),
										],
							NotList = ["teen","college","young","tattoo","taboo","raunchy","brazen","bronzed",
									   "tanned","savage","mysterious","masked","barbarian","bdsm","brooding",
									   "studly","bachelor","S.W.A.T.","hard-drinking","rakish","sly","slick",
									   "roguish","renegade","rebel","eligible","sex addict","thrill-seeking",
									   "powerful","dapper","smooth","fashionable","stylish","single",
									   "wicked","wanton","naughty"])	

class MaleTropeTemplate20(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Gangsta"),
							 id = 120, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([TropesWealthyMale,ProfMale,SpeciesMale],3)
										],
							NotList = ["barbarian","bdsm","S.W.A.T.","eligible","dapper","stylish",
										"blonde","red-headed","nudist","addict"])

class MaleTropeTemplate21(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitMale("Gay-for-Pay Porn Star"),
							 id = 121, 
							 adjlist = 	[ CTEntry([GenModMale],11),
										  CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([NationMale,SkinHairColorMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([ProfBlueCollarMale],3)
										],
							NotList = ["gay"])

class MaleTropeTemplate22(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Gentleman"),
							 id = 122, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale,DickCharMale],9),
										  CTEntry([ClothesMale],8),
										  CTEntry([AgeAdjMale],7),
										  CTEntry([MaritalStatusMale],6),
										  CTEntry([SkinHairColorMale,NationMale],5),
										  CTEntry([TypeModMale],4),
										  CTEntry([SpeciesMale,TropesWealthyMale],2)
										],
							NotList = ["american","stay-at-home","barbarian","leather","shirtless",
										"teen","college","young","tattoo","taboo","raunchy","brazen","bronzed",
									   "tanned","savage","barbarian","brooding","oiled","beefy",
									   "S.W.A.T.","hard-drinking","sly","slick",
									   "renegade","rebel"])
									   
class MaleTropeTemplate23(MaleTropeTemplate):
	def __init__(self):
		super().__init__(	noun = TropeBitMale("Ghost"),
							 id = 123, 
							 adjlist = 	[ CTEntry([AttitudeMale],10),
										  CTEntry([PhysCharMale],9),
										  CTEntry([DickCharMale],8),
										  CTEntry([ClothesMale],6),
										  CTEntry([TropesWealthyMale,ProfFantasyMale,TitlesMale],1)
										],
							NotList = ["taboo","nudist","farmer","peasant","hairy","young","college",
									   "oiled","burly","beef","brawny","buff","giant","hulking"])

							
# Adjs:		GenModMale, AttitudeMale, ClothesMale, PhysCharMale, DickCharMale, TypeModMale,
#			SkinHairColorMale, AgeAdjMale, MaritalStatusMale, NationMale
# Nouns:	ProfMale, RelateMale, SpeciesMale, TitlesMale, TropesWealthyMale
# Jobs:		ProfBlueCollarMale,ProfWhiteCollarMale,ProfFantasyMale,ProfAthleteMale,ProfRockstarMale,
#			ProfNormalMale,ProfAspirationalMale,ProfMale
# CharBitList.append(AttitudeMale())
# CharBitList.append(PhysCharMale())
# CharBitList.append(DickCharMale())
# CharBitList.append(SkinHairColorMale())
# CharBitList.append(GenModMale())
# CharBitList.append(AgeAdjMale())
# CharBitList.append(MaritalStatusMale())
# CharBitList.append(NationMale())
# CharBitList.append(ProfMale())
# CharBitList.append(SpeciesMale())
# CharBitList.append(TropeMale())
# CharBitList.append(RelateMale())
# CharBitList.append(TitleMale())


	