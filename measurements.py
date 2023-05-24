import time
from main import SATSolver

time0 = list()
for _ in range(40):
    start = time.time()

    ss = SATSolver('tests\\uf75-02.cnf')
    is_sat, model = ss.DPLL()

    end = time.time()
    time0.append('%s' % float('%.3g' % (end - start)))
