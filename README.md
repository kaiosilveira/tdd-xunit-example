ℹ️ _This repository is part of my TDD series, please refer to [kaiosilveira/test-driven-development](https://github.com/kaiosilveira/test-driven-development) for the full picture of this project_

# TDD by example - part II: The xUnit example

This repository contains my implementation of the second example presented in Kent Beck's "Test-Driven Development, by example" book.

Our goal in this example is to implement a testing framework similar to xUnit. The interesting and challenging part, though, is that we want to use our framework to test itself throughout the whole process. As Kent says in the book, "it's like performing brain surgery in yourself".

## How to navigate this repo

The code path presented in the book was implemented here using pull requests. Each pull request contains the code for a full chapter, with multiple commits. Each chapter can be seen as an implementation checkpoint until we reach the main goal. There will be a link to the merged pull request for each chapter.

When viewing a pull request, go to the "Commits" tab to see the step-by-step code until the checkpoint is reached. Each commit will have the following pattern:

- The commit title
- The implementation checklist, containing all items we need to change/fix before considering ourselves done
- An output section to show how the code was behaving at that given moment in time

The uppermost commit is the first commit made against the pull request, and the last commit in the list is the last part of the code implemented. So, to keep the chronology of changes, I'd suggest going from top to bottom when looking at the commits. There are also two buttons, "< Prev | Next >", in the Commits tab to navigate between commits. An example commit is shown below:

```
fix broken tests

Checklist:
- Invoke tearDown even if the test method fails
- Run multiple tests 👈🏼

---

Output:
➜ python3 src/test_case_test.py
5 run, 0 failed
```

Some emojis were used to hint at what's being currently done in terms of code for that specific commit. The rules for using emojis are described below:

| Emoji | Usage                                             |
| ----- | ------------------------------------------------- |
| 🎯    | identifies the list item containing the main goal |
| 👈🏼    | The list item we're currently working on          |
| ✅    | Items already finished                            |

Additionally, an auxiliary [GitHub Project](https://github.com/users/kaiosilveira/projects/6/views/1) was put in place to help me keep track of what's left.

## Goal

As mentioned, our goal is to implement a simple testing framework. The initial set of features we want to implement is listed below:

```
- Invoke test method
- Invoke setUp first
- Invoke tearDown afterward
- Invoke tearDown even if the test method fails
- Run multiple tests
- Report collected results
```

The implementation path for these features and their related pull requests and cards are listed in the table below. Hover over the links in the "Chapter" column for a quick summary of the related issue created in the project for the chapter. Hovering over the links in the "Implementation" column will show a preview of the related PR.

| Chapter                                                                                                      | Implementation                                                                                    |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| [#18](https://github.com/kaiosilveira/tdd-xunit-example/issues/3): First steps to xUnit                      | [Bootstrap the testing framework](https://github.com/kaiosilveira/tdd-xunit-example/pull/1)       |
| [#19](https://github.com/kaiosilveira/tdd-xunit-example/issues/5): Set the table                             | [Configure a setUp() method](https://github.com/kaiosilveira/tdd-xunit-example/pull/2)            |
| [#20](https://github.com/kaiosilveira/tdd-xunit-example/issues/6): Cleaning up after                         | [Implement tearDown()](https://github.com/kaiosilveira/tdd-xunit-example/pull/8)                  |
| [#21](https://github.com/kaiosilveira/tdd-xunit-example/issues/7): Counting                                  | [Report collected results](https://github.com/kaiosilveira/tdd-xunit-example/pull/9)              |
| [#22](https://github.com/kaiosilveira/tdd-xunit-example/issues/11): Dealing with failure                     | [Report failed tests](https://github.com/kaiosilveira/tdd-xunit-example/pull/10)                  |
| [#23](https://github.com/kaiosilveira/tdd-xunit-example/issues/13): How suite it is                          | [Implement TestSuite](https://github.com/kaiosilveira/tdd-xunit-example/pull/12)                  |
| [Bonus](https://github.com/kaiosilveira/tdd-xunit-example/issues/19): Handle failures at `tearDown()`        | [Handle failures at tearDown()](https://github.com/kaiosilveira/tdd-xunit-example/pull/20)        |
| [Bonus](https://github.com/kaiosilveira/tdd-xunit-example/issues/18): Invoke `tearDown()` even if test fails | [Invoke tearDown() even if test fails](https://github.com/kaiosilveira/tdd-xunit-example/pull/21) |
| [Bonus](https://github.com/kaiosilveira/tdd-xunit-example/issues/14): Create `TestSuite` from `TestCase`     | [Create TestSuite from TestCase](https://github.com/kaiosilveira/tdd-xunit-example/pull/22)       |
