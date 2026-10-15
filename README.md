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

The Solved table below is generated from these files rather than edited by hand:

```
py update_readme.py            # rewrite the table
py update_readme.py --check    # exit 1 if the table is out of date
```

Each row takes its number, title, difficulty and topics from the heading and
tag lines, and its complexities from the `## Code` section. When a file
documents several methods, the last one feeds the table, so each file builds up
to the solution I would reach for.

## Solved (6)

| #    | Problem                                                           | Difficulty | Topics                     | Time     | Space  |
| ---- | ----------------------------------------------------------------- | ---------- | -------------------------- | -------- | ------ |
| 1    | [Two Sum](problems/0001-two-sum.md)                               | Easy       | Array, Hash Table          | `O(n)`   | `O(n)` |
| 14   | [Longest Common Prefix](problems/0014-longest-common-prefix.md)   | Easy       | String                     | `O(s*m)` | `O(m)` |
| 217  | [Contains Duplicate](problems/0217-contains-duplicate.md)         | Easy       | Array, Hash Table, Sorting | `O(n)`   | `O(n)` |
| 242  | [Valid Anagram](problems/0242-valid-anagram.md)                   | Easy       | String, Hash Table         | `O(n)`   | `O(n)` |
| 485  | [Max Consecutive Ones](problems/0485-max-consecutive-ones.md)     | Easy       | Array                      | `O(n)`   | `O(1)` |
| 1929 | [Concatenation of Array](problems/1929-concatenation-of-array.md) | Easy       | Array                      | `O(n)`   | `O(n)` |
