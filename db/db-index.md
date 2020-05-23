# Index

Indexes are **special lookup tables** that the database search engine can use to speed up data retrieval. Simply put, an index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.

An index can be used to efficiently find all rows matching some column in your query and then walk through only that **subset** of the table to find exact matches. If you don't have indexes on any column in the **WHERE** clause, the SQL server has to walk through **the whole table** and check every row to see if it matches, which may be a slow operation on big tables.

An index helps to speed up **SELECT** queries and **WHERE** clauses, but it slows down data input, with the **UPDATE** and the **INSERT** statements. Indexes can be created or dropped with no effect on the data.

Typically, an index contains keys built from one or more columns in the table or view. These keys are stored in a **B-tree** structure.

### When should indexes be created
 - A column contains a wide range of values
 - A column does not contain a large number of null values
 - One or more columns are frequently used together in a where clause or a join condition

### When should indexes be avoided

 - The table is small
 - The columns are not often used as a condition in the query
 - The column is updated frequently
 - A column contains only a few valid values (e.g. sex)

# Clustered and Non-clustered Indexes 

SQL Server has two types of indexes: clustered index and non-clustered index.

A **clustered index** stores data rows in a sorted structure based on its key values. Each table has only one clustered index because data rows can be only sorted in one order. The table that has a clustered index is called a clustered table.

A **non-clustered index** is a data structure that improves the speed of data retrieval from tables. Unlike a clustered index, a nonclustered index sorts and stores data separately from the data rows in the table. It is a copy of selected columns of data from a table with the links to the associated table.

#  Index Characteristics

### B-Tree Index - (Ordered)

 - A **B-tree index** can be used for column comparisons in expressions that use the **=**, **>**, **>=**, **<**, **<=**, or **BETWEEN** operators. The index also can be used for **LIKE** comparisons if the argument to LIKE is a constant string that does **NOT** start with a wildcard character.

### Hash Index - (Unordered)

 - They are used only for equality comparisons that use the **=** or **<=>** operators (but are very fast). They are not used for comparison operators such as **<** that find a range of values. 
 - The optimizer cannot use a hash index to speed up **ORDER BY** operations.
 - MySQL cannot determine approximately how many rows there are between two values (this is used by the range optimizer to decide which index to use)
 - Only whole keys can be used to search for a row. (With a B-tree index, any leftmost prefix of the key can be used to find rows.)



# How MySQL Uses Indexes

MySQL uses indexes for these operations:

 - To find the rows matching a WHERE clause quickly.
 - To eliminate rows from consideration. If there is a choice between multiple indexes, MySQL normally uses the index that finds the smallest number of rows (**the most selective index**).
 - If the table has a multiple-column index, any **leftmost prefix** of the index can be used by the optimizer to look up rows. For example, if you have a three-column index on (col1, col2, col3), you have indexed search capabilities on (col1), (col1, col2), and (col1, col2, col3).
 - Any index that does not span **all** **AND** levels in the **WHERE** clause is not used to optimize the query. In other words, to be able to use an index, a prefix of the index must be used in every **AND** group.

The following WHERE clauses use indexes:

~~~sql
... WHERE index_part1=1 AND index_part2=2 AND other_column=3

    /* index = 1 OR index = 2 */
... WHERE index=1 OR A=10 AND index=2

    /* optimized like "index_part1='hello'" */
... WHERE index_part1='hello' AND index_part3=5

    /* Can use index on index1 but not on index2 or index3 */
... WHERE index1=1 AND index2=2 OR index1=3 AND index3=3;
~~~

These WHERE clauses do not use indexes:

~~~sql
    /* index_part1 is not used */
... WHERE index_part2=1 AND index_part3=2

    /*  Index is not used in both parts of the WHERE clause  */
... WHERE index=1 OR A=10

    /* No index spans all rows  */
... WHERE index_part1=1 OR index_part2=10
~~~

Sometimes MySQL does not use an index, even if one is available. One circumstance under which this occurs is when the optimizer estimates that using the index would require MySQL to access a very large percentage of the rows in the table. (In this case, a table scan is likely to be much faster because it requires fewer seeks.) However, if such a query uses LIMIT to retrieve only some of the rows, MySQL uses an index anyway, because it can much more quickly find the few rows to return in the result.

# References

1. [SQL - Indexes](https://www.tutorialspoint.com/sql/sql-indexes.htm)
2. [SQL indexes](https://www.geeksforgeeks.org/sql-indexes/)
3. [What is an index in SQL?](https://stackoverflow.com/questions/2955459/what-is-an-index-in-sql)
4. [SQL Server Clustered Indexes](https://www.sqlservertutorial.net/sql-server-indexes/sql-server-clustered-indexes/)
5. [SQL Server non-clustered indexes](https://www.sqlservertutorial.net/sql-server-indexes/sql-server-create-index/)
6. [Clustered and Nonclustered Indexes Described](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver15)
7. [8.3.1 How MySQL Uses Indexes](https://dev.mysql.com/doc/refman/8.0/en/mysql-indexes.html)
8. [8.3.6 Multiple-Column Indexes](https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html)
9. [8.3.9 Comparison of B-Tree and Hash Indexes](https://dev.mysql.com/doc/refman/8.0/en/index-btree-hash.html)