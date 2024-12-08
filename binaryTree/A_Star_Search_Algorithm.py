g_distances = {
    "Arad": [["Timisoara", 118], ["Zerind", 75], ["Sibiu", 140]],
    "Bucharest": [["Pitesti", 101], ["Urziceni", 85], ["Giurgiu", 90]],
    "Craiova": [["Drobeta", 120], ["Rimnicu Vilcea", 146], ["Pitesti", 138]],
    "Drobeta": [["Craiova", 120], ["Mehadia", 75]],
    "Eforie": [["Hirsova", 86]],
    "Fagaras": [["Sibiu", 99], ["Bucharest", 211]],
    "Giurgiu": [["Bucharest", 90]],
    "Hirsova": [["Eforie", 86], ["Urziceni", 98]],
    "Iasi": [["Neamt", 87], ["Vaslui", 92]],
    "Lugoj": [["Timisoara", 111], ["Mehadia", 70]],
    "Mehadia": [["Drobeta", 75], ["Lugoj", 70]],
    "Neamt": [["Iasi", 87]],
    "Oradea": [["Zerind", 71], ["Sibiu", 151]],
    "Pitesti": [["Bucharest", 101], ["Craiova", 138], ["Rimnicu Vilcea", 97]],
    "Rimnicu Vilcea": [["Craiova", 146], ["Sibiu", 80], ["Pitesti", 97]],
    "Sibiu": [["Fagaras", 99], ["Rimnicu Vilcea", 80], ["Oradea", 151], ["Arad", 140]],
    "Timisoara": [["Arad", 118], ["Lugoj", 111]],
    "Urziceni": [["Bucharest", 85], ["Hirsova", 98], ["Vaslui", 142]],
    "Vaslui": [["Iasi", 92], ["Urziceni", 142]],
    "Zerind": [["Arad", 75], ["Oradea", 71]]
}


h_distances = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

# Initialize cost dictionary
cost = {"Arad": 0}  # Starting from Arad

def AStarSearch(goal):
    global g_distances, h_distances
    closed = []             # closed nodes
    opened = [["Arad", 366]]     # opened nodes

    '''find the visited nodes'''
    while True:
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == goal:        # break the loop if node G has been found
            break
        for item in g_distances[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]:int(cost[node]) + item[1]})            # add nodes to cost dictionary
            fn_node = cost[node] + h_distances[item[0]] + item[1]     # calculate f(n) of current node
            temp = [item[0], fn_node]
            opened.append(temp)                                     # store f(n) of current node in array opened

    '''find optimal sequence'''
    trace_node = goal                        # correct optimal tracing node, initialize as node G
    optimal_sequence = [goal]                # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # current node
        if trace_node in [children[0] for children in g_distances[check_node]]:
            children_costs = [temp[1] for temp in g_distances[check_node]]
            children_nodes = [temp[0] for temp in g_distances[check_node]]

            '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
            change the correct optimal tracing node to current node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence


if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch(goal="Bucharest")
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))
