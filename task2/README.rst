Task2
=====

Titles from movies released between 1990 and 2018
(inclusive) with an average rating greater equal 7.5 and
at least 500,000 votes.


Output
------

\[title\]


Additional information
----------------------

* titleType == "movie"

* title := primaryTitle


Data sources
------------

* title.basics.tsv

* title.ratings.tsv


Mapper
======


Process basic
-------------

For each valid line which represents a move released
in (1990, 2018) return \[tnum, title\].


Process rating
--------------

For each line having an average of at least 7.5 and at
least 500,000 votes return \[tnum\].


Reducer
=======

Prints each move title which has two lines. Only movies
which fulfill the defined criterias are represented by
two lines, since the movie from title.ratings.tsv is
otherwise omitted.


