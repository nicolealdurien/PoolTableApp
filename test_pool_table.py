#Unit Tests for Pool Table App

import unittest
from pool_table_class import PoolTable
from pool_tables import *

class PooltableTests(unittest.TestCase):
    def setUp(self):
        self.pool_table = PoolTable(1, False)

    #def test_assign_table(self):
        
     #   self.assertEqual(self.pool_table.assign_table(), "Occupied")

    def test_occupancy_check(self):
        self.assertEqual(self.pool_table.occupancy_check(), "Vacant")

unittest.main()