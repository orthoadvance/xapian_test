# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from subprocess import Popen, PIPE
from pprint import pprint
import shutil, shlex


NB_TESTS = 5
tests = {'glass': {'success': 0, 'errors': 0},
         'chert': {'success': 0, 'errors': 0}}

for i in range(0, NB_TESTS):
    for backend in tests.keys():
        # Remove db if exist
        try:
            shutil.rmtree('catalog')
        except:
            pass
        # Run tests
        print('Test {0}/{1} {2}'.format(i+1, NB_TESTS, backend))
        cmd = 'python ./test_xapian.py {0}'.format(backend)
        cmd = shlex.split(cmd)
        popen = Popen(cmd, cwd='.')
        stdoutdata, stderrdata = popen.communicate()
        if popen.returncode == 1:
            tests[backend]['errors'] += 1
        else:
            tests[backend]['success'] += 1
# Print tests resuls
print '===='*10
print '===='*10
pprint(tests)
print '===='*10
print '===='*10
