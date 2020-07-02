# CSE 101 - IP HW2
# K-Map Minimization 
# Name: DAKSH THAPAR
# Roll Number: 2018137
# Section:A
# Group:1
# Date:15/10/2018

import unittest
from del2 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(2,4,5,6,10) d(12,13,14,15)'),'xy\'+yz\'')
		self.assertEqual(minFunc(3,'(0,1,2,5,6,7) d -'),'w\'x\'+wy+xy\'') 
		self.assertEqual(minFunc(4,'() d -'),'0')
		self.assertEqual(minFunc(3,'(0,1,2,3,4,5,6,7) d -'),'1')
		self.assertEqual(minFunc(4,'(4,8,10,11,12,15) d(9,14)'),'wx\'+wy+xy\'z\'')
		self.assertEqual(minFunc(3,'(0,2,5) d(7)'),'w\'y\'+wy')
		self.assertEqual(minFunc(4,'(0) d -'),'w\'x\'y\'z\'')
		self.assertEqual(minFunc(2,'(0,3) d -'),'w\'x\'+wx')
		self.assertEqual(minFunc(2,'(0) d(3)'),'w\'x\'')		
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5,6,7) d -'),'w\'')




if __name__=='__main__':
	unittest.main()
