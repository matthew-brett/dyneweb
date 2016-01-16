############################################
Research methods in the twenty-first century
############################################

We neuroscientists live in interesting times.

There have been much recent discussion of the possibility that science as
current practiced and published has a high rate of error.  A 2015 study
:cite:`open2015estimating` found that only 39% of a partially-random sample of
cognitive and social psychology articles could be replicated.  Articles that
were more complicated to replicate or that had more surprising results had
lower replication rates.  Ioannidis :cite:`ioannidis2005most` has argued that
the false positive rate will be higher in expensive, fashionable fields with
small sample sizes and complex analysis |--| features of neuroscience
techniques such as neuroimaging.

How did this high rate of false positives come about?  How can we make
published science more likely to be true?

It is clear that the system of academic rewards has played a role
(:cite:`nosek2012scientific,deci1999meta,kohn1993punished`), but fixing the
system of rewards needs political action and education.

I believe that another major factor in the increasing gap between the training
we give our students and the needs of disciplined scientific practice.

What is disciplined scientific practice?  It takes two forms.  The first could
called "best practices in scientific computing".  There is general agreement
about what this means, and it includes standard use of version control,
automated testing, and peer review of scientific code :cite:`wilson2014best`.
These are all techniques than can be shown to reduce error and improve
collaboration.  I know of no neuroscience or psychology course that teaches
these.

The second aspect of disciplined scientific practice is related; to have a
process that teaches steadfast skepticism of our own work and that of other
scientists.

There are many factors that make skepticism more difficult in modern science.
One is that there is a large gap between the statistics and methods that we
teach and the methods used in many recent papers.  Standard neuroscience and
psychology courses teach t-tests, correlation and ANOVA using the methods
pioneered by Fisher in the 1920s :cite:`fisher1925statistical`.  These
teaching methods work well if the student will only be using t-tests, ANOVA or
correlation, but give them little help in understanding such standard methods
as Principal Components Analysis, constrained regression and other techniques
grouped under the heading of "machine learning" :cite:`trevor2009elements`.
To give some index of the problem, a recent textbook called "All of
statistics: a concise course on statistical inference"
:cite:`wasserman2013all` does not have the terms "ANOVA" or "Analysis of
variance" in its index.

A second barrier to skepticism is that our methods courses have come to rely
heavily on off-the-shelf statistical packages such as SPSS and the R computing
language.  Outside a narrow range of analysis, the student is unlikely to know
what calculations these programs are using, making it easy for them to give
in to uncritical belief in their output |--| a phenomenon known as
`garbage-in, gospel-out
<https://en.wikipedia.org/wiki/Garbage_in%2C_garbage_out#Uses>`_.  By teaching
in this way we make it more likely that students will get used to the
dangerous habit of feeding complex data through canned analysis pipelines and
interpreting output they are in no position to assess.

The way to overcome both these barriers to skepticism is for us to teach our
students in a different way.  It is important for the students to understand
what calculations these packages are doing and why.  To quote `Richard Feynman
<https://www.quora.com/What-did-Richard-Feynman-mean-when-he-said-What-I-cannot-create-I-do-not-understand>`_:
"What I cannot create, I do not understand". Luckily we now have many good
tools to teach this kind of computational thinking. In particular, the
scientific computing community has begun to standarize to the Pytho
programming language 

.. rubric:: References

.. bibliography:: research/general.bib research/matthew_brett.bib
    :style: plain

.. include:: links.txt
