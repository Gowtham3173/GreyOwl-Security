import unittest
from src.model import ThreatDetectionModel

class TestThreatDetectionModel(unittest.TestCase):
    def setUp(self):
        self.model = ThreatDetectionModel()

    def test_train(self):
        # Add code here to load and split your data for training
        self.model.train(X_train, y_train)
        self.assertTrue(self.model.model is not None)

if __name__ == "__main__":
    unittest.main()
