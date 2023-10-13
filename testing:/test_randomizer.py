import unittest
from src import randomizer

class TestRandomizer(unittest.TestCase):

    def setUp(self):
        # Sample data for the tests
        self.sample_data_list = ["item1", "item2", "item3", "item4"]
    
    def test_select_random_element(self):
        random_element = randomizer.select_random_element(self.sample_data_list)
        self.assertIn(random_element, self.sample_data_list)

    def test_random_element_uniqueness(self):
        # ensure randomness over multiple calls
        selections = [randomizer.select_random_element(self.sample_data_list) for _ in range(10)]
        self.assertTrue(len(set(selections)) > 1, "Multiple selections should not be the same item repeatedly.")

    def test_shuffle_data(self):
      
        shuffled_data = randomizer.shuffle_data(self.sample_data_list)
        self.assertCountEqual(shuffled_data, self.sample_data_list, "Shuffled data should contain the same items.")
        
        
        another_shuffled_data = randomizer.shuffle_data(self.sample_data_list)
        self.assertNotEqual(shuffled_data, another_shuffled_data, "Subsequent shuffles should typically differ.")



if __name__ == '__main__':
    unittest.main()
