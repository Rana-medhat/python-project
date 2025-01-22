Input=[]
output=[]
IN_width=[]
out_width=[]
out_type=[]
IN_sign=[]
out_sign=[]
clk_name=[]
rst_name=[]

keyword = ["always","end", "ifnone", "or", "rpmos", "tranif1", "and", "endcase", "initial", "output", "rtran",
    "tri", "assign", "endmodule", "inout", "parameter", "rtranif0", "tri0", "begin", "endfunction",
    "input", "pmos", "rtranif1", "tri1", "buf", "endprimitive", "integer", "posedge", "scalared",
    "triand", "bufif0", "endspecify", "join", "primitive", "small", "trior", "bufif1", "endtable",
    "large", "pull0", "specify", "trireg", "case", "endtask", "macromodule", "pull1", "specparam",
    "vectored", "casex", "event", "medium", "pullup", "strong0", "wait", "casez", "for", "module",
    "pulldown", "strong1", "wand", "cmos", "force", "nand", "rcmos", "supply0", "weak0", "deassign",
    "forever", "negedge", "real", "supply1", "weak1", "default", "for", "nmos", "realtime", "table",
    "while", "defparam", "function", "nor", "reg", "task", "wire", "disable", "highz0", "not",
    "release", "time", "wor", "edge", "highz1", "notif0", "repeat", "tran", "xnor", "else", "if",
    "notif1", "rnmos", "tranif0", "xor"]

########################## Take from user name of Design module ############################

while True:
    module_name = input("\nEnter your module name: ")
    if module_name in keyword:
        print("\nreserved keyword,please enter another name")
    elif module_name == "":
        print("\nInvalid name, please enter the module name again.")
    # Check if the first character is a letter or underscore
    elif module_name[0].isalpha() or module_name[0] == '_':
        
        # Check the rest of the characters
        for i in range(1, len(module_name)):
            if module_name[i].isalpha() or module_name[i] == '$' or module_name[i] == '_' or module_name[i].isnumeric():
                continue
            else:
                print("\nInvalid name, please enter the module name again.")
                break
        else:
            design_name = module_name + ".v"
            F=open(design_name,'w' )
            F.write("module %s (" % module_name)
            F.close()
            break  # This is only executed if the loop completes without a break
    else:
        print("\nInvalid name, please enter the module name again.")
        
testbench_name = module_name +"_TB" +".v"
T=open(testbench_name,"w")
############################# Take from user number of inputs #############################

while True:
    input_num=input('\nEnter number of input in your module without clk and rst:')
    if input_num.isnumeric():
        input_num=int(input_num)
        if input_num > 0:
            print("\nnumber of input is %d" % input_num)
            break
        else:
            print("\ninvalid number,please enter number of input again")
            continue  
    else:
        print("\ninvalid number,please enter number of inputs again")
        
########## ask user about design have clk or not and let him enter clk and rst name ########

while True:
    x=input("\nif your design need clk and rst write Y , if not write N:").upper()
    if x.isalpha() and (x == 'Y') :
        while True:
          clk_name=input("\nEnter your clock signal name:")
          if clk_name in keyword:
              print("\nreserved keyword,please enter another name")
          elif clk_name[0].isalpha() or clk_name[0] == '_':
                  
                # Check the rest of the characters
                  for i in range(1, len(clk_name)):
                      if clk_name[i].isalpha() or clk_name[i] == '$' or clk_name[i] == '_' or clk_name[i].isnumeric():
                          continue
                      else:
                          print("\nInvalid name, please enter the clock name again.")
                          break
                  else:
                      break
         
          else: 
              print("\ninvalid clock name,please enter clock name again")
              continue
        while True:
         rst_name=input("\nEnter your reset signal name:")
         if rst_name in keyword:
             print("\nreserved keyword,please enter another name")
         elif rst_name[0].isalpha() or rst_name[0] == '_':
                     
                   # Check the rest of the characters
                     for i in range(1, len(rst_name)):
                         if rst_name[i].isalpha() or rst_name[i] == '$' or rst_name[i] == '_' or rst_name[i].isnumeric():
                             continue
                         else:
                             print("\nInvalid name, please enter the reset name again.")
                             break
                     else:
                         F=open(design_name,'a');
                         F.write("\ninput %s,%s," % (clk_name,rst_name))
                         F.close()
                         break
       
         else: 
            print("\ninvalid rst name,please enter rst naame again")
            continue
        break
    elif x.isalpha() and (x == 'N'):
        print("\nyour design is combinational circuit")
        break
    else:
        print("\ninvalid choice,please write Y or N")
        continue

############################ Take inputs signals name from user ############################

while input_num != 0:
    while True:
        input_name=input("\nEnter your input signal name:")
        if input_name in keyword:
            print("\nreserved keyword,please enter another name")
        elif input_name in clk_name:
            print("\nits clock name,please enter another name")
        elif input_name in rst_name:
            print("\nits reset name,please enter another name")
        elif input_name == "":
            print("\nInvalid name, please enter the module name again.")
        elif input_name in Input:
            print("\nyou entered this name before,please enter another name")
        elif input_name[0].isalpha() or input_name[0] == '_': 
            # Check the rest of the characters
            for i in range(1, len(input_name)):
                if input_name[i].isalpha() or input_name[i] == '$' or input_name[i] == '_' or input_name[i].isnumeric():
                    continue
                else:
                    print("\nInvalid name, please enter the input signal name again.")
                    break
            else:
                Input.append(input_name)
                input_num=input_num-1
                break  # This is only executed if the loop completes without a break
        else:
            print("\nInvalid name, please enter the input signal name again.")
 
########################### Ask user input sigend or unsigned  #############################          
       
    while True:
        s=input("\nif input is signed write Y , if not write N:").upper()
        if s.isalpha() and (s == 'Y') :
            IN_sign.append("signed")
            break
        elif s.isalpha() and (s == 'N'):
            IN_sign.append("")
            break
        else:
            print("\ninvalid choice,please write Y or N")
            continue
        
 ########################### Ask user about width of input  ###############################        
        
    while True:
        w=input("\nEnter width of input signal:")
        if w.isnumeric():
            w=int(w)
            if w > 0:
                IN_width.append(w)
                break
            else:
                print("\ninvalid number,please enter width of input again")
                continue     
        else:
            print("\ninvalid number,please enter width of input again")
            continue
        
############################### write in design file #################################### 
        
    if w == 1: 
        F=open(design_name,'a')
        F.write("\ninput %s %s," % (IN_sign[-1],input_name))
        F.close()
    else:
        F=open(design_name,'a')
        F.write("\ninput %s [%d:0] %s," % (IN_sign[-1],w-1,input_name))
        F.close()
        
########################### Take number of outputs from user  ############################# 

while True:
    output_num=input('\nEnter number of output in your module :')
    if output_num.isnumeric():
        output_num=int(output_num)
        if output_num > 0:
            print("\nnumber of output is %d" % output_num)
            break
        else:
            print("\ninvalid number,please enter number of output again")
            continue  
    else:
        print("\ninvalid number,please enter number of outputs again")
        
########################### Take outputs signals name from user ############################ 

while output_num != 0:
    while True:
        output_name=input("\nEnter your output signal name:")
        if output_name in keyword:
            print("\nreserved keyword,please enter another name")
        elif output_name in clk_name:
            print("\nits clock name,please enter another name")
        elif output_name in rst_name:
            print("\nits reset name,please enter another name")
        elif output_name == "":
            print("\nInvalid name, please enter the module name again.")
        elif output_name in Input:
            print("\nyou entered this name for input signal,please enter another name")
        elif output_name in output:
            print("\nyou entered this name before,please enter another name")
        elif output_name[0].isalpha() or output_name[0] == '_': 
            # Check the rest of the characters
            for i in range(1, len(output_name)):
                if output_name[i].isalpha() or output_name[i] == '$' or output_name[i] == '_' or output_name[i].isnumeric():
                    continue
                else:
                    print("\nInvalid name, please enter the output signal name again.")
                    break
            else:
                output.append(output_name)
                output_num=output_num-1
                break  # This is only executed if the loop completes without a break
        else:
            print("\nInvalid name, please enter the output signal name again.")
 
########################## Ask user output sigend or unsigned  ############################ 
        
    while True:
        s_out=input("\nif output is signed write Y , if not write N:").upper()
        if s_out.isalpha() and (s_out == 'Y') :
            out_sign.append("signed")
            break
        elif s_out.isalpha() and (s_out == 'N'):
            out_sign.append("")
            break
        else:
            print("\ninvalid choice,please write Y or N")
            continue
 
####################### Ask user about type of output is reg or wire  ######################
    
    while True:
        t=input("\nif type of output is reg write r if not write w: ").lower()
        if t.isalpha() and (t == 'r') :
            out_type.append("reg")
            break
        elif t.isalpha() and (t == 'w'):
            out_type.append("")
            break
        else:
            print("invalid choice,please write r or w")
            continue

############################# Ask user about width of output  #############################        
    
    while True:
        w_out=input("\nEnter width of output signal:")
        if w_out.isnumeric():
            w_out=int(w_out)
            if w_out > 0:
                out_width.append(w_out)
                break
            else:
                print("\ninvalid number,please enter width of output again")
                continue     
        else:
            print("\ninvalid number,please enter width of output again")
            continue
        
################################# write in design file ##################################        
    
    if output_num != 0:
        if w_out == 1: 
            F=open(design_name,'a')
            F.write("\noutput %s %s %s," % (out_sign[-1],out_type[-1],output_name))
            F.close()
        else:
            F=open(design_name,'a')
            F.write("\noutput %s %s [%d:0] %s," % (out_sign[-1],out_type[-1],w_out-1,output_name))
            F.close() 
    elif output_num ==0:
        if w_out == 1: 
            F=open(design_name,'a')
            F.write("\noutput %s %s %s\n);" % (out_sign[-1],out_type[-1],output_name))
            F.close()
        else:
            F=open(design_name,'a')
            F.write("\noutput %s %s [%d:0] %s\n);" % (out_sign[-1],out_type[-1],w_out-1,output_name))
            F.close() 
            
######################## check module has sequential circuit or not ######################        
    
while True:
    if x == 'Y':
        y=input("\nif your design is synchronous write Y if not write N:").upper()
        if y.isalpha() and (y == 'N') :  # if true write in file always sequential block which is synchronous
            F=open(design_name,'a')
            F.write("\n\nalways @(posedge %s or negedge %s)\n   begin\n     if (!%s)\n       begin\n              // Reset condition\n       end\n     else\n       begin\n             // Non-reset condition\n       end\n   end "% (clk_name,rst_name,rst_name))
            F.close() 
            break
        elif y.isalpha() and (y == 'Y'):    # if true write in file always sequential block which is asynchronous
            F=open(design_name,'a')
            F.write("\n\nalways @(posedge %s)\n   begin\n     if (!%s)\n       begin\n             // Reset condition\n       end\n     else\n       begin\n            // Non-reset condition\n       end\n   end" % (clk_name,rst_name))
            F.close() 
            break
        else:
            print("invalid choice,please write Y or N")
            continue
    else:
        break
    
######################## Take number of combinational circuit from user ######################
        
while True:
     comp_num=input("\nEnter number of combinational always block:")
     if comp_num.isnumeric():
       comp_num=int(comp_num)
       if comp_num >= 0:
           print("\nnumber of input is %d" % comp_num)
           break
       else:
           print("\ninvalid number,please enter number of combinational always block again")
           continue  
     else:
           print("\ninvalid number,please enter number of combinational always block again")
           
if comp_num == 0:
     print("\nDesign has no combinational always block")
     F=open(design_name,'a')
     F.write("\n\n  //assign statements")
     F.close()
     
elif comp_num >0:
    while comp_num !=0:
        F=open(design_name,'a')
        F.write("\n\nalways @(*)\n   begin\n       //write combinational logic circuit\n   end")
        F.close()
        comp_num=comp_num-1
                   
################################# print endmodule ########################################

F=open(design_name,'a')
F.write("\n\nendmodule")
F.close()
                
############################## write in testbench module file ##############################

T.write("module %s_TB ();" % module_name)   # write name of testbench module  
T.close()

####################### Declare signals in testbench module file ########################

if x == 'Y':
  T=open(testbench_name,'a')
  T.write("\n  reg %s_TB,%s_TB;" % (clk_name,rst_name))
  T.close() 
for i in range(len(Input)):
    if IN_width[i] == 1: 
        T=open(testbench_name,'a')
        T.write("\n  reg %s %s_TB;" % (IN_sign[i],Input[i]))
        T.close()
    else:
        T=open(testbench_name,'a')
        T.write("\n  reg %s [%d:0] %s_TB;" % (IN_sign[i],IN_width[i]-1,Input[i]))
        T.close()

for i in range(len(output)):
    if out_width[i] == 1: 
        T=open(testbench_name,'a')
        T.write("\n  wire %s %s_TB;" % (out_sign[i],output[i]))
        T.close()
    else:
        T=open(testbench_name,'a')
        T.write("\n  wire %s [%d:0] %s_TB;" % (out_sign[i],out_width[i]-1,output[i]))
        T.close() 
           
########################### Instantiation and Signal Connection ##########################            
            
T=open(testbench_name,'a')
T.write("\n\n // instaniate design instance\n\n %s Dut (" % module_name)
T.close()
if x == 'Y':
   T=open(testbench_name,'a')
   T.write("\n   .%s(%s_TB),\n   .%s(%s_TB)," % (clk_name,clk_name,rst_name,rst_name))
   T.close()
for i in range(len(Input)):
    T=open(testbench_name,'a')
    T.write("\n   .%s(%s_TB)," % (Input[i],Input[i]))
    T.close()    
for i in range(len(output)):
    if i==len(output)-1:
        T=open(testbench_name,'a')
        T.write("\n   .%s(%s_TB)\n);" % (output[i],output[i]))
        T.close() 
    else:
        T=open(testbench_name,'a')
        T.write("\n   .%s(%s_TB)," % (output[i],output[i]))
        T.close() 
        
################################# clock Generation #####################################

if x == 'Y':
    while True:
      clk_val=input("\nEnter clock Toggle value:")
      if clk_val.isnumeric():
          clk_val=int(clk_val)
          if clk_val > 0:
              break
          else:
              print("invalid number,please enter value again")
              continue  
      else:
          print("invalid number,please enter value again")
    
    T=open(testbench_name,'a')
    T.write("\n\n // Clock Generation\n\n always \n   begin \n     #%d %s_TB = !%s_TB;\n   end" % (clk_val,clk_name,clk_name))
    T.close()
    
################################### Test cases ########################################

######################## write initial block in Testbench module ########################

T=open(testbench_name,'a')
T.write("\n\n  //Initial block\n\n  initial\n    begin"'\n       $dumpfile("{}.vcd");'.format(module_name))
T.write("\n       $dumpvars;\n\n       //initial values")
T.close()
for i in range(len(Input)): 
        T=open(testbench_name,'a')
        T.write("\n       %s_TB=%d'b0;" % (Input[i],IN_width[i]))
        T.close()
if x == 'Y':
    T=open(testbench_name,'a')
    T.write("\n       %s_TB=1'b0;" % (clk_name))
    T.write("\n       %s_TB=1'b1;" % rst_name)
    T.write('\n       $display ("TEST CASE 1") ;  // test rst signal')
    T.write("\n       #%d" % clk_val)
    T.write("\n       %s_TB=1'b0;" % rst_name)
    T.write("\n       #%d" % clk_val)
    T.write("\n       if()     //Test output from flipflop equal zero")
    T.write('\n         $display ("TEST CASE 1 IS PASSED");     // If True')
    T.write("\n       else")
    T.write('\n         $display ("TEST CASE 1 IS FAILED");     // If False')
    T.write("\n\n       //next Test cases")
    T.write("\n\n\n\n\n        #100")
    T.write("\n        $finish;")
    T.write("\n     end")
    T.write("\n endmodule")
    T.close()

else:
    T=open(testbench_name,'a')
    T.write("\n\n      //write your TestCases here\n\n\n\n\n\n        #100\n        $finish;\n     end\n endmodule")
    T.close()
    
    
