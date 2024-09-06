---
# description: >-
icon: eyes
---

# Why Superlinked?


#### Your users now expect that your search can handle complex queries

![Complex queries](../.gitbook/assets/why-superlinked-image.png)

{% hint style="info" %}
Vector Search with text-only embeddings (& also multi-modal) fails on complex queries, because complex queries are never just about text. They involve other data too!
{% endhint %}

![Example of queries needing other data than text](../.gitbook/assets/why-superlinked-image1.png)

#### With text-only embeddings, you have to handle text separately from your other data and/or use *slow*, *low quality* & *high cost* workarounds

<details>
    <summary>Metadata filters</summary>
    When you convert a fuzzy preference like “recent”, “risky” or “popular” into a filter, you model a sigmoid with a binary step function = not enough resolution.
</details>

<details>
    <summary>Candidate re-ranking</summary>
    Semantic ranking & ColBERT only use text, learn2rank models need ML Engineers.
    Broad queries eg “popular pants” can’t be handled by re-ranking at all, due to poor candidate recall.
</details>

<details>
<summary>Stringify & vectorize</summary>
It’s extremely noisy to stringify & text-embed whole objects like users, SKUs or content+metadata. See below for `cosine(textembed(str(50)),textembed(str(1..100))):`
</details>

![Comparing current methods of combining text-only embeddings to other data](../.gitbook/assets/why-superlinked-image2.png)