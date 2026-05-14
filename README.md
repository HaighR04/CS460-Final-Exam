# The Torchbearer

**Student Name:** Ryan Haigh
**Student ID:** 130419637
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single run from S will find the shortest path to each location, but is not able to identify the order that each relic should be visited in. 
  This requires the algorithm to compare a number of complete routes through each chamber.

- **What decision remains after all inter-location costs are known:**
  After all inter-location costs are known, the order of relic chambers to visit is the last decision to make, as that will determine the final cost of the path through the dungeon.

- **Why this requires a search over orders (one sentence):**
  Since there is not a calculation that immediately determines the optimal visit sequence, the planner has to evaluate different orderings of the chambers to find the best (lowest-cost) traversal.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Spawn(s) | Starting point for the Torchbearer, needed for costs from S to each relic |
| Each Relic Chamber | After each relic is visited, the next destination could be another relic, or T |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested Dictionary |
| What the keys represent | Each source node (S and each relic) |
| What the values represent | Mapped destination nodes to their minimum fuel cost |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionary uses hashing, giving a constant time for accessing keys |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1, one from S and one from each of the k relics
- **Cost per run:** O(M logn), where M is the number of relic chambers
- **Total complexity:** O((k + 1) * M logn)
- **Justification (one line):** Every run will process each edge once with a heap, and it is ran once per source

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  When a node is added to the finalized set, the recorded distance is permanent, meaning no future path through unfinalized nodes could be cheaper, as all edge weights are nonnegative.
- **For nodes not yet finalized (not in S):**
  The node's current distance is the best that has been located so far, but only looking at paths where the intermediate stops are finalized. A cheaper path is still possible.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Before iteration, the only nodes is the source with distance 0, and nothing is finalized. This is trivially correct, as the shortest path from the source to itself is 0, and each other node is infinity.

- **Maintenance : why finalizing the min-dist node is always correct:**
  When the finalized min-dist node u is popped, it becomes finalized. It is safe because all of the edge weights are nonnegative, so any other path to u would be required to pass through another unfinalized node. 
  This would cost at least as much as the current estimate of u, so no cheaper path to u can exist.

- **Termination : what the invariant guarantees when the algorithm ends:**
  When the heap is empty, that means that each node that is reachable has been finalized, and by the invariant, every finalized node has their true shortest distance,
  meaning that the dictionary that is returned is fully correct.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

This matters because if Dijkstra produced incorrect distances, the planner would make routing decisions that are based on wrong fuel costs, and it might
select a route that is suboptimal or even impossible.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Greedy will always pick the closest unvisited relic chamber next, but a cheaper first choice could force future choices to be more expensive, which would make the total cost worse overall than a route that started with a more expensive step.
- **Counter-example setup:** Using the distance table from the spec, but with S -> B = 3.
- **What greedy picks:** In this scenario, greedy would choose S -> C (cost of 2) as C is the closest, then B (cost 1), then D (cost 1), and then T (cost 100) for a total of 2 + 1 + 1 + 100 = 104.
- **What optimal picks:** Optimal would first choose B (cost 3), then D (cost 1), then C (cost 1), then finally T (cost 1) for a total of 3 + 1 + 1 + 1 = 6
- **Why greedy loses:** Greedy committed to C first because it was the cheapest from S, but it did not know that the path forces D to be last, costing 100 to reach T.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore each possible order where the relic chambers can be visited, comparing the total fuel costs of all valid orderings to find the global minimum.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | Has position of Torchbearer at the current moment |
| Relics already collected | relics_remaining | set | Which relics still need to be visited |
| Fuel cost so far | cost_so_far | float | Total fuel used to reach the current state |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | Set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | The backtracking step needs to be able to add and remove quickly, and a set gives O(1) for both |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** k!
- **Why:** At each you choose from the remaining unvisited relics, and with k choices, then k -1, then k-1, this could result in k!

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The lowest cost route found so far, both the total fuel cost in best[0] and the ordering of relics in best[1]
- **When it is used:** At the start of each _explore call before work is done, so that it can check if the current branch can even beat it.
- **What it allows the algorithm to skip:** It skips any branch where the cost_so_far is either equal to or greater than best[0], as nonnegative edge weights mean that the cost will only increase.

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** At this state, we have the cost_so_far (fuel that has already been spent), relics_remaining (which relics still need visiting),  and dist_table (cheapest travels costs between all relveant nodes)
- **What the lower bound accounts for:** It accounts for the cheapest possible way to finish from the current state. This means the minimum cost to reach any of the remaining relcis from the current location plus the miminum cost for any of the remaining relics to T.
- **Why it never overestimates:** THis takes the single cheapest option for each of the remaining legs independently, which is always optimistic, and the actual path has to connect these in some specific order that could only cost more.

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
