# Wiki-Decomp Dataset


## Statistics

**Item** is a concept or object. An **edge** connects two items with a given property.

| Property                     | PID   | Edge Count | Clean Object Count (Raw) |
| ---------------------------- | ----- | ---------- | ------------------------ |
| **Part of**                  | P361  | 4,333,243  | 3,403,293 (3,955,033)    |
| **Has part**                 | P527  | 2,061,253  | 1,690,867 (1,941,348)    |
| **Has part(s) of the class** | P2670 | 33500      | 31,826 (53,478)          |
| Total                        |       |            | 4,014,982  (4,612,728)   |

## Format and Example

The full dataset is in `data`. 

- `data/json` is the format we used in the paper and for the experiments. Here is an example:

  ```
  [
    {
      "qid": "Q1",
      "label": "Universe",
      "desc": "totality consisting of space, time, matter and energy",
      "part": [
        {
          "pid": "Q1133705",
          "plabel": "galaxy filament"
        },
        {
          "pid": "Q11379",
          "plabel": "energy"
        },
        {
          "pid": "Q133327",
          "plabel": "spacetime"
        },
        ...
      ]
    }
  ]
  ```

  It stores the concept we would like to decompose and its parts.

- `dict` stores a dictionary each line. The first QID is the key and the remaining ones make up the value. For example `Q425243 Q629 Q895` means that there is a relation `Q425243 -> Q629` and `Q425243 -> Q895`.

- `item` stores the items occurred with a property, in form of their QID.  The corresponding label for QID is in `labels.pkl`. Files that have `valid_item` in their names removed items that are outdated. 

- `triplet` stores the edges in the form of `QID1 PID QID2` which means there is a property with `PID` from an item `QID1` to the other item `QID2`


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

#### Invalid Items

We also remove edges where an item is `no label defined`, such as [Q1000322](https://www.wikidata.org/wiki/Q1000322). `SERVICE wikibase:label` returns identifier as label (`Q1000322`), which we use to filter these invalid items. 

