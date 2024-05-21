# Verilog Module and Testbench Generator

## Project Overview
This project aims to create a program that generates template designs and testbench Verilog modules.
By implementing this program, students will be able to automatically generate template designs and testbench modules, facilitating the development and testing of Verilog modules.

## Features

### Module Design
The program assists in generating a Verilog module template by performing the following steps:

1. **Module Naming and Initialization**
   - Prompt the user for the module name.
   - Generate a file with the module name and initialize the module design code.

2. **Input and Output Signal Configuration**
   - Request the number of input signals.
   - For each input signal:
     - Ask the user to provide a name, ensuring it is valid and not a reserved word.
     - Request width value from user and validate the width of each signal (must be greater than zero).
     - Determine if the signal is signed or unsigned.
   - Request the number of output signals and repeat the above steps for output signal names and widths.
   - Ask if each signal type is a wire or reg and determine if the signal is signed or unsigned.

3. **Template Design for Combinational and Sequential Blocks**
   - **Sequential Block:**
     - Check if a clock signal is included.
     - If a clock is present, determine if the system is synchronous or asynchronous.
     - Generate the appropriate synchronous or asynchronous always block template.
   - **Combinational Logic:**
     - Ask the user for the number of combinational always blocks.
     - Generate template code for each combinational always block.

4. **Module Finalization**
   - Conclude the module design with the `endmodule` keyword.

### Testbench Design
The program also generates a corresponding testbench for the Verilog module by following these steps:

1. **Testbench Naming**
   - Generate a testbench file with the module name appended by "TB".

2. **Signal Declaration**
   - Declare signals for inputs and outputs by appending `_tb` to input and output names in the design module.
   - Declare signals as `reg` for each input and `wire` for each output from the design module.

3. **Instantiation and Signal Connection**
   - Instantiate the design module within the testbench.
   - Connect the testbench signals to the instantiated module.

4. **Clock Generation**
   - If the design module includes a clock, prompt the user to enter the half-period value for the clock signal.
   - Write an always block template for clock generation.

5. **Initial Block to Write Test Cases**
   - Create an initial block to initialize values for input signals.
   - If the design includes a clock and reset, write a reset test case to verify functionality.

6. **Testbench Finalization**
   - Conclude the testbench module with the `endmodule` keyword.

