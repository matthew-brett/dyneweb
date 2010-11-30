###############################
What I want from a bibliography
###############################

I have a bib file - ``matthew.bib``.

I want to make a page, that lists references there in a sensible way.

The page might be in the form of a template::

    Software
    ========

    [ref1]
    [ref2]

    Methodology
    ===========

    [ref3]
    [ref4]

I'd like then to run a build step, that would take ``matthew.bib``, extract the
references pointed to by e.g ``[ref1]`` (the bibtex key), and substitute a ReST
version of the reference, including markup for downloads.

The markup for an individual reference might end up with something like this:

Grahn, JA, Brett, M (2009) Impairment of beat-based rhythm discrimination in
Parkinson's Disease.  *Cortex 45, 54-61*. `[doi: the-doi/no] <my-doi.link>`_
:download:`[download] <bibs.rst>` :ref:`[bibtex] <grahn2009-bibtex>`

Obviously this needs both DOI and download fields in the bibtex database.

Here I make the reference necessary for the bibtex ref above to work:

.. _grahn2009-bibtex:

::

    @ARTICLE{Grahn2009,
    author = {Jessica A Grahn and Matthew Brett},
    title = {Impairment of beat-based rhythm discrimination in Parkinson's disease.},
    journal = {Cortex},
    year = {2009},
    volume = {45},
    pages = {54--61},
    number = {1},
    month = {Jan},
    doi = {10.1016/j.cortex.2008.01.005},
    url = {http://dx.doi.org/10.1016/j.cortex.2008.01.005}
    }


Lorem ipsum [Ref]_ dolor sit amet.

Some text

.. [Ref] Book or article reference, URL or whatever.

More text

.. Another ref [Ref2]_ points down

.. [Ref2] Another book or article reference

