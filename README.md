# multithreaded-hamilton-paths
This was a project completed for a class called Structured Computer Organization.

We decided to parallelize the finding of hamiltoninan paths (paths that contain each vertex exactly once) in a graph.
I wrote two different algorithms and parallelized both of them.
The multithreaded versions of the algorithms were not faster. I believe this is because of Python's GIL and the significant overhead of threads.

The recursive multithreaded algorithm is also significantly limited by the number of threads that it can produce.
