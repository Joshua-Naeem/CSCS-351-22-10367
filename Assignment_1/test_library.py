import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    

    def setUp(self):
        self.c = Library(['Harry Potter','The Last Airbender', 'Multiverse of Madness'])
        self.c.lendbook('Harry Potter')
        self.c.add_book('Garvin Adventures')
        self.c.new_book('James Harold')
        self.c.delete_book('Harry Potter')
    
        
    #test_case_1
    def test_availablebooks(self):
        print('test_availablebooks')
        self.assertEqual(self.c.get_available_books(), ['Harry Potter','The Last Airbender', 'Multiverse of Madness'])
    
    #test_case_2
    def test_lendbook(self):
        print('test_lendbook')
        self.assertEqual(self.c.lendbook('Harry Potter'), 'Harry Potter')

    #test_case_3
    def test_add_book(self):
        print('test_add_book')
        self.assertEqual(self.c.add_book('Garvin Adventures'), 'Garvin Adventures')
    
    #test_case_4
    def test_new_book(self):
        print('test_new_book')
        self.assertEqual(self.c.new_book('James Harold'), 'James Harold')
    
    #test_case_5
    def test_delete_book(self):
        print('test_delete_book')
        self.assertEqual(self.c.new_book('Harry Potter'), 'Harry Potter')
    
    
if __name__ == '__main__':
    unittest.main()  