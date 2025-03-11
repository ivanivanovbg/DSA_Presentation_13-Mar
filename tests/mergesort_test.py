from unittest import TestCase
from mergesort import merge_sort


class mergesort_Should(TestCase):

    def test_mergesort_sorts_correctly_when_array_has_elements(self):
        #Arrange
        unsorted_list = [10,1,5,4]
        #Act
        sorted_list = merge_sort(unsorted_list)
        #Assert
        self.assertEqual(sorted_list,[1,4,5,10])

    def test_mergesort_sorts_correctly_when_array_has_mixed_positive_and_negative_elements(self):
        #Arrange
        unsorted_list = [10,1,-5,4]
        #Act
        sorted_list = merge_sort(unsorted_list)
        #Assert
        self.assertEqual(sorted_list,[-5,1,4,10])

    def test_mergesort_returns_empty_list_when_original_list_is_empty(self):
        #Arrange
        unsorted_list = []
        #Act
        sorted_list = merge_sort(unsorted_list)
        #Assert
        self.assertEqual(sorted_list,[])

    def test_mergesort_works_with_strings(self):
        #Arrange
        unsorted_list = ["bee","apples","apple","ape"]
        #Act
        sorted_list = merge_sort(unsorted_list)
        #Assert
        self.assertEqual(sorted_list,["ape","apple","apples","bee"])

    def test_mergesort_raises_error_when_values_incompatible(self):
        #Arrange
        unsorted_list = ["bee","apples","apple",1,"ape"]
        #Act and Assert
        with self.assertRaises(TypeError):
            merge_sort(unsorted_list)