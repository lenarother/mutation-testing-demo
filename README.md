# Mutation testing

## Why
- check quality of test suite
- checks quality of code
- discovery of new test cases

## How
- introduce a mutation ---> run tests ---> killed? ---> ok
- introduce a mutation ---> run tests ---> survived? ---> add tests
- introduce a mutation ---> run tests ---> survived and is not a bug -> remove / optimise code

## Automation
- [mutmut](https://mutmut.readthedocs.io/en/latest/)