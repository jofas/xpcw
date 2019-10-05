Task4
=====

Print the top 10 most popular writers (based on the
amount of votes for their most voted title).


Output
------

\[votes|writer\]


Additional information
----------------------

* writer must be in crew for the movie

* output in descending order (no dublicate writers)


Data sources
------------

* title.rating.tsv

* title.crew.tsv

* name.basics.tsv


Mapper
======


Process names
-------------

For every valid line, check if person is a writer and
for each title the writer is associated with return
\[tnum, nconst, name, "name"\].


Process rating and crew
-----------------------

For every valid line return \[tnum, num_votes/writers,
"rating"/"crew"\].


Reducer
=======

Accumulate writers to a movie. If the writer (associated
with the movie) is actually part of the writer crew then
return \[nconst, rating, name\].
Mapper 2
========

In-mapper combiner for reducing network traffic.

Every mapper has a list of 10 elements which contain the
most popular writers the mapper instance encounters.

For every line of the 10 most popular writers return
\[nconst, rating, name\].


Reducer 2
=========

*Important:* only one instance of the second reducer is
spawned.

Return the 10 most destinct popular writers.


