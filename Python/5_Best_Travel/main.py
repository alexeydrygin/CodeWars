def choose_best_sum(t, k, ls):
    def find_best_sum(curr_sum, num_towns_visited, curr_index):
        if num_towns_visited == k:
            if curr_sum <= t:
                return curr_sum
            else:
                return float('-inf')
        if curr_index == len(ls):
            return float('-inf')
        with_curr_town = find_best_sum(curr_sum + ls[curr_index], num_towns_visited + 1, curr_index + 1)
        without_curr_town = find_best_sum(curr_sum, num_towns_visited, curr_index + 1)
        return max(with_curr_town, without_curr_town)
    
    best_sum = find_best_sum(0, 0, 0)
    if best_sum == float('-inf'):
        return None
    else:
        return best_sum
