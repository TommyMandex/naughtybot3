#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Names module

from random import *

class Names:
	FirstNamesList = []
	LastNamesList = []
	
	def FirstName(self):
		sFirstName = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.FirstNamesList) - 1)
		
		sFirstName = self.FirstNamesList[iRandIndex]
		
		return sFirstName

class NamesMale(Names):
	def __init__(self):
		self.FirstNamesList = ['Adam',
			'Alistair',
			'Ambrose',
			'Andre',
			'Angel',
			'Apollo',
			'Archer',
			'Blake',
			'Brad',
			'Bradford',
			'Bradley',
			'Cal',
			'Chad',
			'Christopher',
			'Clint',
			'Clive',
			'Connor',
			'Cullen',
			'Dallas',
			'Dante',
			'Darius',
			'Desmond',
			'Dick',
			'Dominic',
			'Drake',
			'Drew',
			'Eduardo',
			'Esteban',
			'Ferdinand',
			'Finn',
			'Flint',
			'Gavin',
			'Geoffrey',
			'Grant',
			'Griffin',
			'Grigory',
			'Hudson',
			'Hunter',
			'Iain',
			'Ivan',
			'James',
			'Javier',
			'Jim',
			'John',
			'Jordan',
			'Juan',
			'Julian',
			'Kane',
			'Leo',
			'Leon',
			'Lex',
			'Liam',
			'Lorenzo',
			'Manuel',
			'Marco',
			'Max',
			'Michael',
			'Michel',
			'Nicolas',
			'Pablo',
			'Peter',
			'Quentin',
			'Quinn',
			'Rafael',
			'Rafe',
			'Ramon',
			'Raoul',
			'Reed',
			'Reginald',
			'Remington',
			'Rex',
			'Ricardo',
			'Richard',
			'Rico',
			'Roberto',
			'Rogan',
			'Roland',
			'Ronson',
			'Rowan',
			'Royce',
			'Ruben',
			'Russell',
			'Ryder',
			'Sean',
			'Sebastian',
			'Sergei',
			'Shane',
			'Stefan',
			'Sterling',
			'Tom',
			'Tremaine',
			'Trey',
			'Tristan',
			'Tristan',
			'Tucker',
			'Ty',
			'Vance',
			'Vaughan',
			'Vicenzo',
			'Vincent',
			'Xavier']	
		
class NamesFemale(Names):
	def __init__(self):
		self.FirstNamesList = ['Alana',
			'Alexis',
			'Amber',
			'Amelia',
			'Anastasia',
			'Angela',
			'Angelica',
			'Anita',
			'Anna',
			'Annabel',
			'Aria',
			'Autumn',
			'Ava',
			'Bella',
			'Belle',
			'Bianca',
			'Brielle',
			'Brigitte',
			'Brynn',
			'Calliope',
			'Candy',
			'Caroline',
			'Carmina',
			'Cecie',
			'Charity',
			'Chastity',
			'Chelsea',
			'Cherry',
			'Clarissa',
			'Colette',
			'Constance',
			'Cordelia',
			'Daisy',
			'Dalia',
			'Dani',
			'Dannielle',
			'Daphne',
			'Deanna',
			'Delilah',
			'Delores',
			'Dianne',
			'Donna',
			'Eden',
			'Eliza',
			'Elizabeth',
			'Emma',
			'Ericka',
			'Esmerelda',
			'Estelle',
			'Felicia',
			'Felicity',
			'Fiona',
			'Florence',
			'Francesca',
			'Georgina',
			'Ginger',
			'Gisele',
			'Harmony',
			'Heidi',
			'Harriet',
			'Heaven',
			'Honey',
			'Holly',
			'Indigo',
			'Isabelle',
			'Jacinda',
			'Jaqueline',
			'Jasmine',
			'Josephine',
			'Juliana',
			'Juliette',
			'Juniper',
			'Jynx',
			'Kaitlyn',
			'Katrina',
			'Kitty',
			'Lacey',
			'Laurel',
			'Lauren',
			'Lavinia',
			'Lelani',
			'Leslie',
			'Lilah',
			'Lilli',
			'Lola',
			'Marianna',
			'Marilyn',
			'Marsha',
			'Melina',
			'Misty',
			'Molly',
			'Morgan',
			'Natasha',
			'Olive',
			'Olivia',
			'Ophelia',
			'Paris',
			'Penelope',
			'Phoebe',
			'Piper',
			'Rachael',
			'Raven',
			'Regina',
			'Roanna',
			'Rosaline',
			'Roxanne',
			'Ruby',
			'Sable',
			'Sabrina',
			'Saffron',
			'Satin',
			'Savannah',
			'Scarlett',
			'Simone',
			'Sophie',
			'Summer',
			'Svetlana',
			'Sydney',
			'Sylvia',
			'Tiffany',
			'Tonya',
			'Tori',
			'Valentina',
			'Vanessa',
			'Veronica',
			'Viola',
			'Violet',
			'Virginia',
			'Vivienne']