# Java Garbage Collection

### Garbage Collectors

The garbage collection implementation lives in the JVM. Each JVM can implement garbage collection however it pleases; the only requirement is that it meets the JVM specification. Although there are many JVMs, Oracle’s **HotSpot** is by far the most common. It offers a robust and mature set of garbage collection options.


**HotSpot has four garbage collectors:**

- **Serial**: All garbage collection events are conducted serially in one thread. Compaction is executed after each garbage collection.
- **Parallel**: Multiple threads are used for minor garbage collection. A single thread is used for major garbage collection and Old Generation compaction. Alternatively, the Parallel Old variant uses multiple threads for major garbage collection and Old Generation compaction.
- **CMS (Concurrent Mark Sweep)**: Multiple threads are used for minor garbage collection using the same algorithm as Parallel. Major garbage collection is multi-threaded, like Parallel Old, but CMS runs concurrently alongside application processes to minimize “stop the world” events (i.e. when the garbage collector running stops the application). **No compaction is performed**.
- **G1 (Garbage First)**: The newest garbage collector is intended as a replacement for CMS. It is parallel and concurrent like CMS, but it works quite differently under the hood compared to the older garbage collectors

 
# Reference

1. [what-is-java-garbage-collection/](https://stackify.com/what-is-java-garbage-collection/) 