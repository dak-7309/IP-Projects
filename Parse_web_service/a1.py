from urllib.request import *
from datetime import *

#Name: Daksh Thapar
#Roll no- 2018137
#Section- A
#Group- 1





# function to get weather response

"""
this function is used to return json string from a url- which is obtained here by concatenating strings, also containing location and api key that can be entered
by user to obtain a meaningful- url in the form of a string; data can be interpreted and json string can be returned using urlopen() and webpage.read() functions.
"""

def weather_response(location="Delhi", API_key="2ab136be1543b5789451a5994364c0d3"):
	url_prefix = "http://api.openweathermap.org/data/2.5/forecast?"
	URL = url_prefix + "q=" + location + "&APPID=" + API_key
	webpage = urlopen(URL)
	return str(webpage.read())
	# write your code


# function to check for valid response 

"""
this function takes location and the json string as inputs, then finds the 'location' string in the json string by the reference of the word "name" in the json string
and compares the location entered by user and the location in the json string (the strings are converted to lower case so that the exact names can be compared).
if both these values come out to be equal, then the program returns the string False (i.e. no error), else it returns the string "True".
"""

def has_error(location,json):

	pos_initial=json.index("name")+7
	pos_final=json.index("\"",pos_initial)
	json_name= json[pos_initial:pos_final]

	if json_name.lower()==location.lower():
		return "False"
	else:
		return "True"

	# write your code 


# function to get attributes on nth day

"""
this function takes the json string, the nth day from the present day on which the attributes need to be compared, and the time 't' on that nth day from the present
day as inputs. we are using date.today() and timedelta() functions from the datetime module to add n days to the presesnt date. we check for the required date in
the json string and then find the time t in the string, if the dates and times are as the user demanded, then the temperature in that particular circumstance is 
returned by using the reference of the word "temp" in the json string corresponding to the date and time, and then finding the temperature value through it. if 
it doesnt find the required time for that date, then it breaks the loop.
"""

def get_temperature(json, n=0, t="03:00:00"):

	q = 0
	date_final= str(date.today()+timedelta(days=n))

	while True:

		pos = json.find(t,q)

		if json[pos - 11:pos - 1] == date_final:
			pos_index = json.index("temp", pos - 330)
			comma_index = json.index(",",pos_index)
			q = json.index("name")

			#print("Temperature= ")
			return float(json[pos_index + 6:comma_index])


		elif pos == -1:
			#print("the end")
			break

		else:
			q += 2


# write your code

"""
this function takes the json string, the nth day from the present day on which the attributes need to be compared, and the time 't' on that nth day from the present
day as inputs. we are using date.today() and timedelta() functions from the datetime module to add n days to the presesnt date. we check for the required date in
the json string and then find the time t in the string, if the dates and times are as the user demanded, then the humidity in that particular circumstance is 
returned by using the reference of the word "humidity" in the json string corresponding to the date and time, and then finding the humidity value through it. if 
it doesnt find the required time for that date, then it breaks the loop.
"""

def get_humidity(json, n=0, t="03:00:00"):

	q = 0
	date_final = str(date.today() + timedelta(days=n))

	while True:

		pos = json.find(t,q)

		if json[pos - 11:pos - 1] == date_final:

			pos_index = json.index("humidity", pos - 330)
			comma_index = json.index(",", pos_index)
			q = json.index("name")

			#print("Humidity= ")
			return float(json[pos_index + 10:comma_index])

		elif pos == -1:
			#print("the end")
			break

		else:
			q += 2


# write your code

"""
this function takes the json string, the nth day from the present day on which the attributes need to be compared, and the time 't' on that nth day from the present
day as inputs. we are using date.today() and timedelta() functions from the datetime module to add n days to the presesnt date. we check for the required date in
the json string and then find the time t in the string, if the dates and times are as the user demanded, then the pressure in that particular circumstance is 
returned by using the reference of the word "pressure" in the json string corresponding to the date and time, and then finding the pressure value through it. if 
it doesnt find the required time for that date, then it breaks the loop.
"""

def get_pressure(json, n=0,t="03:00:00"):

	q = 0
	date_final = str(date.today() + timedelta(days=n))

	while True:

		pos = json.find(t,q)

		if json[pos - 11:pos - 1] == date_final:

			pos_index = json.index("pressure", pos - 330)
			comma_index = json.index(",", pos_index)
			q = json.index("name")

			#print("Pressure= ")
			return float(json[pos_index + 10:comma_index])

		elif pos == -1:
			#print("the end")
			break

		else:
			q += 2



# write your code

"""
this function takes the json string, the nth day from the present day on which the attributes need to be compared, and the time 't' on that nth day from the present
day as inputs. we are using date.today() and timedelta() functions from the datetime module to add n days to the presesnt date. we check for the required date in
the json string and then find the time t in the string, if the dates and times are as the user demanded, then the wind speed in that particular circumstance is 
returned by using the reference of the word "speed" in the json string corresponding to the date and time, and then finding the wind speed value through it. if 
it doesnt find the required time for that date, then it breaks the loop.
"""

def get_wind(json, n=0,t="03:00:00"):
	q = 0
	date_final = str(date.today() + timedelta(days=n))

	while True:

		pos = json.find(t, q)

		if json[pos - 11:pos - 1] == date_final:

			pos_index = json.index("speed", pos - 330)
			comma_index = json.index(",", pos_index)
			q = json.index("name")

			#print("Wind Speed= ")
			return float(json[pos_index + 7:comma_index])

		elif pos == -1:
			#print("the end")
			break

		else:
			q += 2


# write your code

"""
this function takes the json string, the nth day from the present day on which the attributes need to be compared, and the time 't' on that nth day from the present
day as inputs. we are using date.today() and timedelta() functions from the datetime module to add n days to the presesnt date. we check for the required date in
the json string and then find the time t in the string, if the dates and times are as the user demanded, then the sea level in that particular circumstance is 
returned by using the reference of the word "sea_level" in the json string corresponding to the date and time, and then finding the sea level value through it. if 
it doesnt find the required time for that date, then it breaks the loop.
"""


def get_sealevel(json, n=0,t="03:00:00"):
	q = 0
	date_final = str(date.today() + timedelta(days=n))

	while True:

		pos = json.find(t, q)

		if json[pos - 11:pos - 1] == date_final:

			pos_index = json.index("sea_level", pos - 330)
			comma_index = json.index(",", pos_index)
			q = json.index("name")

			#print("Sea Level= ")
			return float(json[pos_index + 11:comma_index])

		elif pos == -1:
			#print("the end")
			break

		else:
			q += 2
	# write your code




