# TDD by example - part II: The xUnit example

This repository contains my implementation of the second example presented in "Test-Driven Development, by exmaple" (Beck, Kent).

## How to navigate this repo

The code path presented in the book was implemented here using pull requests. Each pull request contains the code for a full chapter, with multiple commits. Each chapter can be seen as an implementation checkpoint until we reach the main goal. There will be a link to the merged pull request for each chapter.

When viewing a pull request, go to the "Commits" tab to see the step-by-step code until the checkpoint is reached. Each commit will have the following pattern:

The commit title
The checklist for the implementation, containing all items we need to change/fix before considering ourselves done
The uppermost commit is the first commit made against the pull request, and the last commit in the list is the last part of the code implemented. So, to keep the chronology of changes, I'd suggest going from top to bottom when looking at the commits. There are also two buttons, "< Prev | Next >", in the Commits tab to navigate between commits.

## Initial list

```
Invoke test method
Invoke setUp first
Invoke tearDown afterward
Invoke tearDown even if the test method fails
Run multiple tests
Report collected results
```
