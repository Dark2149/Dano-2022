import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Установка рабочей директории (в Python обычно не требуется)
# В Python можно использовать полные пути к файлам

# Загрузка данных
Data15 = pd.read_csv("result2015m2.csv", sep=";", decimal=",")
Data20 = pd.read_csv("result2020m.csv", sep=";", decimal=",")
Data21 = pd.read_csv("result2021m.csv", sep=";", decimal=",")
Data22 = pd.read_csv("result2022m.csv", sep=";", decimal=",")
Data14 = pd.read_csv("Северо-Западный.csv", sep=";", decimal=",")

# Функция для преобразования строковых значений с запятыми в числовые значения с точками
def dot(x):
    for col in x.columns:
        try:
            x[col] = x[col].str.replace(',', '.').astype(float)
        except:
            pass
    return x

# Применение функции к данным
Data212 = dot(Data21)
Data152 = dot(Data15)

# Проверка типа данных колонки
is_numeric = pd.api.types.is_numeric_dtype(Data15['Средний.балл.ЕГЭ.студентов..принятых.по.результатам.ЕГЭ.на.обучение.по.очной.форме.по.программам.бакалавриата.и.специалитета.за.счет.средств.соответствующих.бюджетов.бюджетной.системы.РФ'])

# Получение имен колонок
names_data20 = Data20.columns

# Подмножество данных без Москвы и Санкт-Петербурга
h = Data22[(Data22['Region'] != "г.Москва") & (Data22['Region'] != "г.Санкт-Петербур")]
p = h['Доходы.вуза..из.всех.источников'].sort_values().iloc[109:369]
v = h['Доходы.вуза..из.всех.источников'].sort_values().iloc[370:476]
k = h['Доходы.вуза..из.всех.источников'].sort_values().iloc[476:556]

# Построение графиков
plt.figure()
plt.bar(range(len(p)), p)
plt.title('p')
plt.figure()
plt.bar(range(len(v)), v)
plt.title('v')
plt.figure()
plt.bar(range(len(k)), k)
plt.title('k')

# Фильтрация данных
m21 = Data21[(Data21['Region'] != "г.Москва") & (Data21['Region'] != "г.Санкт-Петербург")]
m21a = m21[m21['Доходы.вуза..из.всех.источников'] < 1000000]
m21a = dot(m21a)

# Построение графика отсортированных доходов
plt.figure()
plt.bar(range(len(m21a['Доходы.вуза..из.всех.источников'].sort_values())), 
        m21a['Доходы.вуза..из.всех.источников'].sort_values())
plt.title('Sorted income of universities')

# Выборка целевых университетов по ID
target_ids = [1, 14, 36, 44, 57, 60, 70, 130, 131, 155, 168, 201, 210, 228, 252, 257, 258, 261, 
              284, 287, 301, 318, 1558, 1562, 1607, 1638, 1650, 1673, 1682, 1722, 1755, 1846, 
              1847, 1848, 1861, 1967, 110317]

cel15 = Data15[Data15['ID'].isin(target_ids)]
cel20 = Data20[Data20['ID'].isin(target_ids)]
necel15 = Data15[~Data15['ID'].isin(target_ids)]
necel20 = Data20[~Data20['ID'].isin(target_ids)]

# Загрузка дополнительных данных
Data15_00 = pd.read_csv("2015_00.csv", sep=";", decimal=",")
Data20_00 = pd.read_csv("2020_00.csv", sep=";", decimal=",")
Data15_0x = pd.read_csv("2015_0x.csv", sep=";", decimal=",")
Data20_0x = pd.read_csv("2020_0x.csv", sep=";", decimal=",")
Data15_x0 = pd.read_csv("2015_x0.csv", sep=";", decimal=",")
Data20_x0 = pd.read_csv("2020_x0.csv", sep=";", decimal=",")
Data15_xx = pd.read_csv("2015_xx.csv", sep=";", decimal=",")
Data20_xx = pd.read_csv("2020_xx.csv", sep=";", decimal=",")

# Расчет разницы в цитированиях
g15 = Data15_00['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
g20 = Data20_00['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gn15 = Data15_0x['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gn20 = Data20_0x['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gnx15 = Data15_x0['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gnx20 = Data20_x0['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gny15 = Data15_xx['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']
gny20 = Data20_xx['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР']

y = g20 - g15
yn = gn20 - gn15
ynx = gnx20 - gnx15
yny = gny20 - gny15

# Построение гистограммы
plt.figure()
plt.hist(cel15['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'])
plt.title('Histogram of grants per 100 NPR')

# Построение диаграммы размаха
plt.figure()
plt.boxplot([
    Data15_0x['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'] - 
    Data20_0x['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'],
    Data15_xx['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'] - 
    Data20_xx['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'],
    Data15_00['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР'] - 
    Data20_00['Количество.полученных.грантов.за.отчетный.год.в.расчете.на.100.НПР']
])
plt.title('Boxplot of grant differences')

# Очистка данных от выбросов
cel15 = cel15[cel15['ID'] != 1967]
cel20 = cel20[cel20['ID'] != 1967]
necel15 = necel15[necel15['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР'] < 800]
necel20 = necel20[necel20['Количество.цитирований.публикаций..изданных.за.последние.5.лет..индексируемых.в.информационно.аналитической.системе.научного.цитирования.Scopus.в.расчете.на.100.НПР'] < 800]

# Очистка данных от выбросов (продолжение)
gn15 = gn15[gn15 < 400]
gn20 = gn20[gn20 < 400]
yn = yn[(yn < 500) & (yn > -500)]
y = y[(y > np.quantile(y, 0.05)) & (y < np.quantile(y, 0.95))]
yny = yny[(yny > np.quantile(yny, 0.05)) & (yny < np.quantile(yny, 0.93))]
ynx = ynx[ynx < 1000]

# Расчет медиан
print("Median y:", np.median(y))
print("Median yn:", np.median(yn))

# Проверка на нормальность
print("Shapiro-Wilk test for y:", stats.shapiro(y))
print("Shapiro-Wilk test for yn:", stats.shapiro(yn))
print("Shapiro-Wilk test for ynx:", stats.shapiro(ynx))
print("Shapiro-Wilk test for yny:", stats.shapiro(yny))

# Тест Краскела-Уоллиса
print("Kruskal-Wallis test:", stats.kruskal(y, yn, ynx, yny))

# Симуляция для теста Вилкоксона
m = []
for i in range(10000):
    b = np.random.choice(ynx, 37, replace=False)
    m.append(stats.wilcoxon(yn, b).pvalue)

p_values = np.array(m)
plt.figure()
plt.hist(p_values)
plt.title('Histogram of p-values')

print("Shapiro-Wilk test for p-values:", stats.shapiro(m))
print("Median of p-values:", np.median(m))
print("Number of p-values < 0.05:", sum(m < 0.05))

# Расчет медиан доходов
print("Median income Data20_00:", np.median(Data20_00['Доходы.вуза..из.всех.источников']))
print("Median income Data20_0x:", np.median(Data20_0x['Доходы.вуза..из.всех.источников']))
print("Median income Data20_x0:", np.median(Data20_x0['Доходы.вуза..из.всех.источников']))
print("Median income Data20_xx:", np.median(Data20_xx['Доходы.вуза..из.всех.источников']))

# Установка локали для русского языка (в Python это делается иначе)
# В Python для работы с русским языком обычно используется кодировка UTF-8
