# Types of References in Java

In Java there are four types of references differentiated on the way by which they are garbage collected.

### Strong References

This is the default type/class of Reference Object. Any object which has an active strong reference are not eligible for garbage collection. The object is garbage collected only when the variable which was strongly referenced points to null.

```java
MyClass obj = new MyClass ();
```

### Weak References

If JVM detects an object with only weak references (i.e. no strong or soft references linked to any object object), this object will be marked for garbage collection.

```java
MyClass obj = new MyClass ();
WeakReference<MyClass> weakref = new WeakReference<MyClass>(obj); 
```

### Soft References

In Soft reference, even if the object is free for garbage collection then also its not garbage collected, until JVM is in need of memory badly. All soft references to softly-reachable objects are guaranteed to be cleared before a JVM throws an OutOfMemoryError.

```java
MyClass obj = new MyClass ();
SoftReference <MyClass> softref = new SoftReference <MyClass>(obj); 
```


### Phantom References

Phantom reference objects, which are enqueued after the collector determines that their referents may otherwise be reclaimed. Phantom references are most often used for scheduling pre-mortem cleanup actions in a more flexible way than is possible with the Java finalization mechanism.

Unlike soft and weak references, phantom references are not automatically cleared by the garbage collector as they are enqueued. 

This reference type differs from the other types defined in java.lang.ref Package because it isn't meant to be used to access the object, but as a signal that the object has already been finalized, and the garbage collector is ready to reclaim its memory.


~~~java
MyClass obj = new MyClass ();
ReferenceQueue<MyClass> refQueue = new ReferenceQueue<MyClass>(); 
PhantomReference<MyClass> phantomRef = new PhantomReference<MyClass>(obj,refQueue); 
~~~



# References

1. [Types of References in Java](https://www.geeksforgeeks.org/types-references-java/)
2. [Weak References in Java](https://www.baeldung.com/java-weak-reference)
3. [Soft References in Java](https://www.baeldung.com/java-soft-references)
4. [Phantom References in Java](https://www.baeldung.com/java-phantom-reference)
5. [Class WeakReference\<T\>](https://docs.oracle.com/javase/7/docs/api/java/lang/ref/WeakReference.html)
6. [Class SoftReference\<T\>](https://docs.oracle.com/javase/7/docs/api/java/lang/ref/SoftReference.html)
5. [Class PhantomReference\<T\>](https://docs.oracle.com/javase/7/docs/api/java/lang/ref/PhantomReference.html)
6. [Finalization and Phantom References](https://dzone.com/articles/finalization-and-phantom)