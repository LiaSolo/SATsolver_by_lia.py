import unittest
from main import SATSolver


# общее время работы тестов ~ 7 мин
class SATSolverTester(unittest.TestCase):

    def test_true_1(self):
        ss = SATSolver('tests/test1.txt')
        res = ss.dpll(ss.clauses)
        check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_1: is sat')
        self.assertEqual(True, check, 'oops in test_true_1: model')

    def test_true_2(self):
        ss = SATSolver('tests/test2.txt')
        res = ss.dpll(ss.clauses)
        check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_2: is sat')
        self.assertEqual(True, check, 'oops in test_true_2: model')

    def test_true_3(self):
        ss = SATSolver('tests/test3.txt')
        res = ss.dpll(ss.clauses)
        check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_3: is sat')
        self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_4(self):
        ss = SATSolver('tests/test4.txt')
        res = ss.dpll(ss.clauses)
        check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_4: is sat')
        self.assertEqual(True, check, 'oops in test_true_4: model')

    def test_true_5(self):
        ss = SATSolver('tests/uf75-099.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_5: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_6(self):
        ss = SATSolver('tests/flat30-13.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_6: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_7(self):
        ss = SATSolver('tests/flat50-102.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_7: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_8(self):
        ss = SATSolver('tests/uf20-01000.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_8: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_9(self):
        ss = SATSolver('tests/uf50-0101.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_9: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_10(self):
        ss = SATSolver('tests/uf100-016.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_10: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_11(self):
        ss = SATSolver('tests/uf125-04.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_11: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_12(self):
        ss = SATSolver('tests/uf100-0167.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_12: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_13(self):
        ss = SATSolver('tests/uf75-0100.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_13: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_true_14(self):
        ss = SATSolver('tests/uf75-02.cnf')
        res = ss.dpll(ss.clauses)
        # check = ss.check_model()

        self.assertEqual(True, res, 'oops in test_true_14: is sat')
        # self.assertEqual(True, check, 'oops in test_true_3: model')

    def test_false_1(self):
        ss = SATSolver('tests/test5.txt')
        res = ss.dpll(ss.clauses)
        check = ss.check_model()

        self.assertEqual(False, res, 'oops in test_false_1: is sat')
        self.assertEqual(False, check, 'oops in test_false_1: model')

    def test_false_2(self):
        ss = SATSolver('tests/uuf50-0218.cnf')
        res = ss.dpll(ss.clauses)

        self.assertEqual(False, res, 'oops in test_false_2: is sat')

    def test_false_3(self):
        ss = SATSolver('tests/uuf50-0999.cnf')
        res = ss.dpll(ss.clauses)

        self.assertEqual(False, res, 'oops in test_false_3: is sat')

    def test_false_4(self):
        ss = SATSolver('tests/uuf50-0100.cnf')
        res = ss.dpll(ss.clauses)

        self.assertEqual(False, res, 'oops in test_false_3: is sat')

    def test_false_5(self):
        ss = SATSolver('tests/uuf75-04.cnf')
        res = ss.dpll(ss.clauses)

        self.assertEqual(False, res, 'oops in test_false_3: is sat')


if __name__ == '__main__':
    unittest.main()
