.. _build-site:

How I built this site
=====================

The machinery for this site comes from Fernando Perez - see `Fernando's site`_
and particularly `Fernando's web machinery`_.  I've copied his instructions here
so I can edit them as I build my own site with the same tools.  Thanks to
Fernando for putting up the tools.

Tools needed
------------

Before getting started, make sure you have the following on your computer, else
nothing will really work:

* Make: standard on Linux, you may need to install XCode on OSX.
* Python_: Required for Sphinx and for my scripts to run.
* Sphinx_: The main documentation building tool.
* ImageMagick_: you only need this if you want to use my little thumbnail
  script (see below).
* Rsync: Standard on Linux and OSX, used to upload the site contents to a
  public location.
* Firebug_: pretty much needed to do *any* kind of debugging of web material.

Workflow
--------

These tools work with a very simple approach: the ``conf.py`` file configures
things for Sphinx, the ``themes/matthew`` directory contains the layout and CSS
necessary to render the site (this is configured in ``conf.py``), and the main
Makefile has targets to build the files, update the css for testing cosmetic
changes, and to upload the final content to a public site.  The initial steps
to get the system ready are:

#. Edit ``conf.py`` to suit your taste.

#. Please change the theme name and contents as requested above to your own.

#. Edit the ``Makefile`` to indicate where you will upload the final site (the
   ``WWW`` variable).  To make your life easier on uploads, I suggest you
   configure things for passwordless SSH key-based access, but that's up to
   you.

With these things ready, the normal workflow is:

1. Edit files for content.

2. To build the site, type:

::

   make

3. View the resulting site at ``_build/html/index.html`` in your browser.

4. If you need to make changes to the CSS files only, type:

::

  make css

for a quick update without needing a full rebuild.

5. Occasionally if things don't look right, do a full cleanup/rebuild via:

::

  make clean
  make

6. Once you are happy with the results locally, push to your public site with:

::

  make upload

Additional details and Background reading
-----------------------------------------

If you are interested in building a site with the same workflow, I recommend
that you first:

* Have a quick read of the official Sphinx_ documentation to get an idea of how
  things work.  Don't go into too much detail, but knowing where the main ideas
  are described in the docs will save you time later.

* Do pay attention to the reST notes, because that's the syntax you'll be using
  to actually write.  Note that on this site, I've left always visible the
  "Show Source" links on the right-hand navigation bar, which can be a useful
  way to learn how things are done.  If you see anything in a page you are
  curious about, just click that link.

* Run through the very nice Sampledoc_ mini-tutorial written by John Hunter
  (matplotlib_'s lead developer).  That tutorial will get you 90% of the way
  there, and in fact you may find it sufficient for your purposes.

I (Fernando) personally needed a little bit on top of sampledoc; in particular I wanted
finer control over the layout of the site and decided to build a full Sphinx
theme (albeit a minimally modified one), and I also wanted some tools to
statically upload files like PDFs, zip archives or any other content I might
have in subdirectories into the public site.  By default sphinx does not upload
non-reST files in any other directory than its ``_static`` one, and I wanted to
be able to populate arbitrarily nested subdirectories with material like
papers, talks or software packages, and have those files uploaded *in the same
location* to the public site.

To achieve that, there's a simple script called `copy_trees
<copy_trees.py>`_ that copies my input trees to the Sphinx output build
directory prior to synchronization to the public site.

I (Fernando) also have written a tiny thumbnailer script, `mkthumb <mkthumb>`_
that you may find useful to quickly create smaller images for inline display.
Note that this needs the ``convert`` utility from the ImageMagick_ suite.

.. include:: ../links.txt
