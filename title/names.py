#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Names module

from random import *
from util import *

class Names:
     def __init__(self):
          self.FirstNamesList = []
          self.LastNamesList = []
     
     def FirstName(self):
          sFirstName = ""
          iRandIndex = 0
          
          iRandIndex = randint(0, len(self.FirstNamesList) - 1)
          
          sFirstName = self.FirstNamesList[iRandIndex]
          
          return sFirstName

class NamesMale(Names):
     def __init__(self):
          super().__init__()
          
          self.FirstNamesList = ['Adam',
               'Adonis',
               'Alex',
               'Alistair',
               'Ambrose',
               'Andre',
               'Archer',
               'Benjamin',
               'Bill',
               'Blake',
               'Brad',
               'Bradford',
               'Bradley',
               'Brody',
               'Burt',
               'Buster',
               'Cal',
               'Christopher',
               'Clint',
               'Clive',
               'Connor',
               'Cullen',
               'Dallas',
               'Dante',
               'Darius',
               'Deacon',
               'Desmond',
               'Dick',
               'Dirk',
               'Dominic',
               'Don',
               'Doug',
               'Drake',
               'Drew',
               'Duane',
               'Earl',
               'Ed',
               'Eduardo',
               'Esteban',
               'Ferdinand',
               'Finn',
               'Flint',
               'Frank',
               'Gary',
               'Gavin',
               'Geoffrey',
               'George',
               'Grant',
               'Greg',
               'Griffin',
               'Hudson',
               'Hugh',
               'Hunter',
               'Iain',
               'Ivan',
               'Jack',
               'James',
               'Javier',
               'Jed',
               'Jerry',
               'Jim',
               'Jimmy',
               'Joe',
               'John',
               'Johnny',
               'Jordan',
               'Josh',
               'Juan',
               'Julian',
               'Kane',
               'Lance',
               'Leon',
               'Lex',
               'Liam',
               'Lorenzo',
               'Lou',
               'Luke',
               'Mac',
               'Manuel',
               'Mark',
               'Max',
               'Melvin',
               'Michael',
               'Mike','Mike',
               'Miles',
               'Ned',
               'Nick',
               'Nicolas',
               'Oliver',
               'Paul',
               'Peter',
               'Philmore',
               'Quentin',
               'Quinn',
               'Rafael',
               'Rafe',
               'Ramon',
               'Randy',
               'Raoul',
               'Reed',
               'Reggie',
               'Reginald',
               'Remington',
               'Rex',
               'Ricardo',
               'Rich',
               'Rico',
               'Roberto',
               'Rod',
               'Roland',
               'Romeo',
               'Rowan',
               'Royce',
               'Ruben',
               'Russell',
               'Ryder',
               'Sawyer',
               'Scott',
               'Sean',
               'Sebastian',
               'Seymour',
               'Shane',
               'Skip',
               'Stefan',
               'Steve',
               'Sterling',
               'Thad',
               'Tim',
               'Tom',
               'Tremaine',
               'Trevor',
               'Trey',
               'Tristan',
               'Tucker',
               'Valentine',
               'Vance',
               'Vaughan',
               'Vicenzo',
               'Vincent',
               'Xavier',
               'Zeke']     
          
class NamesFemale(Names):
     def __init__(self):
          super().__init__()
          
          self.FirstNamesList = ['Alana',
               'Alexis',
               'Amanda',
               'Amber',
               'Amelia',
               'Anastasia',
               'Angelica',
               'Anna',
               'Annabel',
               'Aria',
               'Autumn',
               'Ava',
               'Bella',
               'Belle',
               'Bianca',
               'Bobbi',
               'Brielle',
               'Brigitte',
               'Brynn',
               'Calliope',
               'Candy',
               'Carmina',
               'Cecie',
               'Charity',
               'Chastity',
               'Chelsea',
               'Cherry',
               'Clarissa',
               'Clover',
               'Colette',
               'Constance',
               'Cordelia',
               'Daisy',
               'Dani',
               'Daphne',
               'Delilah',
               'Delores',
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
               'Francesca',
               'Georgina',
               'Gisele',
               'Honey',
               'Ima',
               'Indigo',
               'Isabelle',
               'Ivana',
               'Jacinda',
               'Jackie',
               'Jaqueline',
               'Jasmine',
               'Josephine',
               'Juliette',
               'Juniper',
               'Jynx',
               'Katrina',
               'Kitty',
               'Lacey',
               'Laurel',
               'Lavinia',
               'Lelani',
               'Leslie',
               'Licorice',
               'Lilah',
               'Lola',
               'Marianna',
               'Marilyn',
               'Marsha',
               'Melina',
               'Misty',
               'Molly',
               'Morgan',
               'Natasha',
               'Nell',
               'Olive',
               'Olivia',
               'Paris',
               'Penelope',
               'Phillippa',
               'Phoebe',
               'Piper',
               'Raven',
               'Regina',
               'Roanna',
               'Rosaline',
               'Rosie','Rosie',
               'Roxanne',
               'Ruby',
               'Sable',
               'Sabrina',
               'Saffron',
               'Satin',
               'Scarlett',
               'Sharon',
               'Simone',
               'Sophie',
               'Summer',
               'Svetlana',
               'Sydney',
               'Sylvia',
               'Tonya',
               'Tori',
               'Valentina',
               'Vanessa',
               'Veronica',
               'Viola',
               'Violet',
               'Virginia',
               'Vivienne',
               'Zenobia']
               
class LastNames(WordList):
     def __init__(self):
          super().__init__()
          
          self.List = ["Amalova",
               "Analicker",
               "Anlicker",
               "Bangs","Bangs",
               "Bardot",
               "Beaver","Beaver","Beaver",
               "Beeter",
               "Blush",
               "Bodie",
               "Black",
               "Brest","Bresst",
               "Bottoms",
               "Buhnz",
               "Butts",
               "Cherry",
               "Church",
               "Clozov",
               "Cox",
               "Cracks",
               "Cream",
               "Creamer",
               "Creams",
               "Cummer",
               "Cummings","Cummings",
               "Daley",
               "De Boest",
               "Devlyn",
               "Dick",
               "Dickens",
               "Dicker",
               "Dicter",
               "Dix",
               "Faulks",
               "Fox",
               "Fuchs",
               "Furrows",
               "Goodebody",
               "Goodhead",
               "Gozinya",
               "Grotch",
               "Hancock",
               "Handler",
               "Hard",
               "Harder",
               "Hardin",
               "Head",
               "Hill",
               "Hiscock",
               "Hoar",
               "Holden",
               "Hump",
               "Humper",
               "Hung",
               "Hunt",
               "Hyman",
               "Hunter",
               "Inya",
               "Janus",
               "Jiggles",
               "Johnson",
               "Jones",
               "King",
               "Knight",
               "Knightly",
               "Knockers",
               "Knott",
               "Knox",
               "Knuttz",
               "Koch",
               "Kootch",
               "Krevises",
               "Kuntz",
               "Lace",
               "La Vigne",
               "Lipps",
               "Liquor",
               "Long",
               "Lust",
               "Mandelay",
               "Mann",
               "McCreviss",
               "Mellck",
               "Milfinger",
               "Minx",
               "Moore",
               "Moorecox",
               "Moorehard",
               "Moorehead",
               "Morgan",
               "Mortits",
               "Mount",
               "Mountcox",
               "Mountford",
               "Muncher",
               "Muff",
               "Muffin",
               "Nippell",
               "Oxhard",
               "Peach",
               "Peaches",
               "Pearl",
               "Peckwood",
               "Peters",
               "Philmore",
               "Pohl",
               "Polk",
               "Poppa",
               "Popper",
               "Prince",
               "Quinn",
               "Rack",
               "Red",
               "Rose",
               "Rohdd",
               "Sachs",
               "Sacks",
               "Sax",
               "Schaft",
               "Snatch",
               "Spunk",
               "St. Claire",
               "Steele",
               "Stiffington",
               "Stiffly",
               "Strange",
               "Stroker",
               "Stuffers",
               "Swallows",
               "Sweet",
               "Throat",
               "Topper",
               "Vale",
               "Valentine",
               "Wang",
               "Weiner",
               "White",
               "Wilde",
               "Winters",
               "Wood",
               "Zahara",
               "Zemen"]
               
class AuthorNamesMale(Names):
     def __init__(self):
          super().__init__()
          
          self.FirstNamesList = ['Barry',
               'Ben','Ben',
               'Bill',
               'Buster',
               'Chuck',
               'Deacon',
               'Dewey',
               'Dick','Dick',
               'Dirk',
               'Dixon',
               'Dom',
               'Don',
               'Doug',
               'Drew',
               'Duane',
               'Duke',
               'Earl',
               'Ed',
               'Frank',
               'Gaylord',
               'Grant',
               'Hank',
               'Hans',
               'Harry','Harry','Harry',
               'Holden','Holden',
               'Howie',
               'Hugh','Hugh',
               'Isaac',
               'Ivan',
               'Jack','Jack',
               'Jim',
               'Jimmy',
               'Joe',
               'John',
               'Johnny',
               'Josh',
               'Juan',
               'Justin',
               'Kane',
               'Kenny',
               'Lance','Lance',
               'Lou',
               'Max',
               'Mike','Mike',
               'Miles',
               'Neil',
               'Nick',
               'Oliver','Oliver',
               'Otto',
               'Pat','Pat',
               'Peter','Peter',
               'Phil',
               'Philip',
               'Philmore',
               'Randy',
               'Raoul',
               'Rich','Rich',
               'Rob',
               'Rod',
               'Rusty',
               'Ryder',
               'Sawyer','Sawyer',
               'Seymour','Seymour','Seymour',
               'Tom',
               'Willie','Willie',
               'Woody','Woody',
               'Zeke']     
          
class AuthorNamesFemale(Names):
     def __init__(self):
          super().__init__()
          
          self.FirstNamesList = ['Amanda','Amanda','Amanda',
               'Anita','Anita','Anita','Anita',
               'Anna',
               'Ava',
               'Bobbi',
               'Candy',
               'Carrie',
               'Chastity',
               'Cherry',
               'Crystal',
               'Dixie',
               'Eden',
               'Edith',
               'Fonda',
               'Hilda',
               'Honey',
               'Ida',
               'Ima',
               'Inya','Inya',
               'Issa','Issa',
               'Ivana','Ivana','Ivana','Ivana',
               'Jackie',
               'Kari',
               'Kimmy',
               'Kitty',
               'Lacey',
               'Licorice',
               'Lilah',
               'Lola',
               'Mary',
               'May',
               'Maya',
               'Misty',
               'Molly',
               'Morgan',
               'Nastya',
               'Nell',
               'Olive',
               'Olivia','Olivia',
               'Ophelia','Ophelia','Ophelia',
               'Piper',
               'Princess',
               'Rhoda','Rhoda',
               'Rosie','Rosie',
               'Saffron',
               'Sandy',
               'Satin',
               'Scarlett',
               'Sharon','Sharon','Sharon',
               'Stella',
               'Summer',
               'Tara',
               'Tonya',
               'Violet',
               'Virginia',
               'Wilma']