from __future__ import print_function
import sys

from setuptools import setup

setup(
    name="xpybutil",
    maintainer="Fenner Macrae",
    author_email="fmacrae.dev@gmail.com",
    version="0.0.6",
    license="WTFPL",
    description="An incomplete xcb-util port plus some extras",
    long_description="See README",
    url="http://github.com/BurntSushi/xpybutil",
    platforms='POSIX',
    packages=['xpybutil'],
    data_files=[('share/doc/xpybutil', ['README.md', 'COPYING'])]
)
