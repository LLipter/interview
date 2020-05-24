# SQL Database Engine

SQL (Structured Query Language) is a language used to communicate with relational databases. The objective of SQL is to manage large amounts of data, especially if there’s lots of data being written simultaneously and too many data transactions. The data management comes into play when the SQL client communicates with a database — and thus comes the ability to create/drop/collect/store data, update or delete that data, extract that data, and manage user permissions to that data. This system is called the relational database management system.

According to Microsoft, the RDBMS processes the SQL statement by:

1. **Compiling (Parsing)**: Tokenizes the statement into individual words with valid verbiage and clauses.
2. **Compiling (Checks semantics)**: Validates the statement by checking the SQL statement against the system’s catalog and seeing it these databases, tables, and columns that the user wants exist and if the user has privileges to execute the SQL query.
3. **Compiling (Binding)**: Generates a query plan for the statement which is the binary representation of the steps required to carry out the statement. In almost all SQL server engines, it will be byte code. What has now been compiled is a command line shell — a program that reads SQL statements and now sends them to the database server for optimization and execution.
4. **Optimizing**: Optimizes the query plan and chooses the best algorithms such as for searching and sorting. This feature is called the Query Optimizer or Relational Engine. Once this is done, we now have a prepared SQL statement.
5. **Executing**: The RDBMS executes the SQL statement by running the query plan.

# MySQL 8.0 Supported Storage Engines

 - **InnoDB**: 
 	- The **default** storage engine in MySQL 8.0. 
 	- InnoDB is a **transaction-safe** (ACID compliant) storage engine for MySQL that has commit, rollback, and crash-recovery capabilities to protect user data. 
 	- InnoDB **row-level locking** (without escalation to coarser granularity locks) and Oracle-style consistent nonlocking reads increase multi-user concurrency and performance. 
 	- InnoDB stores user data in **clustered indexes** to reduce I/O for common queries based on primary keys. 
 	- To maintain data integrity, InnoDB also supports FOREIGN KEY referential-integrity constraints. 
 	- InnoDB uses the **Contention-Aware Transaction Scheduling (CATS)** algorithm to prioritize transactions that are waiting for locks. When multiple transactions are waiting for a lock on the same object, the CATS algorithm determines which transaction receives the lock first. The CATS algorithm prioritizes waiting transactions by assigning a scheduling weight, which is computed based on the number of transactions that a transaction blocks. For example, if two transactions are waiting for a lock on the same object, the transaction that blocks the most transactions is assigned a greater scheduling weight. If weights are equal, priority is given to the longest waiting transaction.
 - **MyISAM**: These tables have a small footprint. **Table-level locking** limits the performance in read/write workloads, so it is often used in read-only or read-mostly workloads in Web and data warehousing configurations.
 - **Archive**: These compact, **unindexed tables** are intended for storing and retrieving large amounts of seldom-referenced historical, archived, or security audit information.
 - **Blackhole**: The Blackhole storage engine accepts but does not store data, similar to the Unix /dev/null device. Queries always return an empty set. These tables can be used in replication configurations where DML statements are sent to slave servers, but the master server does not keep its own copy of the data.

|                               | InnoDB       |  MyISAM      |  Archive      |
| :-------------                | :----------: | :----------: | :-----------: |
| **B-tree indexes**            | Yes          | Yes          | No            |
| **Cluster database support**  | No           | No           | No            |
| **Clustered indexes**         | Yes          | No           | No            |
| **Hash indexes**              | No           | No           | No            |
| **MVCC**                      | Yes          | No           | No            |
| **Transactions**              | Yes          | No           | No            |



# References 

1. [How a SQL Database Engine Works](https://medium.com/@grepdennis/how-a-sql-database-engine-works-c67364e5cdfd)
2. [Chapter 16 Alternative Storage Engines](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html)
3. [15.1 Introduction to InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html)
4. [15.7.6 Transaction Scheduling](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-scheduling.html)
5. [16.2 The MyISAM Storage Engine](https://dev.mysql.com/doc/refman/8.0/en/myisam-storage-engine.html)
6. [16.5 The ARCHIVE Storage Engine](https://dev.mysql.com/doc/refman/8.0/en/archive-storage-engine.html)
