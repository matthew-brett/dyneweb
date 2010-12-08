""" sphinx extension to implement bibtex blocks

Specifically it implements a new directive

.. bibrefs:: myrefs.bib
    :style: natbib.bst

    [ref1]
    [ref2]
    [ref3]

which results in the generation of 3 reference targets with the references
extracted from myrefs.bib and formatted according `natbib` style.

:copyright: Copyright 2010 by Matthew Brett
:license: BSD
"""
import os
from os import path
import codecs

from docutils import nodes, statemachine
from docutils.parsers.rst import directives

from sphinx.util.compat import Directive

# Copied from hg sphinx environment.py
def relfn2path(self, filename, docname=None):
    """Return paths to a file referenced from a document, relative to
    documentation root and absolute.

    Absolute filenames are relative to the source dir, while relative
    filenames are relative to the dir of the containing document.
    """
    if filename.startswith('/') or filename.startswith(os.sep):
        rel_fn = filename[1:]
    else:
        docdir = path.dirname(self.doc2path(docname or self.docname,
                                            base=None))
        rel_fn = path.join(docdir, filename)
    try:
        return rel_fn, path.join(self.srcdir, rel_fn)
    except UnicodeDecodeError:
        # the source directory is a bytestring with non-ASCII characters;
        # let's try to encode the rel_fn in the file system encoding
        enc_rel_fn = rel_fn.encode(sys.getfilesystemencoding())
        return rel_fn, path.join(self.srcdir, enc_rel_fn)


def refs_to_cites(refs, bib_text, options):
    cite_u_like = ['.. [%s] some text' % ref for ref in refs]
    return cite_u_like


class BibrefsDirective(Directive):

    has_content = True
    # Take arguments as one long string, we will parse into comma-separated
    # filenames later
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'style': directives.unchanged,
    }

    def arg_to_filenames(self, arg):
        """ Parse input argument line to contents

        Filenames are separated by commas
        """
        return [name.strip() for name in arg.split(',')]

    def run(self):
        document = self.state.document
        settings = document.settings
        env = settings.env
        fnames = self.arg_to_filenames(self.arguments[0])
        read_bibs = []
        for fname in fnames:
            rel_filename, filename = relfn2path(env, fname)
            env.note_dependency(rel_filename)
            try:
                fp = codecs.open(filename, 'r', 'utf-8')
                try:
                    bibcontents = fp.read()
                finally:
                    fp.close()
            except (IOError, OSError):
                return [document.reporter.warning(
                    'External bibtex file %r not found or reading '
                    'it failed' % filename, line=self.lineno)]
            read_bibs += bibcontents
        # Refs are just not-blank lines
        refs = []
        for line in self.content:
            ref = line.strip()
            if ref != '':
                refs.append(ref)
        citation_text = refs_to_cites(refs, read_bibs, self.options)
        tab_width = self.options.get('tab-width', settings.tab_width)
        self.state_machine.insert_input(citation_text, 'bibrefs-insertion')
        return []


def setup(app):
    app.add_directive('bibrefs', BibrefsDirective)

