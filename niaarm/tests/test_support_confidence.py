from unittest import TestCase
from niaarm.association_rule import AssociationRule
from niaarm.dataset import Dataset

class TestSupportConfidence(TestCase):
    # let's borrow test case from wikipedia: https://en.wikipedia.org/wiki/Lift_(data_mining)

    def setUp(self):
        data = Dataset("datasets/wiki_test_case.csv")
        self.features = data.get_features()
        self.transactions = data.transaction_data

    def test_a(self):
        # Rule: A => 0
        antecedent_a = [['A']]

        consequence_a = [[0, 0]]

        support_a = 0.42857142857142855

        confidence_a = 0.75

        vector =  [0.27989089, 0.0, 0.28412449, 0.75629334, 0.0796189,  0.0, 0.0]

        oper = AssociationRule(self.features)

        cut = oper.get_cut_point(0, len(self.features))

        rule = oper.build_rule(vector)

        antecedent, consequence = oper.get_ant_con(rule, cut)

        support, confidence = oper.calculate_support_confidence(
                antecedent, consequence, self.transactions)
        
        # TODO
        self.assertEqual(antecedent, antecedent_a)
        #self.assertEqual(consequence, consequence_a)
        #self.assertEqual(support_a, support)
        #self.assertEqual(confidence_a, confidence)


    def test_B(self):
        # Rule: B => 1
        antecedent_b = [['B']]

        consequence_b = [[1, 1]]

        support_b = 0.2857142857142857

        confidence_b = 0.666666666667

        vector =  [0.95157038, 0.17362622, 1.0, 0.34473467, 0.65286096, 0.22928163, 0.68833485]

        oper = AssociationRule(self.features)

        cut = oper.get_cut_point(0, len(self.features))

        rule = oper.build_rule(vector)

        antecedent, consequence = oper.get_ant_con(rule, cut)

        support, confidence = oper.calculate_support_confidence(
                antecedent, consequence, self.transactions)

        self.assertEqual(antecedent, antecedent_b)
        self.assertEqual(consequence, consequence_b)
        self.assertEqual(support_b, support)
        self.assertAlmostEqual(confidence_b, confidence)
