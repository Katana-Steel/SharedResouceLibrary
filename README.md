### the Shared Resource Dynamic Library 

written by Rene Kjellerup (c) 2018
this project is released under GNU's GPL version 3 or later at your
option.

---
this project was created to compile .rc resouce files typically found
in windows projects where the operating system provides the mechanism
to fetch text stored in a DLL an present it to an Application.

---
to build and run:

```
mkdir build
cd build
cmake ..
make
ctest -V
```