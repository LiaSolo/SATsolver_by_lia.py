import matplotlib.pyplot as plt
import statistics
from scipy.stats import normaltest, norm, sem

with open('time2.txt', 'r') as file1:
    time1 = list(map(float, file1.readlines()))
    print(time1)

n = normaltest(time1)
print(normaltest(time1))

plt.hist(time1, color='#FF1493')
plt.show()

avg = statistics.mean(time1)
print('Среднее арифметическое: ', avg)

st_dev = statistics.stdev(time1)
print('Стандартное отклонение: ', st_dev)

st_dev_sem = sem(time1)
print('Стандартное отклонение среднего: ', st_dev_sem)

ratio = float('%s' % float('%.1g' % (st_dev/avg * 100)))
print(f'Отношение среднего отклонения к среднему: ~{ratio}%')

conf_interval = norm.interval(confidence=0.95, loc=avg, scale=st_dev_sem)
len_conf = conf_interval[1] - conf_interval[0]
print('Половина длины доверительного интервала: ', len_conf/2)
print(f'95%-доверительный интервал: {"%s" % float("%.3g" % avg)} ± '
      f'{"%s" % float("%.1g" % (len_conf / 2))}')

print('Половина длины предсказывающего интервала: ', 2 * st_dev)
print(f'95%-предсказывающий интервал: {"%s" % float("%.2g" % avg)} ± '
      f'{"%s" % float("%.g" % (2 * st_dev))}')
