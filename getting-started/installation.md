---
# description: >-
icon: display
---

# Installation

### In a notebook
Install the superlinked library:

```python
%pip install superlinked
```


### As a script
Ensure your python version is at least `3.10.x` but not newer than `3.12.x`.

```bash
$> python -V
Python 3.10.9
```

If your python version is not `>=3.10` and `<=3.12` you might use [pyenv](https://github.com/pyenv/pyenv) to install it.

Upgrade pip and install the superlinked library.

```bash
$> python -m pip install --upgrade pip
$> python -m pip install superlinked
```

### Run the example

{% hint style="info" %}
First run will take slightly longer as it has to download the embedding model.
{% endhint %}


```python   
from superlinked.framework.common.schema.schema import schema
from superlinked.framework.common.schema.schema_object import String
from superlinked.framework.common.schema.id_schema_object import IdField
from superlinked.framework.dsl.space.text_similarity_space import TextSimilaritySpace
from superlinked.framework.dsl.index.index import Index
from superlinked.framework.dsl.query.param import Param
from superlinked.framework.dsl.query.query import Query
from superlinked.framework.dsl.source.in_memory_source import InMemorySource
from superlinked.framework.dsl.executor.in_memory.in_memory_executor import InMemoryExecutor


@schema # Describe your schemas.
class Document:
    id: IdField  # Each schema should have exactly one `IdField`.
    body: String # Use `String` for text fields.

document = Document()

relevance_space = TextSimilaritySpace(text=document.body, model="sentence-transformers/all-mpnet-base-v2") # Select your semantic embedding model.
document_index = Index([relevance_space]) # Combine your spaces to a queryable index.

query = Query(document_index).find(document).similar(relevance_space.text, Param("query_text")) # Define your query with dynamic parameters.

source: InMemorySource = InMemorySource(document) # Connect a data source to your schema.

executor = InMemoryExecutor(sources=[source], indices=[document_index]) # Tie it all together to run your configuration.
app = executor.run()

source.put([{"id": "happy_dog", "body": "That is a happy dog"}])
source.put([{"id": "happy_person", "body": "That is a very happy person"}])
source.put([{"id": "sunny_day", "body": "Today is a sunny day"}])

print(app.query(query, query_text="Who is a positive friend?")) # Run your query.
```