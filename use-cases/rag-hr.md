---
description: Learn about fundamental concepts of Superlinked.
icon: headset
---



# HR Chatbot using Retrieval Augmented Generation

Many companies aim to make HR documents more accessible to employees and contractors. A recent promising approach is building a RAG system on top of HR documents. This is because it
- provides a unique response to any query,
- reduces hallucinations as the answer has to be grounded in the retrieved context,
- makes the process highly scalable due to automatic question-answering.

However, this solution possesses its unique challenges. For example
- keeping the knowledgebase consistent and up-to-date,
- running LLMs efficiently,
- ensuring the generated results are correct and aligned with company communication guidelines,

In our case, we have three HR policy sources for our hypothetical company.
1. An older HR policy, which contains our maternity leave policy and details on manager responsibilities.
1. A more recent update, that contains inaccurate information on management responsibilities - but one that also contains unique information on paternity leave.
1. A newer policy document that contains updated information about management responsibilities, correcting the mistakes of the previous modernising attempt - alongside some other HR policy information.

A good system will be able to:
- provide relevant information on maternity leave (only covered in the old document),
- synthesize contradicting information and only present to us the correct ones

Regarding synthesizing information, there are contradictions between the documents pertaining to management responsibilities. We are going to use the 
- creation_date of the policy,
- and the usefulness score of each paragraph

as a proxy to know for similar documents with 

- similar information but different wording, and some important parts slightly altered, or
- also talking about seemingly the same topic, but without conveying useful information

which one is more relevant to our query.

### Try it out on Colab

{% embed url="https://colab.research.google.com/github/superlinked/superlinked/blob/main/notebook/rag_hr_knowledgebase.ipynb#scrollTo=e9fb5d47-d6b9-4cdd-b2b4-80dda4eef996" %}
{% endembed %}

<table data-view="cards">
<thead>
<tr><th></th><th></th><th data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref">
</th></tr>
</thead>
<tbody>
    <tr>
        <td><strong>Getting Started</strong></td>
        <td>Edit pages, collections, content, and more in GitBook.</td>
        <td></td>
        <td><a href=".gitbook/assets/content-editor.png">content-editor.png</a></td>
        <td><a href="https://colab.research.google.com/github/superlinked/superlinked/blob/main/notebook/rag_hr_knowledgebase.ipynb#scrollTo=e9fb5d47-d6b9-4cdd-b2b4-80dda4eef996">link</a></td>
    </tr>
    
</tbody>
</table>