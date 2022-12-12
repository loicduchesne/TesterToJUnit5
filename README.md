# Convert COMP250 testers to JUnit5 tester

This tool converts a .java tester (with a specified structure) file to a .java JUnit5 tester file. 

If you are interested in using JUnit5 for a COMP250 project I recommend watching tutorials.
 This tool is meant for individuals who know how to use JUnit 5.

### Requirements:
- Specific tester file structure (*see Tester file structure section*)
- Python 3.10

### Instructions:
1) Download or clone the files to a project root of your choice. Do necessary project setup if needed.
2) open *testerToJUnit5.py* in the IDE of your choice. Set the *file_name* (line 10) & *new_tester_name* (line 11).
3) After the setup, simply run testerToJUnit5.py. A file should appear in the TesterToJUnit5 directory, this file is the converted file.

*Note: **3)** Will not work if there is already a file of the same name in the working directory.*

### Tester file structure:

**IMPORTANT**: The tester file has to be in the specific format seen in A2, A3 testers
 for it convert properly. There is no verifications on if the file is in the correct format.

*Structure required for correct conversion to JUnit5*:

``` java
import *

class $test 1$ implements Runnable{

  @Override
  public void run() {
    //...
  }
}

//... 1 -> n tests

class $test n$ implements Runnable{

  @Override
  public void run() {
    //...
  }
}


public class $tester name$ {
  //...
}
```