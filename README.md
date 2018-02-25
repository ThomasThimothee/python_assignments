How to execute the program:
1 - clone/download our project in your desired local repository, we use a modified version of the webget module created in class, this modified webget module is provided in our project.
2 - In your Command Prompt / Terminal, navigate to the correct repository 
3 - type: python bg_assignment_1.py https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls

notes: our program gives as output several graphs as well as a text output in the command prompt / terminal. The display of each graph is a "blocking call" meaning that you will need to close the diagram window in order to see the next one.
Stretch-out the window of the graphs to see more clearly the information displayed.


Results:

Question 1 : Has the crime decreased or increased over the last 20 years?
To answer this question we decided to use a line graph. We can see on the output graph that the line is clearly going down.
So we conclude that from 1994 to 2013, the total number of crime decreased

Question 2 : Has the type of crime changed?
During the group presentation we got additional information. We were asked to observe the evolution of the type of crime commited on a 10 year basis. We have data for the years from 1994 to 2013, so we studied the years 1994-2004 and 2013. To try to get an answer to the question we decided to use 3 pie-charts. We can see in these charts that the types of crime have not changed

Question 3: Has the crime moved to from one area to another?
In order to answer this question we should have had access to data over time, however we have access to the crimes per state only for the year 2013. With this information we decided to display a histogram to visualize total amount of crime per state. If we had access to this data over time, we would have been able to display a 3D histogram where we would have been able to see if some state recorded an increase while others recorded a decrease of total number of crime

Question 4: Is there a connection between type of crimes and locations?
To answer this question we decided to output a Text in the terminal/Command prompt. 
In this dictionary you can see the 3 most "popular" types of crime per state. We could see that for almost all states, the 3 most popular types of crime in 2013 were Property crime, Larceny theft and Burglary. ONLY in DISTRICT OF COLUMBIA there is more Violent crime than Burglary. So no, we don't see a connection between type of crimes and locations.

Question 5: Which year was the most crime and what crime occured most times?
To answer this question we decided to display two histograms. The first shows that the year with highes number of crime was 1994. The second show that the most popular type of crime in 1994 was property crime.

