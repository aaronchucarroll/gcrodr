# gcrodr
Recreating gcrodr in python

For the code translation - first focus on translating GCRO-DR to Python separately from the code I sent you from Stéphane.  As you develop the code in Python, you should test it using the linear system files that the Python code generates (and then compare against the iterations you get in Matlab with those same systems you converted to .mat files). Look into KryPy - it has other recycling methods (MINRES, CG, GMRES), so may provide some insight, but maybe not. Otherwise, starting from scratch may be helpful.  GCROT (an analogous method to GCRO-DR) is already in SciPy, so you can also check that out for any helpful pointers.
