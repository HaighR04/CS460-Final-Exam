# Development Log – The Torchbearer

**Student Name:** Ryan Haigh
**Student ID:** 130419637

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/10/26]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

This assignment focuses on the torchbearer, which is a robot that must begin at entrance S, then traverse through every relic chamber in set M at least once, then finally exit through T, all while using the minimum possible fuel. Since this dungeon is a weighted directed graph, edges will only go one way with a cost.

The important focus is first locating the shortest path to each room, as well as connections between them, and then once all paths are discovered, connect the shortest order of room traversals from start to finish
to ensure that the route is really the "shortest path"

I think the first thing that needs to be implemented is run_dijkstra, since this is what everything else relies on for the correct shortest-path distances. Looking at the program, _explore looks to be the most difficult part due to the pruning aspect, as getting that, backtracking, and the base case all correct at the same time will be tough. For testing, the four provided test cases would be a good start, then I will try some small graphs that I make so that I can verify the answers myself.

---

## Entry 2 – [5/10/26]: Work through Part 1, 2, and 3, as well as implementing the code for Part 2 and Part 3

I read through all the files and took notes on the order that I should complete everything. I reasoned through run_dijkstra's, and realized an edge case that I might have missed had I not fully read through it.
This edge case regarded nodes that do not have outgoing nodes, and are mentioned in other noes, ie 'B': [('C', 2)], where B would be considered a key, but C is not included in graph, and therefore might get ignored
I completed my goal of finishing Parts 1, 2, and 3 for both torchbearer and README, and will re-read over README and ASSIGNMENT today, and continue with Part 4 and 5 tomorrow.
---

## Entry 3 – [5/12/26]: Implementation of Part 5 and ensuring that it backtracks through the relics properly with pruning

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

While working through Part 5 and filling out find_optimal_route and _explore, I was taking a little while to figure out how I was going to implement the pruning and backtracking aspect. I was able to figure out the recursive case and base case, but I completely blanked on what the pruning condition would need to be. As I was working through the function, I think I tried to add it somewhere within the recursive case. Once I had written the recursive case fully and was writing out examples on my paper, I realized that it would not work properly in that part of the function, and figured that adding it at the beginning would remove any unnecssary recursion or base case checking if the cost was already suboptimal.
---
## Entry 4 - [5/14/26]: Fell asleep working on some of the stuff and realized I implemented them wrong.

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

I was really busy during 5/13 and intended to work on some of the explain portions, but I only did it right before I went to bed and realized today that I not only just wrote wrong information for some of them, but I also forgot to update the pruning condition with the work from Part 6b. Today, I was able to not only fix some of my typing errors, but ensure that the pruning condition was correctly and properly commented. It took me a little while to fully understand the importance between the cost_so_far >= best and lower_bound implementation.

## Entry 5 – [5/14/26]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

I feel like the time I was given was proper for this assignment, I was just not as efficient as I should have been. Luckily, I listened to the Professor's warning about starting late, which definitely saved me. I did have to go over the lecture slides quite a bit to make sure I was managing each part of the search in the right way, but it was useful for finalizing the project. Given more time, I could have implemented some sort of comparison mechanism between different search algorithms to show the true efficiency of the optimal search using the lower_bound pruning, but that was not necessary, and would have just acted as the cherry on top. Other than that, I should have just focused more during the sessions I was working so I wouldn't have to go back over my work to fix stupid mistakes. The time estimates vary based on my level of attentiveness, such as Part 3 where I was insanely locked in but Part 6 got me stuck.


---

## Final Entry – [5/14/26]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1 hour |
| Part 2: Precomputation Design | 1 hour |
| Part 3: Algorithm Correctness | 30 minutes |
| Part 4: Search Design | 1 hour |
| Part 5: State and Search Space | 2 hours |
| Part 6: Pruning | 1.5 hours |
| Part 7: Implementation | 2 hour |
| README and DEVLOG writing | 1.5 hours |
| **Total** | 10.5 hours |
