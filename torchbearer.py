"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Ryan Haigh
Student ID:   130419637

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    
    """
    return """placeholder value until I fill this out with my actual answer from the README. 
    I just want to make sure that the test for non-empty string is working correctly before I write the full answer here."""


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    sources = set()
    sources.add(spawn)
    # exit_node does not get added as it should not be used as a source for dijkstra's algorithm since it is only the destination 
    for relic in relics:
        sources.add(relic)
    return list(sources)

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    dist = {}
    for node in graph:
        dist[node] = float('inf')
        for neighbor, _ in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = float('inf') # Makes sure that all nodes, even ones that only appear as neighbors, as in dist and assigned INF
    dist[source] = 0
    
    heap = [(0, source)]
    visited = set()
    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue # Skip since this node has already been visited and finalized
        visited.add(node)
        
        for neighbor, edge_cost in graph[node]: # Iterate through neighbors of the current node to find shorter path
            new_cost = cost + edge_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor)) # Add the neighbor to the heap with the updated cost for another exploration
            
    
    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    dist_table = {}
    sources = select_sources(spawn, relics, exit_node)
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    
    """
    return """
    Part 3a:
    - Finalized Nodes: dist[v] is the permanent and true shortest path distance from the source to v.
    - Unfinalized Nodes: dist[u] is the current shortest path from the source to u using only finalized nodes.
    
    Part 3b:
    - Initialization: The distance to source is 0, and is correct, and all other distances are infinity, since no path has been found yet.
    - Maintenance: The minimum unfinalized node is safe to finalize since nonnegative edge weights will ensure that there are no shorter
    paths that exist through the unfinalized nodes that remain.
    - Termination: Each node that is reachable has been finalized, which means that all distances are correct.
    
    Part 3c:
    - Distances that are not correct would lead to the planner potentially choosing a suboptimal or invalid route.

"""


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    
    """
    return """
    Why Greedy Fails:
    - Greedy will always pick the closeset unvisited relic chamber next, but a cheaper first choice might 
    force future choices to be more expensive, which would make the total cost worse overall compared to a route 
    that started with a more expensive first choice but allowed for cheaper future choices.
    - Counter-example: Using the distance table from spec, but S -> B = 3 instead of 1.
    - Greedy picks: Nearest relic chamber without looking ahead. S -> C (2), then C -> B (1), then B -> D (1), 
    then D -> T (100). Total = 2 + 1 + 1 + 100 = 104.
    - Optimal picks: the ordering of chambers that would minimize the total cost. S -> B (3), then B -> D (1), 
    then D -> C (1), then C -> T (1). Total = 3 + 1 + 1 + 1 = 6.
    - Why Greedy Loses: Greedy committed to C first because it was the cheapest from S, but it did not know 
    that the path forces D to be last, costing 100 to reach T. This is due to greedy's lack of ability to look \
    forward and consider possible penalties of early cheap choices.
    
    What the Algorithm Must Explore:
    - The algorithm must explore each possible order where the relic chambers canbe visited, comparing the total
    fuel costs of all valid orderings to find the global minimum.
    
"""


# =============================================================================
# PARTS 5 + 6
# =============================================================================
# I made this helper function to assist with the improved pruning condition. It isn't required but I 
def lower_bound(dist_table, current_loc, relics_remaining, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    current_loc : node
    relics_remaining : collection
        Set
    exit_node : node

    Returns
    -------
    float
    """
    
    if not relics_remaining:
        return dist_table[current_loc][exit_node]
    
    # The lowest cost step from the current location to any remaining relic
    min_to_next_relic = min(dist_table[current_loc][r] for r in relics_remaining)
    # The lowest cost step from any remaining relic to the exit node
    min_to_exit = min(dist_table[r][exit_node] for r in relics_remaining)
    
    return min_to_next_relic + min_to_exit


def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    best = [float('inf'), []] # Holds the current best solution
    relics_remaining = set(relics)
    _explore(dist_table, spawn, relics_remaining, [], 0, exit_node, best)
    return (best[0], best[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b. (Set)
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    # Pruning Condition
    
    # Pruning here is safe because the lower bound would never overestimate the remaining cost, as it 
    # assumes the cheapest next relic and cheapest exit independently. Since all of the edge weights 
    # are nonnegative, then true remaining cost >= lower_bound, so cost_so_far + lower_bound >= best[0], 
    # there is no possible complete route through the current branch that would beat best[0].
    lower_bound_cost = lower_bound(dist_table, current_loc, relics_remaining, exit_node)
    if cost_so_far + lower_bound_cost >= best[0]:
        return # Prune this branch since it won't lead to a better solution than the current best
    
    # Base Case
    if not relics_remaining:
        final_cost = cost_so_far + dist_table[current_loc][exit_node]
        if final_cost < best[0]:
            best[0] = final_cost
            best[1] = list(relics_visited_order)
        return
    
    # Recursive Case
    for relic in relics_remaining:
        travel_cost = dist_table[current_loc][relic]
        new_cost = cost_so_far + travel_cost
        
        relics_remaining.remove(relic) # Backtracking part, mark, recurse, then unmark
        relics_visited_order.append(relic)
        
        _explore(dist_table, relic, relics_remaining, relics_visited_order, new_cost, exit_node, best)
        
        relics_remaining.add(relic) # Undo the changes made before the recursive call
        relics_visited_order.pop()
        

# =============================================================================
# PIPELINE
# =============================================================================


def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
