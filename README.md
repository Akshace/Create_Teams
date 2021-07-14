
## Choosing Teams	

# Problem Statement :

<p align=justify>The problem was to create groups of users based on their preferences, for eg. each user might want a team of size (1-3) and request for specific teammates.
Each student might not get his/her preferred choice of team, which will result in the number of complains increasing. Our goal is too create such groups 
which will minimize the number of complains.</p>

## Our understanding :

<p align=justify>We have to search for possible groups of users, whilst calculating the complains associated with each groups creation. We can store the groups and complains
value, in a **heapq** which will pop the lowest complain value once it is pushed in heapq. Main challenge is to figure out the best search technique which
can take into consideration the preferences of students and proceed the search based on input of preferences.</p>

## Approach :

<p align=justify>Our approach to this problem is a little different from traditional search algorithms, we are using **pandas correlation matrix** to generate values which depict the compatibility between two users based on their preferences.</p>

The preferences has been converted into ratings using **random.randint** with cases like - 
<ol>
 <li> User want to work alone gets 9,10 rating on his/her position in the list of users.</li>
<li> All preferred users will get rating (6-8) with respect to the concerened user.</li>
<li> All users which were specificaly not requested by the user will get (0-2) rating.</li>
<li> All remaining users will get rating (3-5).</li>
</ol>
This process will create a list of lists which will have ratings of users concerened with each user.

<p align=justify> Next, we proceed to create a correlation matrix using this data. The correlation matrix generated will have values indicating the compatibility of user with 
every other user. This will help us in creating groups as the higher value users will be grouped with concerned users.</p>

Also, we have set conditions to limit the group length to 3, so we will create required groups based on data from correlation matrix.

Now the groups created will be pushed into the heapq which will keep track of count of complains associated with each group.

Once the pop is called, the group with lowest complain will be popped and result is displayed.

All this process takes place inside a **timed while loop set to 20 seconds**, when it completes, the heappop is executed.  
<p align=justify> For easily accesing the member preference and the person they dont want to work with. While reading the file we are making two different dictionaries for preferred members and dontwant members. These dictionaries are being accessed when we need to calculate the complains for a given team, the length of preferred dictionary list is being used to calculate the complains based on the size of the teams. The members of the preferred list are being used to calculate the complains based on whether the right members are being assigned or not. In this loop we are also taking care of the members who want random assignment. In the last loop of the complains function we are calculating the number of complains based on the assignment where the member is assigned a team which he doesn't want to work with. For this loop the dont want dictionary is being used. While returning the complains we are summing all the complains and returning a single integer value which will give us the exact complains of the input team combination</p>
Challenges:
<ul>
 <li> Biggest challenge was finding the complains of the given combination of the team </li>
 <li> In our problem we are using the correlation matrix so it was a bit tricky to decide the range of the random variables while creating the correlation matrix</li> 
 <li> The final challenge was extracting the values from the correlation matrix and converting it into team combinations</li>  
 </ul>
