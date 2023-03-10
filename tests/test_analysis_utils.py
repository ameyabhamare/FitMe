"""
Unit tests for utils/analysis module
"""
import sys
import os
import unittest
import pandas as pd


sys.path.insert(
    0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import utils

class TestAnalysisUtils(unittest.TestCase):
    """
    Test suite for analysis utils
    """
    def test_filter_df_user_id_valid_id(self):
        """
        Filters by user id
        """
        # Arrange
        df = pd.DataFrame(
            {'Id': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
        user_id = 2

        # Act
        filtered_df = utils.analysis_utils.filter_df_user_id(df, user_id)

        # Assert
        self.assertEqual(len(filtered_df), 1)
        self.assertEqual(filtered_df.iloc[0]['Name'], 'Bob')

    def test_filter_df_user_id_invalid_id(self):
        """
        Throws upon invalid id
        """
        # Arrange
        df = pd.DataFrame(
            {'Id': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
        user_id = 4

        # Act/Assert
        with self.assertRaises(TypeError):
            utils.analysis_utils.filter_df_user_id(df, user_id)


if __name__ == "__main__":
    unittest.main()
