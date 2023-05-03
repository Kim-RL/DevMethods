# Зависимости:

* Tensorflow 1.1+
* Pygmo 2.9 + 
* Keras 2.1+
* numpy 1.14+

# Задачи проекта:
В этом проекте исследуется примнение метаэвристических алгоритмов к оптимизации весов нейронных сетей. Рассматривается оптимизация весов в следующих архитектурах: 
1. Полносвязная - dense.py, задача классификации на датасете MNIST.
2. Рекуррентная - rnn.py, задача бинарной класиификации на датасете IMDB.
3. Сверточная - cnn.py, задача классификации на датасете MNIST.

# Использование:

Для тестирования метаэвристических алгоритмов на примерах 1)-3) необходимо выбрать конфигурацию алгоритма, заполнив файл config.json, и запустить одну из команд:

* python dense.py
* python rnn.py
* python cnn.py

В файле config.json в поле "algo" должно быть записано название одного из алгоритмов оптимизации доступных в Pygmo, остальные поля - параметры алгоритмов. С доступными алгоритмами и параметрами можно ознакомиться здесь: https://esa.github.io/pagmo2/.

После завершения работы скрипта лучший набор весов будет сохранен в файл best_weights_X.bin, а значение качества работы сети при этом наборе весов в файл result_X.json. (X=dense/rnn/cnn).

Для тестирования метаэвристических алгоритмов оптимизации на произволной архитектуре необходимо реализовать саму нейронную сеть и функцию "приспособленности", которая принимая на вход вектор весов сети распределят их по слоям и возвращает качесвто работы сети. При этом, если небходимо максимизировать качество, то функция приспособленности должна возвращать отрицательное значение: 

```python
def eval_func(weights):
    ...
    return -1.*quality
```

Далее необходимо задать задачу оптимизации и создать экземляр оптимизатора:
```python
from scripts.problem import Problem
from scripts.genboost import GenBoost

my_prob = Problem(fit_func=eval_model, dim=N, lb=-l, rb=r)
gb = GenBoost(problem=my_prob)
```

dim - число весов сети.
lb, rb - верхняя и нижняя границы значений весов сети.

Для запуска оптимизации:
```python
with open('config.json') as json_data:
    params = json.load(json_data)
pop = gb.run(params)
```

После окончания процесса оптимизации переменная pop будет содержать результирующее множнство наборов весов сети. 

Лучший набор весов и его качество:
```python
pop.champion_x
pop.champion_f
```
