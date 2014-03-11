.. _cv:

################
Curriculum Vitae
################

****************
Personal Details
****************

**Date of birth**
    November 20, 1964

**Nationality**
    British

**Email**
    matthew.brett@gmail.com

**Work address**
     | Helen Wills neuroscience institute
     | 210 Barker Hall
     | University of California
     | Berkeley CA 94720

*********************
Research and teaching
*********************

There are five threads to my work:

#. Training in neurology to registrar level
#. Research on brain basis of movement planning and performance
#. Research, teaching and consulting on brain imaging methods
#. Development of open-source software for imaging methods
#. Teaching scientific computing

Training in neurology
=====================

I trained in neurology at: Cambridge; St Bartholomew's hospital; The National
Hospital for Neurology; Oxford and the Hammersmith Hospital. I had a National
Training Number to continue training to consultant level but gave this up to
continue research.

Research on movement
====================

My first research post was on PET imaging of apraxia and movement selection
supervised by David Brooks and John Stein. I continued research on movement in
the MRC Cognition and Brain Science Unit (CBSU) with my two students Katja
Osswald and Jessica Grahn.  Jessica's work was particularly successful with a
well-cited and clean paper in the Journal of Cognitive Neuroscience showing that
beat perception causes striking bilateral activation of the basal ganglia.

Research and teaching on imaging methods
========================================

As part of my PET research I taught myself programming in MATLAB, the SPM
software package and the principles of imaging methods including statistics.  I
began to teach, eventually resulting in a series of popular tutorials on
imaging statistics and multiple comparison correction (see *online tutorials* in
publication list). The tutorial on multiple comparisons became a book chapter in
a standard reference on functional imaging analysis (Brett et al 2007).  I
developed an interest in methodology research, showing, for example, that
activation PET imaging suffers from some specific movement artifacts that can
easily be mistaken for frontal lobe activation (Brett et al 1999).

My experience of programming allowed me to develop new methods.  I co-wrote a
paper with one of the main SPM authors on methods of warping damaged brains to
standard brain templates (Brett et al 2001) (418 citations).  In 2001 I gave my
first full neuroimaging course, giving nine hours of lectures and 5 hours of
practical teaching. With Ingrid Johnsrude and Adrian Owen, I wrote a review on
ways of identifying location of brain activation, cited 770 times. Later I
published a paper with Tom Nichols, Jesper Anderson and others on an incorrect
statistical procedure for so-called "conjunction analysis" in SPM (Nichols et al
2005) (859 citations). I contributed to the standard reference paper on
reporting guidelines for functional MRI (Poldrack et al 2008) and co-authored a
paper with Rebecca Saxe and Nancy Kanwisher on the region of interest technique
for analysing FMRI data (Saxe et al 2006).

With Eleftherios Garyfallidis and Ian Nimmo-Smith, I became increasingly
interested in diffusion imaging (Garyfallidis et al 2010, 2012). Our
collaboration became the dipy project, which has since developed into a
successful international collaboration of diffusion researchers (Garyfallidis
2014).

With Jean-Baptiste Poline, I wrote a review and tutorial paper on the general
linear model in functional MRI for a recent special issue of NeuroImage (Poline
and Brett 2012).

Development of open-source software for imaging methods
=======================================================

When I was working at the MRC CBSU, I went to a job talk by Russell Epstein in
which he described his work with Nancy Kanwisher using functional MRI to study
the parahippocampal place area. I was struck by the simplicity and elegance of
their analysis.  At the time we could not use SPM software to do these analyses
and this barrier was enough to make it a lot less likely that other researchers
would use these methods.  With colleagues in France, I wrote the MarsBaR region
of interest toolbox that allows Kanwisher-type region-of-interest analyses using
SPM.  Since then I have updated and released MarsBaR at regular intervals. The
abstract for MarsBaR has been cited nearly 1500 times.

I worked on wavelet analysis methods with Federico Turkheimer and John Aston.
This work introduced me to David Donoho's writing and the concept of
reproducible science [#donoho]_.  We used our own Phiwave toolbox for an
analysis for a competition at the Human Brain Mapping Conference (Aston et al
2006).  I published all the scripts for the analysis to make it reproducible;
see http://phiwave.sourceforge.net/fiac/index.html.

While on a two-year visit to Berkeley from 2003 I started working with
programmers and scientists interested in open-source software development.  With
Jarrod Millman, I initiated a proposal to develop an international collaboration
with statisticians, signal processing and image processing experts to write a
new entirely open software library for functional imaging analysis. We chose the
Python programming language for this effort because of its famously clean
syntax, high quality scientific libraries, and fully open-source distribution.
The NIH eventually funded this proposal as a 3-year R01 grant from 2007-2010.
The program became the Nipy project |--| http://nipy.org.

The collaborations from this work gave me much greater experience of the working
practice of successful scientific programmers, and allowed me to see and use the
many tools that are developing for improving scientific code and sharing
analyses. For example, all our `nipy.org`-based projects use standard
open-source best practice for software development, including distributed
version control based at http://github.com/nipy, full web-based code review,
and automated code testing on our own servers and publicly available testing
servers for open-source projects.

The Nipy community now consists of six projects. I am the lead developer of the
main *nipy* project and the *nibabel* image reading library, and a core
developer of *dipy* (see above).

In part because of this work, I have become increasingly involved in projects to
teach computing methods to students and researchers. I have taught and assisted
at *Software Carpentry* workshops [#swc]_ teaching basic techniques for using
scientific code.

I have been lucky to have been very close to the development of the
IPython notebook, an interactive web-based application that allows sharing of
code and data for describing analyses and teaching. This technology has allowed
me to go back to previous tutorials in which I had tried to mix code and
explanation, and rewrite them as I had imagined them, with full interactivity,
simple code and high-quality mathematical markup (see online *tutorial* section
of publications).  The IPython notebook has been picked up very rapidly and has
already been used for reproducible publications in statistics, microbial
ecology, genomics, cosmology, astronomy, oceanography, computational biology,
and computational neuroscience [#ipython-refs]_.

With Jean-Baptiste Poline and Paul Ivanov, we have used this technology to give
a course on practical neuroimaging that combines teaching of the concepts with
code implementing and illustrating these concepts.

******************
Research Positions
******************

**August 2008 - present**
    *Associate researcher at the Brain Imaging Center, University of California,
    Berkeley*. Consulting on design and analysis of functional brain imaging
    data; post-graduate teaching on functional imaging ; development of `nipy`
    open source software projects; contributing to development of new algorithms
    for analysis of diffusion imaging; giving a 28-week course teaching
    neuroimaging analysis through examples of running code.
**October 2005 – July 2008**
    *Senior investigator scientist at the MRC Cognition & Brain Sciences Unit,
    Cambridge*. Working with Ian Nimmo-Smith and other members of the methods
    group. Consulting on design and analysis of functional brain imaging data
    and diffusion imaging data, new research on brain imaging methods, teaching
    of functional imaging methods.
**October 2003 – September 2005**
    *Associate specialist in psychology at the University of California,
    Berkeley*.  Working with Rich Ivry. Research into mechanisms of movement
    selection using functional brain imaging.
**March 1999 – September 2003**
    *Research associate at the MRC Cognition & Brain Sciences Unit, Cambridge*.
    Working with John Duncan on mechanisms of movement selection using
    functional brain imaging (positron emission tomography, functional MRI
    scanning).  Also working on algorithms for matching structural brain images
    from damaged brains to normal brain templates.
**February 1996 – February 1999**
    *Research registrar in neurology at the MRC Cyclotron Unit, Hammersmith
    hospital and Oxford laboratory of physiology*. Jointly supervised by David
    Brooks (London) and John Stein (Oxford).  Using regional blood flow images
    from positron emission tomography to study the role of motor areas in
    response design and selection.

*****************
Medical Positions
*****************

**June 1995 – January 1996**
    Registrar in neurology at the Radcliffe Infirmary, Oxford
**August 1994 – April 1995**
    Senior house officer in neurology at The National Hospital for Neurology,
    Queen Square, London
**August 1992 – July 1994**
    Senior house officer medical rotation at St Bartholomew’s Hospital, London
**February 1992 – July 1992**
    Senior house officer in neurosciences at Addenbrooke's Hospital, Cambridge
**August 1991 – January 1992**
    Research worker at the Institute of Psychiatry, London
**August 1990 – July 1991**
    House officer at the Princess Alexandra Hospital, Harlow and Royal London
    Hospital.

****************************
Education and Qualifications
****************************

**1994**
    *Membership of the Royal College of Physicians (UK)*. Physicians that want
    to specialize in branches of general medicine such as neurology need to pass
    this examination of academic and clinical competence in general medicine.
**1987 – 1990**
    *Bachelor of Medicine and Surgery (MB BChir)*
**1984 – 1987**
    *BA 2.i; Experimental Psychology, Cambridge University (UK)*

******
Awards
******

**1996**
    British Brain and Spine Foundation 3 year research training fellowship
**1984**
    Open Entrance Scholarship to Cambridge University

Journals
========

Reviewer for NeuroImage, Human Brain Mapping, Journal of Cognitive Neuroscience,
Neuroscience Letters, Clinical Neurophysiology, Journal of Neuroimaging, the
Journal of Clinical and Experimental Neuropsychology, Frontiers in
Neuroinformatics, Computing in Science and Engineering, Frontiers in Brain
Imaging Methods, Computers in Science and Engineering, Public Library of Science
One. Member of the editorial board of *Frontiers in Brain Imaging Methods*.

Graduate supervision
====================

**2000 – 2004** *Katja Osswald*
    The role of SMA and basal ganglia in motor learning, mechanisms of apraxia
    and methods of functional MRI analysis (submitted May 2004).  Katja is now a
    teaching fellow at the department of psychology in York and a practicing
    clinical psychologist.

**2001 – 2004** *Jessica Grahn*
    The functional anatomy of musical beat perception. Jessica is currently an
    assistant professor in the department of psychology in the university of
    Western Ontario.

I was a member of the graduate committee for the MRC cognition and brain
sciences unit 2007-2008

Undergraduate supervision
=========================

* Lent 2007 through Easter 2008 : Supervised Cambridge medical students on
  neuroscience for Jesus college.
* 1994-1995 : Supervised Oxford medical students on neuroanatomy

Post-doctoral scholars supervised
=================================

**2001 – 2002** *Alexandre Andrade*
    Working on surface-based functional MRI statistics, coherence analysis.
    Alexandre is now a professor Institute of Biophysics and Biomedical
    Engineering, Lisbon, Portugal.

**2002 – 2006** *Ferath Kherif*
    Working on multivariate statistics for clustering and diagnostics of
    functional imaging data. Ferath is currently a principal investigator at the
    Laboratory of Research in Neuroimaging, Lausanne, Switzerland.

Invited talks
=============

Invited talks on neuroimaging methods in Cambridge, London, Oxford, York,
Sheffield, Paris, Lyon, Marseille, Tokyo, Buenos Aires, Berkeley, Stanford,
Havana; including:

* 2013: invited speaker for International Neuroinformatics Coordinating Facility
  workshop in Havana; "The need and the methods for reproducible science".
* 2009: presentation to Neuroinformatics session of Human Brain Mapping
  conference; "Neuroimaging in Python".
* 2009: invited speaker for FMRIB Software Library course at Human Brain
  Mapping conference, San Francisco; "Experimental design".
* 2007: invited speaker for 5th Latin-American congress of clinical
  neurophysiology, Havana; "Software and change in science".
* 2004, 2006, 2007: Invited speaker for Human Brain Mapping conference course on
  functional MRI
* 2000 – 2003: Invited speaker at annual functional imaging courses held in
  Paris.

Courses taught
==============

* February |--| October 2013, Berkeley; with Jean-Baptiste Poline and Paul
  Ivanov. A course for two hours per week on "practical neuroimaging" - teaching
  the ideas of analysis with code, and the practice of scientific coding.
* December 2013, Stanford; teacher at the "fMRI data analysis workshop".
* 2008 – present, Berkeley: *Regular post-graduate teaching for "Functional MRI
  Methodology Seminar" series and "Neuroimaging seminar series"*. My topics
  include: motion correction; cross-modality registration; registration between
  subjects; modeling of evoked haemodynamic signal; analysis of variance and
  multiple regression using the General Linear Model; statistical inference
  using fixed and random effects; multiple comparison correction using Random
  field theory, False Discovery Rate and permutation testing; diffusion imaging
  principles and analysis.
* 1999 - 2003; 2005 - 2008, Cambridge; *Regular seminars on image processing and
  statistics in functional MRI* covering motion correction; within and cross
  modality registration; cross subject brain registration; statistical inference
  and multiple comparison correction using Random field theory, False Discovery
  Rate and permutation testing.
* 2005, Oslo: *4 day course on functional MRI analysis with SPM* (with
  Ansgar Furst) covering motion correction; cross-modality registration;
  registration between subjects; modeling of evoked haemodynamic signal;
  analysis of variance and multiple regression using the General Linear Model;
  statistical inference using fixed and random effects; multiple comparison
  correction using Random field theory, False Discovery Rate and permutation
  testing.
* 2005, Yale: *Faculty for course on anatomical and functional MRI analysis
  using SPM*
* 2001, Melbourne, Australia: gave 9 hours of lectures and 5 hours of practical
  sessions on functional MRI analysis using SPM covering similar topics to Oslo
  course above.

.. rubric:: Footnotes

.. [#donoho] Buckheit, Jonathan B., and David L. Donoho. *Wavelab and
   reproducible research*. Springer New York, 1995.

.. [#ipython-refs]
   https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks#wiki--reproducible-academic-publications
.. [#swc] Software carpentry (http://software-carpentry.org) is an international
   project to teach scientists to use computing tools; founded in 1998, it is
   now part of the Mozilla Science Lab.

.. [#dpc-nibabel] http://qa.debian.org/popcon.php?package=nibabel
.. [#dpc-dipy] http://qa.debian.org/popcon.php?package=dipy

.. |--| unicode:: U+2013   .. en dash
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:
