Task 1
======

Retrieve average, minimum and maximum duration for all
titles per *movie* genre.


Output
------

\[avg|max|min|genre\]


Additional information
----------------------

* title -> genre: 1 -> n (title should be considered for
                          all associated genres)

* avg: in minutes and rounded to two decimal places

* runtime = 0 should be considered in computation


Data sources
------------

* title.basics.tsv


Mapper
======

For each valid line return \[genre, runtime\].


Combiner
========

Accumulates over genre. Sums the runtime, counts the
amount of movies and sets min and max.

For each genre return \[genre, summed runtime,
amount of lines (movies), min, max\].


Reducer
=======

Accumulates over genre (see Combiner).


