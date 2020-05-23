# Transaction Isolation Levels

Isolation levels define the degree to which a transaction must be isolated from the data modifications made by any other transaction in the database system. A transaction isolation level is defined by the following phenomena: 

 - **Dirty Read**: A Dirty read is the situation when a transaction reads a data that has not yet been committed. For example, Let’s say transaction 1 updates a row and leaves it uncommitted, meanwhile, Transaction 2 reads the updated row. If transaction 1 rolls back the change, transaction 2 will have read data that is considered never to have existed.
 - **Non Repeatable read**: Non Repeatable read occurs when a transaction reads same row twice, and get a different value each time. For example, suppose transaction T1 reads data. Due to concurrency, another transaction T2 updates the same data and commit, Now if transaction T1 rereads the same data, it will retrieve a different value.
 - **Phantom Read**: Phantom Read occurs when two same queries are executed, but the rows retrieved by the two, are different. For example, suppose transaction T1 retrieves a set of rows that satisfy some search criteria. Now, Transaction T2 generates some new rows that match the search criteria for transaction T1. If transaction T1 re-executes the statement that reads the rows, it gets a different set of rows this time.


Based on these phenomena, The SQL standard defines four isolation levels: 

1. **Read Uncommitted**: Read Uncommitted is the lowest isolation level. In this level, one transaction may read not yet committed changes made by other transaction, thereby allowing dirty reads. In this level, transactions are not isolated from each other.
2. **Read Committed**: This isolation level guarantees that any data read is committed at the moment it is read. Thus it does not allows dirty read. The transaction holds a **read or write lock** on the current row and will be released **at the end of each statement** (instead of until the end of the transaction), and thus prevent other transactions from reading, updating or deleting it.
3. **Repeatable Read** (MySQL default setting): The transaction holds **read locks** on all rows it references and **writes locks** on all rows it inserts, updates, or deletes **until the transaction completes**. Since other transaction cannot read, update or delete these rows, consequently it avoids non-repeatable read.
4. **Serializable**: This is the Highest isolation level. A serializable execution is guaranteed to be serializable. Serializable execution is defined to be an execution of operations in which concurrently executing transactions appears to be serially executing. **Range locks** are placed in the range of key values that match the search conditions of each statement executed in a transaction **until the transaction completes**. This blocks other transactions from updating or inserting any rows that would qualify for any of the statements executed by the current transaction. This means that if any of the statements in a transaction are executed a second time, they will read the same set of rows. The range locks are held until the transaction completes.

The Table is given below clearly depicts the relationship between isolation levels, read phenomena and locks:

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/transactnLevel.png)


# References

1. [Transaction Isolation Levels in DBMS](https://www.geeksforgeeks.org/transaction-isolation-levels-dbms/)
2. [SET TRANSACTION ISOLATION LEVEL](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-ver15)