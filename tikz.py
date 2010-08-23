# -*- coding: utf-8 -*-

# A picture drawing directive using TikZ

# Todo:
# - If something fails, e.g. a syntax error in the latex code then only there is
#   no feedback.

import tempfile
import posixpath
from os import path, getcwd, chdir, mkdir, system
from subprocess import Popen, PIPE
try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx.util import ensuredir, ENOENT, EPIPE
from sphinx.util.compat import Directive


class tikz(nodes.General, nodes.Element):
    pass

class TikzDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {'libs':directives.unchanged}

    def run(self):
        node = tikz()
        node['code'] = '\n'.join(self.content)
        node['arguments'] = self.arguments
        node['libs'] = self.options.get('libs', None)
        return [node]

DOC_HEAD = r'''
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{bm}
\usepackage{tikz}
%s
\pagestyle{empty}
'''

DOC_BODY = r'''
\begin{document}
\begin{tikzpicture}
%s
\end{tikzpicture}
\end{document}
'''

def html_visit_tikz(self,node):
    print "\n***********************************"
    print "You have entered the following argument"
    print "***********************************"
    for line in node['arguments']:
        print line
    print "***********************************"
    print "You have entered the following tikzlibraries"
    print "***********************************"
    print node['libs']
    print "\n***********************************"
    print "You have entered the following text"
    print "***********************************"
    print node['code']
    print "***********************************"
    hashkey = node['code'].encode('utf-8')
    fname = 'tikz-%s.png' % (sha(hashkey).hexdigest())
    if hasattr(self.builder, 'imgpath'):
        # 'HTML'
        relfn = posixpath.join(self.builder.imgpath, fname)
        outfn = path.join(self.builder.outdir, '_images', fname)
    else:
        # 'LaTeX'
        relfn = fname
        outfn = path.join(self.builder.outdir, fname)
        
    print relfn
    print outfn

    ensuredir(path.dirname(outfn))

    libs = ''
    if node['libs']:
        libs = '\usetikzlibrary{' + node['libs'] + '}'

    latex = DOC_HEAD % libs + DOC_BODY % node['code']
    if isinstance(latex, unicode):
        latex = latex.encode('utf-8')

    print latex
    if not hasattr(self.builder, '_tikz_tempdir'):
        tempdir = self.builder._tikz_tempdir = tempfile.mkdtemp()
    else:
        tempdir = self.builder._tikz_tempdir

    # tempdir = 'tmp'
    # mkdir(tempdir)

    tf = open(path.join(tempdir, 'tikz.tex'), 'w')
    tf.write(latex)
    tf.close()

    latex_args = 'latex --interaction=nonstopmode tikz.tex'

    curdir = getcwd()
    chdir(tempdir)

    system(latex_args)
    system('cp tikz.tex /tmp')

    dvips_args = 'dvips tikz.dvi'
    system(dvips_args)
    system('cp tikz.ps /tmp')

    pstoimg_args = 'pstoimg -type png -scale 1.64 -antialias -aaliastext -crop a'
    pstoimg_args += ' -out ' + outfn + ' tikz.ps'
    print pstoimg_args
    system(pstoimg_args)

    chdir(curdir)

    self.body.append(self.starttag(node, 'div', CLASS='math'))
    self.body.append('<p>')
    self.body.append('<img src="%s" alt="%s" /></p>\n</div>' %
                         (relfn, self.encode(node['code']).strip()))


def depart_tikz(self,node):
    pass

def setup(app):
    app.add_node(tikz,
                 html=(html_visit_tikz, depart_tikz))
    app.add_directive('tikz', TikzDirective)
