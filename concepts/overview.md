---
description: Explore the core ideas and principles behind Superlinked's functionality..
icon: bullseye-arrow
---

# Overview

1. Describe your data using Python classes with the [@schema](../reference/common/schema/schema.md) decorator.
2. Describe your vector embeddings from building blocks with [Spaces](../reference/dsl/space/index.md).
3. Combine your embeddings into a queryable [Index](../reference/dsl/index/index.md).
4. Define your search with dynamic parameters and weights as a [Query](../reference/dsl/query/query.md).
5. Load your data using a [Source](../reference/dsl/source/index.md).
6. Define your transformations with a [Parser](../reference/common/parser) (e.g.: from [`pd.DataFrame`](../reference/common/parser/dataframe_parser.md)). 
7. Run your configuration with an [Executor](../reference/dsl/executor/in_memory/in_memory_executor.md).