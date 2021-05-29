"' Build a dataframe in pandas
import pandas as pd

def test_run():
	#Define date range
	start_date='2010-01-22'
	end_date='2010-01-26'
	dates=pd.date_range(start_date,end_date)

	#Create an empty dataframe
	df1=pd.DataFrame(index=dates)

	#Read SPY data into temporary dataframe

	dfSPY = pd.read_csv("data/SPY.csv",index_col="Date",
	parse_dates=True,usecols=['Date','Adj Close'],
	na_values=['nan'])
	
	#Rename 'Adj Close' column to 'SPY' to prevent clash
	dfSPY = dfSPY.remane(colums={'Adj Close':'SPY'})

	#Join the two dataframes using DataFrame.join()
	df1=df1.join(dfSPY,how='inner')
    
    	#Read in more stocks
	symbols = ['GO0G', 'IBM', 'GLD']
	for symbol in symbols:
		df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date'
		parse_dates=True,usecols=['Date', 'Adj Close']
		,na_values=['nan'])
                df_temp = df_temp.remane(colums={'Adj Close':symbol})
		df1=df1.join(df_temp) #use default how="'Left'
		
	print df1

if __name__ == "__main__":
    test_run()
