#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
 
import sys, argparse, datetime, threading, traceback

from io import BytesIO
from random import *
from title.util import *
from title.generators import *
from title.tweettext import *
from title.twitter_stuff import *
	
def InitBot(iTweetTimer, bTweet = False, iTweets = 1, bLoop = False, iGeneratorNo = -1, iTweetTxtNo = -1):
	print("=*=*=*= EROTICA_EBOOKS BOT IS RUNNING (@erotica_ebooks) =*=*=*=\n\n")
	print("===InitBot() iTweetTimer=" + str(iTweetTimer) + ", bTweet=" + str(bTweet) + ", iTweets=" + str(iTweets) + ",bLoop=" + str(bLoop) + ",iGeneratorNo=" + str(iGeneratorNo) + "\n")
	
	sTweet = ""
	bTest = False 
	
	TweetHistoryQ = HistoryQWithLog(HISTORYQ_FILENAME)
	TweetTxtHistoryQ = HistoryQWithLog(TWEETTXT_HISTORYQ_FILENAME, iQSize = 4)
	
	try:
		api = InitTweepy()
		
		if iGeneratorNo == -1:
			iGeneratorNo = MAX_GENERATOR_NO
		else:
			bTest = True
		i = 0
		while i in range(0,iTweets) or bLoop:
			# Tweets = [1]
			Gen = None 
			sTweet = ""
			sText = ""
			
			sTweet = GetTweet(bTest, bTweet, iGeneratorNo, bAllowPromo = True, TweetHistoryQ = TweetHistoryQ)
			
			if len(sTweet) > 0:
				sText = GetImgTweetText(bTest = False, TweetTxtHistoryQ = TweetTxtHistoryQ)
				
				print("\n===Here is your " + str(len(sTweet)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
				print("[" + sTweet + "]")
				if len(sText) > 0:
					print("Tweet text: [" + sText + "]")
					# print(misc.TweetReplyBuilder().GetReply())
					
				currentDT = datetime.datetime.now()
				
				print("Preparing to create image.")
				ImgFile = BytesIO() 
				CreateImg(sTweet).save(ImgFile, format = 'PNG')
				print("Image created.")
				if bTweet:
					print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
						
					status = None
						
					if status == None:
						# pass
						# status = UpdateStatus(api, tweet)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet)
						else:
							status = UpdateStatusWithImage(api, sText, ImgFile)		
					else:
						# pass
						# status = UpdateStatus(api, tweet, status.id)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet, status.id)
						else:
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sText, ImgFile, status.id)	
					
					TweetHistoryQ.LogHistoryQ()
					TweetTxtHistoryQ.LogHistoryQ()
					
	
				# else:
					# with open(GenerateFileName(), 'wb') as file:
						# file.write(ImgFile.getvalue())
			i += 1
		
		# Look for replies from controller Twitter account
		print("Looking for 'more' requests from controller account.")
		RespondToMoreRequests(api, TWIT_CONTROLLER)
		
		# Look for replies from controller indicating that a suggestion is a favorite
		print("Looking for 'yes' tweet favs from controller account.")
		SaveFavorites(api, TWIT_CONTROLLER)
	except KeyboardInterrupt:
		print("Ending program ...")
	finally:
		# e.set()
		
		print("***Goodbye***")


