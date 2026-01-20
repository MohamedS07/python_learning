def birthdayCakeCandles(candles):
	    if candles == []:
	        print("Invalid")
	    else:
	        count=0
	        a = max(candles)
	        for i in range(len(candles)):
	            if candles[i]==a:
	                count+=1
	        print(count)
	
birthdayCakeCandles([4,4,1,3])