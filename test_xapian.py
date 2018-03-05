# -*- coding: UTF-8 -*-
#
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

# Import from the Standard Library
from optparse import OptionParser
from sys import exit

# Import xapian
import traceback
import xapian



class XapianTest(object):

    def test(self, backend):
        if backend == 'glass':
            backend = xapian.DB_BACKEND_GLASS
        elif backend == 'chert':
            backend = xapian.DB_BACKEND_CHERT
        else:
            raise ValueError
        catalog = xapian.WritableDatabase('catalog', backend)
        catalog.begin_transaction(True)
        for i in range(0, 5000):
            #print('Doc {0}'.format(i))
            doc = xapian.Document()
            for j in range(0, 50):
                doc.add_value(j, 'Value {0}'.format(j))
            catalog.add_document(doc)
            catalog.commit_transaction()
            if i%50==0:
                for documentID in range(1, catalog.get_doccount() + 1):
                    document = catalog.get_document(documentID)
                    value1 = document.get_value(0)
                    value2 = document.get_value(1)
                    #print 'Value doc {0} - {1}'.format(documentID, value1)
                    #print 'Value doc {0} - {1}'.format(documentID, value2)
            catalog.commit()
            catalog.begin_transaction(True)




if __name__ == '__main__':
    # The command line parser
    usage = '%prog [OPTIONS] backend'
    version = '1.0'
    description = 'Test xapian'
    parser = OptionParser(usage, version=version, description=description)
    # Parse arguments
    options, args = parser.parse_args()
    n_args = len(args)
    if n_args != 1:
        parser.error('Wrong number of arguments.')
    else:
        backend = args[0]
        t = XapianTest()
        try:
            t.test(backend)
        except:
            print traceback.format_exc()
            exit(1)
    exit(0)
