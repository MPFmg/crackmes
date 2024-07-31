# Sections

### File

**Stripped:** A stripped binary is one from which all or most of the debugging information and symbols have been removed.
**Not Stripped:** A non-stripped binary contains all the debugging information and symbols that were present when the binary was compiled.

### Program Trees

##### .text
- **Purpose:** This section contains the actual code (instructions) of the program
- **Properties:** It is typically read-only and executable
- **Example:** The <u>main</u> function and other functions you've defined will reside here

##### .data
- **Purpose:** This section holds initialized global and static variables
- **Properties:** It is usually both readable and writable
- **Example:** `int globalVar = 5`; will be placed in the .data section because it's a global variable with an initial value

##### .bss
- **Purpose:** This section contains unitialized global and static variables
- **Properties:** It's readable and writable. The .bss section is typically zeroed out when the program starts. 
- **Example:** `int uninitializedVar;` will be placed in the .bss section because it's a global variable without an initial value

##### .rodata
- **Purpose:** This section holds read-only data, like constants and string literals
- **Properties:** It's read-only 
- **Example:** `const char *message = "Hello, World!";` will be placed in the .rodata section because it's a constant string 

You can see where all this sections start and end in: <u>Window > Memory Map</u>

### Symbol Trees

##### Functions
- Contains all the functions <u>identified</u> in the binary
- Usage: Double-clicking a function in the symbol tree will navigate to its location in the disassembly or decompiler view. 

##### Labels
- Contains labels used within the code. Labels are typically used to mark specific points in the code, such as loops or jump targets
- Labels help to understand the flow of the program, especially in assembly code where control flow can be complex

##### Globals
- List global variables identified in the binary. These can be in sections like .data or .bss
- Global variables are crucial for understanding the state and behavior of the program. You can track how these variables are accessed and modified

##### Classes/Namespaces
- Represents classes and namespaces, especially in C++ binaries
- This helps in navigating object-oriented code, understanding class hierarchies, and analyzing methods and member variables within classes

##### Imports
- List all the functions and variables that the binary imports from external libraries. This are dynamic link libraries (DLL) on Windows or shared objects (so) on unix-like
- By examining imports, you can infer what external functionalities the binary relies on

##### Exports
- List all the functions and variables that the binary makes available to other binaries. These are the functions that other programs or libraries can call
- By examining exports, you can determine what services or functionalities the binary provides to other binaries. Also can help in identify how this binary fits in to a larger system.
