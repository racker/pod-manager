# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import doctest

from distutils.core import setup
from distutils.core import Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from subprocess import call
from os.path import splitext, basename, join as pjoin

def read_version_string():
    version = None
    sys.path.insert(0, pjoin(os.getcwd()))
    from libcloud import __version__
    version = __version__
    sys.path.pop(0)
    return version


class Pep8Command(Command):
    description = "run pep8 script"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pep8
            pep8
        except ImportError:
            print ('Missing "pep8" library. You can install it using pip: '
                  'pip install pep8')
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(('pep8 %s/pod_manager/' %
                (cwd)).split(' '))
        sys.exit(retcode)


setup(
    name='pod-manager',
    version=read_version_string(),
    description='todo',
    author_email='dodo',
    requires=[],
    packages=[
        'pod_manager',
    ],
    package_dir={
        'pod_manager': 'pod_manager',
    },
    license='Apache License (2.0)',
    url='https://github.com/racker/pod-manager/',
    cmdclass={
        'pep8': Pep8Command,
    },
    classifiers=[
        'Development Status :: 4 - Beta'
    ])
