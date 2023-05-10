
class SATSolver:

    def __init__(self, file_txt):
        with open(file_txt, 'r') as file:
            lines = list(file.read().split('\n'))
            for line in lines:
                if line[:5] == 'p cnf':
                    self.num_vars, self.num_clauses = map(int, line[6:].split())
                    self.__result = {i: True for i in range(1, self.num_vars + 1)}
                    self.__clauses = list()

                elif line[0] != 'c':
                    temp = set(map(int, line[:-2].split()))
                    self.__clauses.append(temp)

    def __del_uno(self, cnf):
        for c in cnf:
            if len(c) == 1:
                for l_ in c:
                    if l_ > 0:
                        self.__result[l_] = True
                    else:
                        self.__result[-l_] = False
                    cnf = [i.difference({-l_}) for i in cnf]

                    if c in cnf:
                        cnf.remove(c)

        return cnf

    def __del_pure(self, cnf):
        # print('del pure 1', cnf)
        for l_ in range(1, self.num_vars + 1):
            flag = None
            for c in cnf:
                if l_ in c and flag is None:
                    flag = True
                elif -l_ in c and flag is None:
                    flag = False
                elif (l_ in c and not flag) or (-l_ in c and flag):
                    flag = None
                    break
            if type(flag) == bool:
                self.__result[abs(l_)] = flag
                for c in cnf:
                    if l_ in c or -l_ in c:
                        cnf.remove(c)

        return cnf

    def DPLL(self):
        is_sat = SATSolver.__dpll(self, self.__clauses)
        if is_sat:
            return is_sat, self.__result
        else:
            return is_sat, None

    def __dpll(self, cnf):
        cnf = self.__del_uno(cnf)
        cnf = self.__del_pure(cnf)

        if len(cnf) == 0:
            return True

        if any([len(c) == 0 for c in cnf]):
            return False

        for l_ in cnf[0]:
            literal = l_
            break
        if literal > 0:
            flag = True
        else:
            flag = False

        # remove true clauses
        new_cnf = [c for c in cnf if literal not in c]
        # remove false literal
        new_cnf = [c.difference({-literal}) for c in new_cnf]

        sat = self.__dpll(new_cnf)
        if sat:
            self.__result[abs(literal)] = flag
            return sat

        new_cnf = [c for c in cnf if -literal not in c]
        new_cnf = [c.difference({literal}) for c in new_cnf]

        sat = self.__dpll(new_cnf)
        if sat:
            self.__result[abs(literal)] = not flag
            return sat

        return False

    def check_model(self):
        ans = True
        for c in self.__clauses:
            temp = False
            for l_ in c:
                if l_ > 0:
                    temp = temp or self.__result[l_]
                else:
                    temp = temp or (not self.__result[-l_])
            ans = ans and temp

        return ans
