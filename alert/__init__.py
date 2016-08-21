# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import subprocess

from docopt import docopt

__version__ = '0.1'


def main():
    """Alert

    Usage:
      alert <text>...
      alert <text>... [--title=<title>]
      alert (-h | --help)
      alert --version

    Options:
      -h --help     Show this screen.
      --version     Show version.
    """
    arguments = docopt(main.__doc__, version='OSX Alert 0.1')

    text = ' '.join(arguments.get('<text>'))
    title = arguments.get('--title', 'Alert')

    subprocess.call(["osascript", "-e", ('display notification "%s" with title "%s"' % (text, title))])


if __name__ == '__main__':
    main()
