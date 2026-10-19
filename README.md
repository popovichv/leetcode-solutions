# LeetCode Solutions

My personal tracker of the LeetCode problems I have solved. Each file has a
written explanation of the idea behind the solution, its time and space
complexity, and the code.

## Structure

```
problems/
  0001-two-sum.md        # <4-digit problem number>-<kebab-case-title>.md
update_readme.py         # regenerates the Solved table below
```

Every file follows the same layout:

- `# <number>. <Title>`: heading matching the LeetCode problem
- `**Difficulty:**` and `**Topics:**`: tag lines right under the heading, the
  first ending in two spaces so GitHub keeps them on separate lines
- the problem statement, straight from LeetCode
- `## Explanation`: how the solution works, and nothing else
- `## Code`: time/space complexity, then the implementation

When a problem has several worthwhile approaches, I split both sections into
matching `### <Name> Method` subsections, so each explanation sits next to the
code it describes.

The Solved table below is generated from these files using `update_readme.py` script.

## Solved (15)

| #    | Problem                                                                                                                       | Difficulty | Topics                     | Time     | Space  |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------- | -------- | ------ |
| 1    | [Two Sum](problems/0001-two-sum.md)                                                                                           | Easy       | Array, Hash Table          | `O(n)`   | `O(n)` |
| 14   | [Longest Common Prefix](problems/0014-longest-common-prefix.md)                                                               | Easy       | String                     | `O(s*m)` | `O(m)` |
| 20   | [Valid Parenthesis](problems/0020-valid-parenthesis.md)                                                                       | Easy       | String, Stack              | `O(n)`   | `O(n)` |
| 21   | [Merge Two Sorted Lists](problems/0021-merge-two-sorted-lists.md)                                                             | Easy       | Linked List                | `O(n+m)` | `O(1)` |
| 27   | [Remove Duplicates](problems/0027-remove-element.md)                                                                          | Easy       | Array, Two Pointers        | `O(n)`   | `O(1)` |
| 155  | [Min Stack](problems/0155-min-stack.md)                                                                                       | Medium     | Stack, Design              | `O(1)`   | `O(n)` |
| 169  | [Majority Element](problems/0169-majority-element.md)                                                                         | Easy       | Array, Hash Table          | `O(n)`   | `O(n)` |
| 206  | [Reverse Linked List](problems/0206-reverse-linked-list.md)                                                                   | Easy       | Linked List                | `O(n)`   | `O(1)` |
| 217  | [Contains Duplicate](problems/0217-contains-duplicate.md)                                                                     | Easy       | Array, Hash Table, Sorting | `O(n)`   | `O(n)` |
| 242  | [Valid Anagram](problems/0242-valid-anagram.md)                                                                               | Easy       | String, Hash Table         | `O(n)`   | `O(n)` |
| 485  | [Max Consecutive Ones](problems/0485-max-consecutive-ones.md)                                                                 | Easy       | Array                      | `O(n)`   | `O(1)` |
| 682  | [Baseball Game](problems/0682-baseball-game.md)                                                                               | Easy       | Array, Stack               | `O(n)`   | `O(n)` |
| 707  | [Design Linked List](problems/0707-design-linked-list.md)                                                                     | Medium     | Linked List, Design        | `O(1)`   | `O(n)` |
| 1299 | [Replace Elements with Greatest Element on Right Side](problems/1299-replace-elements-with-greatest-element-on-right-side.md) | Easy       | Array                      | `O(n)`   | `O(1)` |
| 1929 | [Concatenation of Array](problems/1929-concatenation-of-array.md)                                                             | Easy       | Array                      | `O(n)`   | `O(n)` |
