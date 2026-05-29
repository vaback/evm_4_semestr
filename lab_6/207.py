class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Строим граф: для каждого курса список курсов, которые от него зависят
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Состояния:
        # 0 = не посещен
        # 1 = в процессе обработки (в текущем DFS пути)
        # 2 = полностью обработан (циклов не найдено)
        state = [0] * numCourses
        
        def has_cycle(course):
            # Если курс уже в процессе обработки -> нашли цикл
            if state[course] == 1:
                return True
            # Если курс уже обработан -> циклов от него нет
            if state[course] == 2:
                return False
            
            # Помечаем как "в процессе"
            state[course] = 1
            
            # Проверяем всех соседей (зависимые курсы)
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            # Помечаем как "обработан"
            state[course] = 2
            return False
        
        # Проверяем каждый курс (граф может быть несвязным)
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True