SATsolver на основе алгоритма DPLL
Пример использования:
```python
ss = SATSolver('tests/test1.txt') # путь до файла в формате DIMACS
res = ss.dpll(ss.clauses) # True - satisfiable, False - unsatisfiable
model = ss.result # Если True, то здесь будет соответствующие значения переменных
check = ss.check_model() # Можно проверить, что формула при полученных значений переменных satisfiable
```
