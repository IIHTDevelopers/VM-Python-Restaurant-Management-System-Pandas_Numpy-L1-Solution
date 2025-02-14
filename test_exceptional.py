import unittest
from restaurant_manager import RestaurantManager
from TestUtils import TestUtils

class ExceptionalTests(unittest.TestCase):
    def setUp(self):
        self.restaurant = RestaurantManager()
        self.test_utils = TestUtils()

    
    def test_empty_customer_name(self):
        """Test empty customer name raises ValueError"""
        try:
            self.restaurant.validate_customer("")
            self.test_utils.yakshaAssert("test_empty_customer_name", False, "exception")
            print("test_empty_customer_name = Failed")
        except ValueError:
            self.test_utils.yakshaAssert("test_empty_customer_name", True, "exception")
            print("test_empty_customer_name = Passed")
        except Exception:
            self.test_utils.yakshaAssert("test_empty_customer_name", False, "exception")
            print("test_empty_customer_name = Failed")

if __name__ == '__main__':
    unittest.main()
