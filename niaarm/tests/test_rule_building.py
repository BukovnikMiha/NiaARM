from unittest import TestCase
from niaarm.association_rule import AssociationRule
from niaarm.dataset import Dataset


class TestBuildRuleA(TestCase):
    # let's borrow test case from Wikipedia:
    # https://en.wikipedia.org/wiki/Lift_(data_mining)
    def setUp(self):
        data = Dataset("datasets/wiki_test_case.csv")
        self.features = data.get_features()
        self.oper = AssociationRule(self.features)

    def test_get_permutation(self):
        """Test map permutation method;
        permutation for ordering elements of association rule is located on the end
        of the vector"""

        permutation = self.oper.map_permutation(
            [0.98328107, 0.93655004, 0.6860223, 0.78527931, 0.96291945, 0.18117294, 0.50567635])

        self.assertEqual(permutation, [0.18117294, 0.50567635])

    def test_if_feasible_rule(self):
        """Test if rule is feasible"""
        antecedent_a = ["NO"]
        antecedent_b = ["A"]
        antecedent_c = ["1"]
        consequence_a = ["A"]
        consequence_b = ["0"]
        consequence_c = ["NO"]

        self.assertEqual(
            self.oper.is_rule_feasible(
                antecedent_a,
                consequence_a),
            False)
        self.assertEqual(
            self.oper.is_rule_feasible(
                antecedent_b,
                consequence_b),
            True)
        self.assertEqual(
            self.oper.is_rule_feasible(
                antecedent_c,
                consequence_a),
            True)
        self.assertEqual(
            self.oper.is_rule_feasible(
                antecedent_c,
                consequence_b),
            True)
        self.assertEqual(
            self.oper.is_rule_feasible(
                antecedent_a,
                consequence_c),
            False)

    def test_threshold_move(self):
        move = self.oper.calculate_threshold_move(0)
        move2 = self.oper.calculate_threshold_move(1)

        self.assertEqual(move, 1)
        self.assertEqual(move2, 2)

    def test_vector_position(self):
        """Important test for checking the position of feature in vector

           Categorical features consists of two vector elements, while
           each numerical feature consists of three vector elements.
        """

        permutation = self.oper.map_permutation(
            [0.98328107, 0.93655004, 0.6860223, 0.78527931, 0.96291945, 0.18117294, 0.50567635])

        order = self.oper.get_permutation(permutation)

        position1 = self.oper.get_vector_position_of_feature(0)
        position2 = self.oper.get_vector_position_of_feature(1)

        self.assertEqual(position1, 0)
        self.assertEqual(position2, 2)

    def test_build_rule(self):
        """Test procedure for building rules"""
        rule1 = self.oper.build_rule([0.45328107,
                                      0.13655004,
                                      0.6860223,
                                      0.78527931,
                                      0.96291945,
                                      0.18117294,
                                      0.50567635])
        rule2 = self.oper.build_rule([0.95328107,
                                      0.13655004,
                                      0.6860223,
                                      0.78527931,
                                      0.96291945,
                                      0.18117294,
                                      0.50567635])
        rule3 = self.oper.build_rule([0.95328107,
                                      0.98655004,
                                      0.6860223,
                                      0.78527931,
                                      0.96291945,
                                      0.18117294,
                                      0.50567635])
        rule4 = self.oper.build_rule([0.45328107,
                                      0.20655004,
                                      0.6860223,
                                      0.78527931,
                                      0.10291945,
                                      0.18117294,
                                      0.50567635])
        rule5 = self.oper.build_rule([0.45328107,
                                      0.20655004,
                                      0.2060223,
                                      0.79527931,
                                      0.10291945,
                                      0.18117294,
                                      0.50567635])
        rule6 = self.oper.build_rule([0.45328107,
                                      0.20655004,
                                      0.2060223,
                                      0.19727931,
                                      0.10291945,
                                      0.18117294,
                                      0.50567635])
        rule7 = self.oper.build_rule([0.95328107,
                                      0.20655004,
                                      0.2060223,
                                      0.19727931,
                                      0.10291945,
                                      0.18117294,
                                      0.50567635])

        self.assertEqual(rule1, [["A"], "NO"])
        self.assertEqual(rule2, [["B"], "NO"])
        self.assertEqual(rule3, ["NO", "NO"])
        self.assertEqual(rule4, [["A"], [1, 1]])
        self.assertEqual(rule5, [["A"], [0, 1]])
        self.assertEqual(rule6, [["A"], [0, 0]])
        self.assertEqual(rule7, [["B"], [0, 0]])


class TestBuildRuleB(TestCase):
    # Abalone test case
    def setUp(self):
        data = Dataset("datasets/Abalone.csv")
        self.features = data.get_features()
        self.oper = AssociationRule(self.features)

    def test_get_permutation(self):
        """Test map permutation method;
        permutation for ordering elements of association rule is located on the end
        of the vector"""
        vector1 = [
            0.55841534,
            0.95056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            0.73569511,
            1.0,
            0.15337635,
            0.11438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.82623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]

        permutation = self.oper.map_permutation(vector1)

        self.assertEqual(permutation,
                         [0.82623934,
                          0.0,
                          0.57660376,
                          0.0694041,
                          0.35173438,
                          0.09158622,
                          0.74415574,
                          0.56159659,
                          0.49068101])

    def test_threshold_move(self):
        move = self.oper.calculate_threshold_move(0)
        move2 = self.oper.calculate_threshold_move(1)
        move3 = self.oper.calculate_threshold_move(2)
        move4 = self.oper.calculate_threshold_move(3)
        move5 = self.oper.calculate_threshold_move(4)

        self.assertEqual(move, 1)
        self.assertEqual(move2, 2)
        self.assertEqual(move3, 2)
        self.assertEqual(move4, 2)
        self.assertEqual(move5, 2)

    def test_vector_position(self):
        vector1 = [
            0.55841534,
            0.95056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            0.73569511,
            1.0,
            0.15337635,
            0.11438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.82623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]

        permutation = self.oper.map_permutation(vector1)

        order = self.oper.get_permutation(permutation)

        self.assertEqual(order, [1, 3, 5, 4, 8, 7, 2, 6, 0])

        position1 = self.oper.get_vector_position_of_feature(0)
        position2 = self.oper.get_vector_position_of_feature(1)
        position3 = self.oper.get_vector_position_of_feature(2)

        self.assertEqual(position1, 0)
        self.assertEqual(position2, 2)
        self.assertEqual(position3, 5)

    def test_build_rule(self):
        """Test procedure for building rules"""

        vector1 = [
            0.55841534,
            0.95056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            0.73569511,
            1.0,
            0.15337635,
            0.11438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.82623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]
        rule1 = self.oper.build_rule(vector1)

        rule1_a = [[0.2620357326, 0.4989950842], 'NO', 'NO', 'NO', 'NO', 'NO', [0.34108412769999996, 0.56784007355], [0.13678483190000001, 0.44964727704], 'NO']

        self.assertEqual(rule1, rule1_a)

        vector2 = [
            0.75841534,
            0.15056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            0.73569511,
            1.0,
            0.15337635,
            0.91438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.82623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]

        permutation = self.oper.map_permutation(vector2)

        order2 = self.oper.get_permutation(permutation)

        rule2 = self.oper.build_rule(vector2)

        rule2_a = [[0.2620357326, 0.4989950842], 'NO', 'NO', 'NO', 'NO', 'NO', [0.34108412769999996, 0.56784007355], [0.13678483190000001, 0.44964727704], ['M']]

        self.assertEqual(rule2, rule2_a)
        self.assertEqual(order2, [1, 3, 5, 4, 8, 7, 2, 6, 0])

        vector3 = [
            0.35841534,
            0.15056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            0.73569511,
            1.0,
            0.15337635,
            0.91438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.72623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]

        permutation = self.oper.map_permutation(vector3)

        order3 = self.oper.get_permutation(permutation)

        rule3 = self.oper.build_rule(vector3)

        rule3_a = [[0.2620357326, 0.4989950842], 'NO', 'NO', 'NO', 'NO', 'NO', [0.34108412769999996, 0.56784007355], ['I'], [0.13678483190000001, 0.44964727704]]

        self.assertEqual(rule3, rule3_a)
        self.assertEqual(order3, [1, 3, 5, 4, 8, 7, 2, 0, 6])

        vector4 = [
            0.35841534,
            0.15056955,
            0.57296633,
            0.25275099,
            0.1311689,
            0.48081366,
            0.86191609,
            0.0,
            0.4988256,
            1.0,
            0.23,
            0.15337635,
            0.91438008,
            0.24168367,
            0.1185402,
            0.81325209,
            0.67415024,
            0.59137232,
            0.1794402,
            0.48980977,
            0.13287764,
            0.63728572,
            0.3163273,
            0.37061311,
            0.52579599,
            0.7206465,
            0.72623934,
            0.0,
            0.57660376,
            0.0694041,
            0.35173438,
            0.09158622,
            0.74415574,
            0.56159659,
            0.49068101]

        rule4 = self.oper.build_rule(vector4)

        rule4_a = [[0.2620357326, 0.4989950842], [0.5636729279999999, 1.13], 'NO', 'NO', 'NO', 'NO', [0.34108412769999996, 0.56784007355], ['I'], [0.13678483190000001, 0.44964727704]]

        self.assertEqual(rule4, rule4_a)
