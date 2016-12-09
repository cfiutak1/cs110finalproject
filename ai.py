import random
import math
class AI:

	def refineOdds(self, minodds, maxodds, rawodds, tocall, currentvalue, betround, bigblind, numplayers):
		self.minodds = minodds
		self.rawodds = rawodds
		self.maxodds = maxodds
		if tocall > currentvalue:
			self.tocall = currentvalue
		elif tocall <= currentvalue:
			self.tocall = tocall
		self.currentvalue = currentvalue
		self.betround = betround
		self.bigblind = bigblind
		self.numplayers = numplayers
		
		if self.betround == "preflop":
			#Refines the odds of playing by taking the curent raw odds, the max % possible (~50% with pocket aces and 4 players preflop), and the number of players and basing the odds of playing the hand on an exponential scale. For example, 2-7 unsuited has a 4% chance of calling and pocket aces has a ~99% chance of calling.
			self.oddsofplaying = (math.exp(self.rawodds*self.numplayers)/math.exp(self.maxodds*self.numplayers)) ** (2/3)
			

			if self.oddsofplaying <= 0.2:
				self.oddsofplaying = self.oddsofplaying ** 4
				
			elif 0.2 < self.oddsofplaying <= 0.25:
				self.oddsofplaying = self.oddsofplaying ** (1/1.5)

			elif 0.25 < self.oddsofplaying <= 0.4:
				self.oddsofplaying = self.oddsofplaying ** (1/3.75)
				
			elif 0.4 < self.oddsofplaying:
				self.oddsofplaying = self.oddsofplaying ** (1/6)
				

			#Takes into consideration the amount that is required to call vs. the stash of the player if the refined odds are less than 80%
			if self.oddsofplaying < 0.8:
				self.oddsofplaying = self.oddsofplaying - (self.oddsofplaying * (math.log(self.tocall)/math.log(self.currentvalue)) ** ((self.rawodds/self.minodds) ** 4.13))
				
			#Converts to a scale out of 100      
			self.oddsofplaying = self.oddsofplaying * 100
			self.oddsofplaying = int(self.oddsofplaying) + 1
			
			

		elif self.betround == "postflop" or "postturn" or "postriver":
			self.oddsofplaying = (math.exp(self.rawodds*self.numplayers)/math.exp(self.maxodds*self.numplayers)) ** (1/3.2)

			if self.oddsofplaying <= 0.2:
				self.oddsofplaying = self.oddsofplaying ** 1.87
					
			elif 0.2 < self.oddsofplaying <= 0.40:
				self.oddsofplaying = self.oddsofplaying
					
			elif 0.40 < self.oddsofplaying <= 0.70:
				self.oddsofplaying = self.oddsofplaying ** (1/2)
					
			elif 0.70 < self.oddsofplaying <= 1:
				self.oddsofplaying = self.oddsofplaying ** (1/9)
		
			#Takes into consideration the amount that is required to call vs. the stash of the player. Only if processed odds < 80%
			if self.oddsofplaying < .8:
				self.oddsofplaying = self.oddsofplaying - (self.oddsofplaying * (math.log(self.tocall + 1)/math.log(self.currentvalue + 1)) ** ((self.rawodds/self.minodds) ** 4.13))
			  
			self.oddsofplaying = self.oddsofplaying * 100
			self.oddsofplaying = int(self.oddsofplaying) + 1
			
		return self.oddsofplaying
		
		
	def aiDecision(self, oddsofplaying, personality):
		self.personality = personality
		
		if self.personality == "tightaggressive":
			if self.oddsofplaying <= 37:
				return "Fold"
				

			elif 37 < self.oddsofplaying <= 60:
				myvar = random.randrange(101)
				if myvar < 30:
					return "Fold"
				
				elif myvar >= 30:
					return "Call"
			
			elif 60 < self.oddsofplaying <= 70:
				return "Call"
			
			elif 70 < self.oddsofplaying <= 77:
				myvar = random.randrange(101)
				if myvar < 50:
					return "Call"
				
				elif 50 <= myvar < 87:
					return "Raise2BB"
				
				elif myvar >= 87:
					return "Raise3BB"
			
			elif 77 < self.oddsofplaying <=85:
				myvar = random.randrange(101)
				if myvar < 25:
					return "Call"
				
				elif 25 <= myvar < 75:
					return "Raise2BB"
					
				elif 75 <= myvar < 87:
					return "Raise3BB"
				
				elif myvar >= 87:
					return "RaisePot"
					
			elif self.oddsofplaying > 85:
				myvar = random.randrange(101)
				
				if myvar < 33:
					return "Raise2BB"
				
				elif 33 <= myvar < 66:
					return "Raise3BB"
					
				elif 66 <= myvar < 85:
					return "RaisePot"
					
				elif myvar >= 85 and self.currentvalue < 2500:
					return "AllIn"
				
				elif myvar >= 85:
					return "RaisePot"
		
		elif self.personality == "looseaggressive":
			if self.oddsofplaying <= 15:
				return "Fold"
				
			elif 15 < self.oddsofplaying <= 30:
				myvar = random.randrange(101)
				if myvar < 30:
					return "Fold"
				
				elif myvar >= 30:
					return "Call"
			
			elif 30 < self.oddsofplaying <= 70:
				return "Call"
			
			elif 70 < self.oddsofplaying <= 77:
				myvar = random.randrange(101)
				if myvar < 50:
					return "Call"
				
				elif 50 <= myvar < 87:
					return "Raise2BB"
				
				elif myvar >= 87:
					return "Raise3BB"
			
			elif 77 < self.oddsofplaying <= 85:
				myvar = random.randrange(101)
				if myvar < 25:
					return "Call"
				
				elif 25 <= myvar < 75:
					return "Raise2BB"
					
				elif 75 <= myvar < 87:
					return "Raise3BB"
				
				elif myvar >= 87:
					return "RaisePot"
					
			elif self.oddsofplaying > 85:
				myvar = random.randrange(101)
				
				if myvar < 33:
					return "Raise2BB"
				
				elif 33 <= myvar < 66:
					return "Raise3BB"
					
				elif 66 <= myvar < 85:
					return "RaisePot"
					
				elif myvar >= 85 and self.currentvalue < 2500:
					return "AllIn"
				
				elif myvar >= 85:
					return "RaisePot"

		elif self.personality == "loosepassive":
			if self.tocall > self.bigblind * 3:
				if self.oddsofplaying < 85:
					return "Fold"
				elif self.oddsofplaying >= 85:
					return "Call"
	
			elif self.tocall < self.bigblind * 3:        
				if self.oddsofplaying <= 50:
					return "Fold"
					
				elif 50 < self.oddsofplaying <= 70:
					myvar = random.randrange(101)
					if myvar < 30:
						return "Fold"
					
					elif myvar >= 30:
						return "Call"
				
				elif 70 < self.oddsofplaying <= 77:
					return "Call"
				
				elif 77 < self.oddsofplaying <= 85:
					myvar = random.randrange(101)
					if myvar < 75:
						return "Call"
					
					elif myvar >= 75:
						return "Raise2BB"
				
				elif self.oddsofplaying > 85:
					myvar = random.randrange(101)
					if myvar < 25:
						return "Call"
					
					elif 25 <= myvar < 75:
						return "Raise2BB"
						
					elif myvar >= 75:
						return "Raise3BB"

		elif self.personality == "tightpassive":
			if self.tocall > self.bigblind * 3:
				if self.oddsofplaying < 85:
					return "Fold"
				elif self.oddsofplaying >= 85:
					return "Call"
	
			elif self.tocall < self.bigblind * 3:        
				if self.oddsofplaying <= 50:
					return "Fold"
					
				elif 50 < self.oddsofplaying <= 70:
					myvar = random.randrange(101)
					if myvar < 30:
						return "Fold"
					
					elif myvar >= 30:
						return "Call"
				
				elif 70 < self.oddsofplaying <= 77:
					return "Call"
				
				elif 77 < self.oddsofplaying <= 85:
					myvar = random.randrange(101)
					if myvar < 75:
						return "Call"
					
					elif myvar >= 75:
						return "Raise2BB"
				
				elif self.oddsofplaying > 85:
					myvar = random.randrange(101)
					if myvar < 25:
						return "Call"
					
					elif 25 <= myvar < 75:
						return "Raise2BB"
						
					elif myvar >= 75:
						return "Raise3BB"
	
		elif self.personality == "loosepassive":
			if self.tocall > self.bigblind * 3:
				if self.oddsofplaying < 85:
					return "Fold"
				elif self.oddsofplaying >= 85:
					return "Call"
	
			elif self.tocall < self.bigblind * 3:       
	  
				if self.oddsofplaying <= 70:
					return "Call"
				
				elif 70 < self.oddsofplaying <= 85:
					myvar = random.randrange(101)
					if myvar < 75:
						return "Call"
					
					elif myvar >= 75:
						return "Raise2BB"
				
				elif self.oddsofplaying > 85:
					myvar = random.randrange(101)
					if myvar < 25:
						return "Call"
					
					elif 25 <= myvar < 75:
						return "Raise2BB"
						
					elif myvar >= 75:
						return "Raise3BB"

		elif self.personality == "madman":
			if self.oddsofplaying < 35:
				myvar = random.randrange(101)
		
				if myvar <= 50:
					return "Call"
		
				elif myvar > 50:
					return "Raise2BB"
		
			elif 35 <= self.oddsofplaying < 50:
				return "Raise2BB"
		
			elif 50 <= self.oddsofplaying < 66:
				myvar = random.randrange(101)
		
				if myvar <= 50:
					return "Raise3BB"
		
				elif myvar > 50:
					return "RaisePot"
		
			elif self.oddsofplaying >= 66:
				myvar = random.randrange(101)
				if myvar <= 30:
					return "RaisePot"
				elif myvar > 30:
					return "AllIn"
'''
def main():
	ai = AI()
	refineOdds(self, minodds, maxodds, rawodds, tocall, currentvalue, betround, bigblind, numplayers)
	'''