So I was playing outpost (https://boardgamegeek.com/boardgame/1491/outpost) a few days ago.
I got bored of having to calculate all possible values that I could bid with my current resources
and wondered if there was a practical way to simple print the values I can bid with the combinations
or cards used.

It turns out it is a good match for using Dynamic programing to build all the solutions in a list 
in Python. I had some free time and figured out it would be a fun exercise to practice some python.

Basically, the solution is built one by one by backtracking from the previous position of all lists
created in a previous step. So it looks for lists with one elements, then lists with 3 elements and
so on, until we have all lists that can be created with the input numbers (card values from Outpost).

I know I have to do some tuning, as once I hit 25 itens it get a bit slow in my PC, but It is unlikely
that a player will have a hand of more than 15 to 20 cards, so for the purpose it was built, it provides
a reasonable response time.

I hope somebody has fun with it.

PS - for some reason, the appends kept creating lists within lists, so I simply used pandas flatten function
to collapse each list of lists into a single list and generate the output.
