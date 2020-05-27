# Inverted Index

An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. In simple words, it is a hashmap like data structure that directs you from a word to a document or a web page.

There are two types of inverted indexes: A **record-level** inverted index contains a list of references to documents for each word. A **word-level** inverted index additionally contains the positions of each word within a document. The latter form offers more functionality, but needs more processing power and space to be created.

Suppose we want to search the texts “hello everyone, ” “this article is based on inverted index, ” “which is hashmap like data structure”. If we index by (text, word within the text), the index with location in text is:

|hello    |(1, 1)  |
|:---     | :---   |
|everyone |(1, 2)  |
|this     |(2, 1)  |
|article  |(2, 2)  |
|is       |(2, 3); (3, 2) |
|based    |(2, 4)  |
|on       |(2, 5)  |
|inverted |(2, 6)  |
|index    |(2, 7)  |
|which    |(3, 1)  |
|hashmap  |(3, 3)  |
|like     |(3, 4)  |
|data     |(3, 5)  |
|structure|(3, 6)  |


Advantage of Inverted Index are:

 - Inverted index is to allow fast full text searches, at a cost of increased processing when a document is added to the database.
 - It is easy to develop.
 - It is the most popular data structure used in document retrieval systems, used on a large scale for example in search engines.

Inverted Index also has disadvantage:

 - Large storage overhead and high maintenance costs on update, delete and insert.



# References

1. [Inverted Index](https://www.geeksforgeeks.org/inverted-index/)