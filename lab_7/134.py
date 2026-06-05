class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # Жадный алгоритм O(n)
        total_gas = 0
        total_cost = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]
            
            # Если на текущей станции бак становится отрицательным,
            # значит нельзя начать с предыдущих стартовых позиций
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        
        return start_index if total_gas >= total_cost else -1