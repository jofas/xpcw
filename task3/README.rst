Task3
=====

Print the top rated movie for each genre for each decade
of the 20th century.


Output
------

\[decade|genre|title\]


Additional information
----------------------

* titleType == "movie"

* output sorted by decade, genre

* if two or more top rated movies: 1st in alphabetical
  order


Data sources
------------

* title.basics.tsv

* title.ratings.tsv


Mapper
======


Process basic
-------------

For each valid line which represents a movie from the
20th century return \[tnum, title, genres, decade\].


Process rating
--------------

For each line return \[tnum, avg\].


Reducer
=======

Concatenates rating entries with basic entries. Splits
the genres field of the basic entry and for each genre
returns \[decade, genre, avg, title\]


Mapper 2
========

In-mapper combiner for reducing network traffic.

For each decade and genre, the title with the best rating
is saved and the others are disregarded.

Returns \[decade, genre, avg, title\].


Reducer 2
=========

*Important:* The input is sorted and partitioned, so that
for each decade and genre the highest rated movie is the
first entry (alphabetically ordered if rating is the
same). Therefore the task is accomplished by simply
printing the first entry by decade and genre.


