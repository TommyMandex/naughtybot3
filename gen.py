#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class module

from random import *
from util import *

MAXBUCKETTRIES = 100

class Generator():
    def __init__(self, 
                 ID = -1, 
                 Priority = GenPriority.Normal, 
                 Type = GeneratorType.Normal, 
                 Disabled = False, 
                 sTxt = ""):

        # each generator should have a unique ID
        self.ID = ID

        # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
        self.Priority = Priority

        # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
        self.GeneratorType = GeneratorType

        # disabled = true disables the generator so it cannot be selected
        self.Disabled = Disabled 

        # the generated text
        self.Txt = sTxt

        # normal / promo / test
        self.Type = Type

    def Generate(self):
        self.Txt = self.GenerateTxt()

    # this will be overridden by most generators but this is how it should look
    def GenerateTxt(self):
        sTxt = ""

        return sTxt


class GeneratorContainer():
    def __init__(self, GeneratorClass, iFirstID = 1, HistoryQ = None):
        super().__init__()  # just in case

        GeneratorObj = GeneratorClass()
        self.GeneratorClassName = str(type(GeneratorObj).__name__)

        # The optional history q
        if not HistoryQ is None:
            self.HistoryQ = HistoryQ
        else:
            self.HistoryQ = None

        # List of unique generators 
        self.GeneratorList = []

        # Buckets of prioritized generators for random selection
        self.BucketLowest = []
        self.BucketLow = []
        self.BucketNormal = []
        self.BucketAboveAverage = []
        self.BucketHigh = []
        self.BucketSuperHigh = []

        # If generator IDs are not given the container will add them
        self.NextGenID = iFirstID

        # Build generator list
        for subclass in GeneratorClass.__subclasses__():
            item = subclass()
            if not item.Disabled:
                if item.ID == -1:
                    item.ID = self.NextGenID

                self.AddGenerator(item, item.Priority)
                self.NextGenID = item.ID + 1

        # Validate generator list
        self.ValidateGenIDs()

        # Print list (uncomment for debugging)
        #self.PrintGeneratorList()

        #print(self.GeneratorClassName + " Priority Buckets:")
        #print(" * Lowest priority bucket has " + str(len(self.BucketLowest)) + " items")
        #print(" * Normal priority bucket has " + str(len(self.BucketNormal)) + " items")
        #print(" * Above Average priority bucket has " + str(len(self.BucketAboveAverage)) + " items")
        #print(" * High priority bucket has " + str(len(self.BucketHigh)) + " items")
        #print(" * Super High priority bucket has " + str(len(self.BucketSuperHigh)) + " items")

    def AddGenerator(self, Gen, Priority = GenPriority.Normal):
        bResult = False 

        if Priority == GenPriority.Lowest:
            self.BucketLowest.append(Gen)
        elif Priority == GenPriority.Low:
            self.BucketLow.append(Gen)
        elif Priority == GenPriority.AboveAverage:
            self.BucketAboveAverage.append(Gen)
        elif Priority == GenPriority.High:
            self.BucketHigh.append(Gen)
        elif Priority == GenPriority.SuperHigh:
            self.BucketSuperHigh.append(Gen)
        else:
            self.BucketNormal.append(Gen)
        self.GeneratorList.append(Gen)

        bResult = True

        return bResult 

    # Get an individual generator by ID or class name
    def GetGenerator(self, GenID):
        Generator = None 

        if len(self.GeneratorList) > 0:
            if isinstance(GenID, int):
                for gen in self.GeneratorList :
                    if gen.ID == GenID:
                        Generator = gen
                        break
            elif isinstance(GenID, str):
                for gen in self.GeneratorList :
                    if type(gen).__name__ == GenID:
                        Generator = gen
                        break

                         
        return Generator

    # Get list of generators
    def GetGeneratorList(self):
        return self.GeneratorList  

    def PrintGeneratorList(self):
        sTxt = ""

        sTxt = "List of generators for " + str(self) + ":\n\n"
        if len(self.BucketLowest) > 0:
            for gen in self.GeneratorList:
                sTxt += " * " + self.GeneratorClassName + " | \tID # " + str(gen.ID) + " | \t" + str(gen.Priority)
                sTxt += "\n"

        print(sTxt)

    # Get list of prioritized generators
    def GetSelectorList(self):
        return self.SelectorList

    def GetBucket(self):
        Bucket = []

        
        #print("Selecting priority bucket for " + str(self.GeneratorClassName))

        iCount = 0
        while len(Bucket) == 0 and iCount < MAXBUCKETTRIES:
            iChance = randint(1, 57)                                # 1 + 2 + 3 + 4 + 5 = 15

            if iChance == 1:
                Bucket = self.BucketLowest
                #print(" Lowest bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance >= 2 and iChance < 4:      # 2x
                Bucket = self.BucketLow 
                #print(" Normal bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance >= 4 and iChance < 8:      # 2x
                Bucket = self.BucketNormal 
                #print(" Normal bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance >= 8 and iChance < 16:      # 3x
                Bucket = self.BucketAboveAverage
                #print(" AboveAverage bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance >= 16 and iChance < 32:     # 4x
                Bucket = self.BucketHigh
                #print(" High bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance >= 32 and iChance < 58:    # 5x
                Bucket = self.BucketSuperHigh
                #print(" SuperHigh bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            else:
                Bucket = self.BucketNormal
                print(" WARNING: Default bucket (normal) selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")

            iCount = iCount + 1

        return Bucket

    # Get a random generator
    def RandomGenerator(self, bAllowPromo = True, Type = None):
        Generator = None 
        AllowedTypes = []
        Bucket = []
          
        if not Type is None:
            AllowedTypes = [Type] 
        else:
            AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
        if bAllowPromo:
            AllowedTypes.append(GeneratorType.Promo)

        Bucket = self.GetBucket()
        while len(Bucket) == 0 or Generator == None or not Generator.Type in AllowedTypes:
            Bucket = self.GetBucket()
            if len(Bucket) > 0:
                Generator = choice(Bucket)
                    
        return Generator 

    def GetGeneratorsSequential(self, bAllowPromo = True, Type = None):
          GeneratorList = []
          AllowedTypes = []
          
          if not Type is None:
               AllowedTypes = [Type] 
          else:
               AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
          if bAllowPromo:
               AllowedTypes.append(GeneratorType.Promo)

          for gen in self.GeneratorList:
               if gen.Type in AllowedTypes:
                    GeneratorList.append(gen)
               
          return GeneratorList     

    def ValidateGenIDs(self):
        bValid = True

        IDList = []

        if len(self.GeneratorList) > 0:
            for gen in self.GeneratorList:
                if gen.ID in IDList:
                    print("=*= WARNING =*= " + self.GeneratorClassName + " ID # " + str(gen.ID) + " has a duplicate.\n")
                    bValid = False
                else:
                    IDList.append(gen.ID)

        return bValid



