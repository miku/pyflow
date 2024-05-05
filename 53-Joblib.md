# Joblib

> Data-flow programming for performance

From the docs:

> **On-demand computing**: in pipeline systems such as labView or VTK, calculations are performed as needed by the outputs and only when inputs change.
> **Transparent parallelization**: a pipeline topology can be inspected to deduce which operations can be run in parallel (it is equivalent to purely functional programming).

Functions are the simplest abstraction used by everyone. Pipeline jobs (or tasks) in Joblib are made of decorated functions.

Tracking of parameters in a meaningful way requires specification of data model. Joblib gives up on that and uses hashing for performance and robustness.

## Memoization

Store expensive computation on disk.

## Parallel generator

> The core idea is to write the code to be executed as a generator expression, and convert it to parallel computing