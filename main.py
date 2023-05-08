
class SATSolver:

    def __init__(self, file_txt):
        with open(file_txt, 'r') as file:
            lines = list(file.read().split('\n'))
            for line in lines:
                if line[:5] == 'p cnf':
                    self.num_vars, self.num_clauses = map(int, line[6:].split())
                    self.result = {i: True for i in range(1, self.num_vars + 1)}
                    self.clauses = list()

                elif line[0] != 'c':
                    temp = set(map(int, line[:-2].split()))
                    # print(temp)
                    self.clauses.append(temp)

    def del_uno(self, cnf):
        # print('del uno 1', cnf)
        for c in cnf:
            if len(c) == 1:
                for l in c:
                    if l > 0:
                        self.result[l] = True
                    else:
                        self.result[-l] = False
                    cnf = [i.difference({-l}) for i in cnf]

                    if c in cnf:
                        # print(c)
                        # print('del uno 1', cnf)
                        cnf.remove(c)

                    # print(cnf)
        # print('del uno', cnf)
        # print('del uno', self.result)
        return cnf

    def del_pure(self, cnf):
        # print('del pure 1', cnf)
        for l in range(1, self.num_vars + 1):
            flag = None
            for c in cnf:
                if l in c and flag is None:
                    flag = True
                elif -l in c and flag is None:
                    flag = False
                elif (l in c and not flag) or (-l in c and flag):
                    flag = None
                    break
            if type(flag) == bool:
                self.result[abs(l)] = flag
                for c in cnf:
                    if l in c or -l in c:
                        cnf.remove(c)

        # print('del pure', cnf)
        # print('del pure', self.result)

        return cnf

    def dpll(self, cnf):
        # print(cnf)
        # print(self.result)
        cnf = self.del_uno(cnf)
        cnf = self.del_pure(cnf)

        if len(cnf) == 0:
            return True

        if any([len(c) == 0 for c in cnf]):
            return False

        for l in cnf[0]:
            literal = l
            break
        if literal > 0:
            flag = True
        else:
            flag = False

        # выкинули истинные клозы и из клоз еще ложную литеру
        new_cnf = [c for c in cnf if literal not in c]
        new_cnf = [c.difference({-literal}) for c in new_cnf]

        sat = self.dpll(new_cnf)
        if sat:
            self.result[abs(literal)] = flag
            return sat

        new_cnf = [c for c in cnf if -literal not in c]
        new_cnf = [c.difference({literal}) for c in new_cnf]

        sat = self.dpll(new_cnf)
        if sat:
            self.result[abs(literal)] = not flag
            return sat

        return False

    def check_model(self):
        ans = True
        for c in self.clauses:
            temp = False
            for l in c:
                if l > 0:
                    temp = temp or self.result[l]
                else:
                    temp = temp or (not self.result[-l])
            ans = ans and temp
        return ans


