# Wiki-Decomp Dataset


[toc]

## Statistics

**Claim** is a concept or object. An **edge** connects two claims with a given property.

| Property                     | PID   | Edge Count | Claim Count |
| ---------------------------- | ----- | ---------- | ----------- |
| **Part of**                  | P361  |            |             |
| **Has part**                 | P527  |            |             |
| **Has part(s) of the class** | P2670 | 56,790     | 53,478      |

## Format and Example



## Methodology

### Data Retrieval

We use [**Linked Data Fragments**](https://linkeddatafragments.org/concept/) endpoint to extract decomposition triplets. This is a data retrieval method that queries more efficiently while minimizes server resource usage. See the [interface](https://query.wikidata.org/bigdata/ldf), [Wikidata page](https://www.wikidata.org/wiki/Wikidata:Data_access#Linked_Data_Fragments_endpoint) and [user manual](https://www.wikidata.org/wiki/Wikidata:Data_access#Linked_Data_Fragments_endpoint:~:text=.%20See%20the-,user%20manual,-and%20community%20pages) for more details.

### Data cleaning

#### Invalid Edge

We remove invalid edges that include outdated items such as:

```
wd:Q59157079  wdt:P2670  <http://www.wikidata.org/.well-known/genid/717bc97b9e7a66be2c60720d52a23f53>
```

This edge shows that second item does not have a valid ID (presented as a dead link) has label `unknown value`. 

Therefore the edge count will differ from raw edge counts from Linked Data Fragment. 

#### Invalid Claim

We also remove edges where a claim is `no label defined`, such as [Q1000322](https://www.wikidata.org/wiki/Q1000322).  

