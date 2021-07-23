
date = (input("Enter date in YYYY-MM-DD format").split("-"))
print(date)


year = int(date[0])
age = 2021 - year 
convert_age = list(str(age))
num_candles=int(convert_age[-1])
print(num_candles)

if num_candles % 2 == 0:
	half_candle = num_candles//2
	candle_string = "i" * half_candle + "_" + "i" * half_candle
else:
	candle_string = "i" * num_candles

num_space = 11- len (candle_string)
candle_string += '_' * (num_space//2)
candle_string  =  '_' * (num_space//2) + candle_string





print (f""" 
              {candle_string}     
             |:H:a:p:p:y:|
           __|___________|__
          |^^^^^^^^^^^^^^^^^|
          |:B:i:r:t:h:d:a:y:|
          |                 |
          ~~~~~~~~~~~~~~~~~~~"""
	     )
