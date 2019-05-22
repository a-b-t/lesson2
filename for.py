"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, 
                 {'school_class': '4b', 'scores': [4, 5, 5, 5, 5]},
                 {'school_class': '4c', 'scores': [2, 2, 2, 2, 2]},
                 {'school_class': '4d', 'scores': [3, 4, 4, 3, 3]}
                ]


avg_score_school = 0
for i in range(len(school_scores)):
    avg_score_class = sum(school_scores[i]['scores'])/len(school_scores[i]['scores'])
    print('Средний балл класса {} равен {}'.format(school_scores[i]['school_class'], avg_score_class))
    avg_score_school += avg_score_class/len(school_scores)

print('Средний балл по школе равен {}'.format(avg_score_school))
