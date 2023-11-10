import os

for i in os.listdir("./src"):                                                               # compile
    print("nasm -fmacho src/" + str(i) + " -o build/" + str(i).replace(".asm", ".o"))       # .asm
    os.system("nasm -fmacho src/" + str(i) + " -o build/" + str(i).replace(".asm", ".o"))   # files
print()                                                                                     

compile_objects_command = "ld -macosx_version_min 10.8 -arch x86_64 -o build/main"            # 
for i in os.listdir("./build"):                         # Linking
    if i[-2] == "." and i[-1] == "o":                   #   all
        compile_objects_command += "  build/"+ str(i)   # .o files
print(compile_objects_command)                          # 
os.system(compile_objects_command)                      # 


# Run final main file