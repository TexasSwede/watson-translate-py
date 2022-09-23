import unittest
from translate import englishToFrench, frenchToEnglish

class Test_En_Fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # "Hello" should translate to "Bonjour"
        self.assertEqual(englishToFrench(), None)  # Test when no text is given
        self.assertNotEqual(englishToFrench(""), "")  # Test when a blank string is given
        

class Test_Fr_En(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # "Bonjour" should translate to "Hello"
        self.assertEqual(frenchToEnglish(), None)  # Test when no text is given
        self.assertNotEqual(frenchToEnglish(""), "")  # Test when a blank string is given
        
unittest.main()