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

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | ~1 hour|
| Part 2: Precomputation Design | ~1.5 hours|
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
