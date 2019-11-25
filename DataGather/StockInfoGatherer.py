from Auth.OAuth import OAuthContext

class DataSponge:
	def __init__(self):
		self.Auth = OAuthContext()
		
	def Get30DayStockPrice(self, date):
		return

	def Get30DayMacD(self, date):
		return
	def Get30DayMovingAverage(self, date):
		return 
	def Get30DayRSIValue(self, date):
		return 	
	def Get30DayChalkinsVolatility(self, date):
		return 
	def Test(self, param):
		self.json = self.Auth.GetParameter(param)
		return self.json