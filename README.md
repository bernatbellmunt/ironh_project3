# IRONHACK PROJECT 3
Bernat Bellmunt Cabutí

Well after several rounds of investements and multiple months working on remote, I need to find an office for my new gaming company **Catacrack Gaming**.

![](images/future-gaming.gif)


After asking my employees this are the conclusions:
 
- Close to Starbucks
- Close to Schools
- Close to the Airport
- Close to Vegan Restaurants (because, I'm vegan)
- Close to a Basketball stadium
- City with good night life
- Close to a Pet Saloon, because we have a dog 🐶
- Presence of Design Companies in my city
- Presence of successful tech startups

As I want the best for employees, I will add too, the average wage / cost of live into my formula.

**Knowing all this, lets find our best office!**

![](images/E3xX.gif)


## How to proceed?

The aim of my exercise is to obtain a specific value for each of my potential localizations, named RANK.

In order to calculate the rank I have done the following:
1. Obtain from MongoDB companies all the gaming companies registered and extracted name, city, country, latitude and longitude.

![](images/Screenshot%202022-10-31%20at%2018.36.43.png)



2. Get the number of design companies per city and number of successfull tech startups in the city

![](images/Screenshot%202022-10-31%20at%2018.38.09.png)



3. Now that I know if there are these types of companies in my city I will proceed to calculate the following using Foursquare API calls:
- Distance to the closest Starbucks
- Distance to the airport
- Average distance to near clubs
- Average distance to close schools
- Average distance to near vegan restaurants
- Distance to closest basketball court
- Distance to closest pet saloon

![](images/Screenshot%202022-10-31%20at%2018.42.12.png)


4. Now, I must merge into the table the data for cost of living index and average wage, extracted from the following websites:

    "https://www.numbeo.com/cost-of-living/rankings.jsp" and "https://www.numbeo.com/cost-of-living/city_price_rankings?itemId=105"


5. My output table will look like this:

![](images/Screenshot%202022-10-31%20at%2018.44.54.png)


Once the oput table is ready we can calculate the rank value for each of my offices and sort it to get the best one...

My formula is the following:

Rank =  10 + row["nº design comp"] * 20/87 * 0.1 + row["nº tech (>$1M)"] * 15/87 * 0.1 - row["dist to starbucks (km)"] * 10/87 * 0.1 - row["dist to airport (km)"] * 20/87 *0.15 - row["average dist to clubs (km)"] * 87/87 * 0.1 - row["average dist to vegan rest. (km)"]*1/87 * 0.05 - row["average dist to schools (km)"] * 26/87 * 0.1 - row["dist. to closes basketball court (km)"]*1/87 *0.05 - row["dist. to closest canine salon (km)"]*1/87 * 0.05 - row["cost living index"] / row["avg_wage"] * 87/87 * 0.2

Once we sort by rank, our city is...

![](images/San_Francisco_from_the_Marin_Headlands_in_August_2022.jpeg)
**San Francisco, California**

![](images/Screenshot%202022-10-31%20at%2018.49.48.png)

Our office will be located in the following direction:
*3258-3300 21st St, San Francisco, CA 94110, USA*

This office meets all the criteria:

![](images/Screenshot%202022-10-31%20at%2018.51.48.png)

![](images/Screenshot%202022-10-31%20at%2018.53.02.png)

![](images/Screenshot%202022-10-31%20at%2018.54.21.png)

I'm looking forward to seeing you all in our new offices!!