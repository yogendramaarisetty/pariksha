import subprocess,os 
from subprocess import run, PIPE,STDOUT,Popen
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
compile_command = {}
run_command = {}
file_name_ext = {}
code_file_path = {}

def compile_run(language,code,custom_input,request,candidate):
    file_name = str(request.user.id)+request.user.username+str(candidate.id)
    path = os.path.join(BASE_DIR,'code_files')
    file_name_ext = {
    'C' : f'{file_name}.c',
    'C++': f'{file_name}.cpp',
    'Java': 'MyClass.java',
    'Python': f'{file_name}.python',
    'C#':f'{file_name}.cs',
    }
    code_file_path = {
    'C' : 'c_codes',
    'C++': 'cpp_codes',
    'Java': 'java_codes',
    'Python': 'python_codes',
    'C#':'csharp_codes',
    }
    compile_command = {
    'C' : f'gcc {file_name_ext[language]}',
    'C++': f'g++ {file_name_ext[language]}',
    'Java': 'javac MyClass.java',
    'Python': f'python3 {file_name_ext[language]}',
    'C#':f'mcs {file_name_ext[language]}',
    }
    run_command = {
    'C' : './a.out',
    'C++': './a.out',
    'Java': 'java MyClass',
    'Python': f'python3 {file_name_ext[language]}',
    'C#': f'mcs {file_name_ext[language]}',
    }
    #write file
    path = os.path.join(path, code_file_path[language])
    os.chdir(path)
    try:
        os.mkdir(file_name)
    except:
        pass
    path = os.path.join(path, file_name)
    os.chdir(path)
    code_file = open(file_name_ext[language],'w')
    code_file.flush()
    code_lines = code.split("\n")
    for line in code_lines:
        code_file.write(line)
    code_file.close()
    print("********\n",compile_command[language],"\n****\n",run_command[language],"\n******")
    compile_code = subprocess.Popen(compile_command[language],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    compile_errors = compile_code.stderr.readlines()
    if len(compile_errors)==0:
        run_code = subprocess.run(run_command[language], stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True,timeout=2)
        runtime_errors = run_code.stderr
        output = run_code.stdout
        if runtime_errors!="":
            return "Run Time Errors:\n"+runtime_errors
        elif output == "":
            return "Your code didn't print anything"
        return output
    else:
        errors="Compilation Errors:\n"
        for e in compile_errors:
            errors+=e.decode("utf-8")
        return errors 
