import subprocess,os 
from subprocess import run, PIPE,STDOUT,Popen
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def compile_run(language,code,custom_input,request,candidate):
    print(BASE_DIR)
    print("#####################3")
    output=""
    file_name = str(request.user.id)+request.user.username+str(candidate.id)
    p = BASE_DIR
    path = os.path.join(p,"code_files")
    if language == "Python":
        output = execute_python(code,custom_input,file_name,path)
    elif language == "Java":
        output = execute_java(code,custom_input,file_name,path)
    elif language == "C":
        output = execute_c(code,custom_input,file_name,path)
    elif language == "C++":
        output = execute_cpp(code,custom_input,file_name,path)
    elif language == "C#":
        output = execute_csharp(code,custom_input,file_name,path)
    return output

def execute_python(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'python_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
   
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".python"
    # return file_name_ext
    # return os.getcwd()
    code_file = open(file_name_ext,'w')
    
    code_file.flush()
    code_file.write(code)
    code_file.close()
    
    cmd = f'python {file_name_ext}'
    p=os.getcwd()
    run_code = subprocess.run(cmd, stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
    errors = run_code.stderr
    if len(errors)==0:
        os.chdir(root_path)
        
        if run_code.stdout == "":
            return "Your code didn't print anything."
        return run_code.stdout
    else:
        os.chdir(root_path)
        return errors   

def execute_java(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'java_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= "MyClass.java"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l)
    code_file.close()
    cmd = f'javac {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    cmd='java MyClass'
    if len(errors)==0:
        run_code = subprocess.run(cmd, stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True,timeout=10)
        os.chdir(root_path)
        if run_code.stderr!="":
            return run_code.stderr
        elif run_code.stdout == "":
            return "Your code didn't print anything."
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error 


def execute_c(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'c_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".c"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l)
    code_file.close()
    cmd = f'gcc {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        run_code = subprocess.run("./a.out", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
        os.chdir(root_path)
        if run_code.stderr!="":
            return run_code.stderr
        elif run_code.stdout == "":
            return "Your code didn't print anything."
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error   

def execute_cpp(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'cpp_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".cpp"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'g++ {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        try:
            run_code = subprocess.run("./a.out", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
            os.chdir(root_path)
        except:
            os.chdir(root_path)
        finally:
            os.chdir(root_path)
        if run_code.stderr!="":
            return run_code.stderr
        if run_code.stdout == "":
            return "Your code didn't print anything."
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error 

def execute_csharp(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'csharp_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".cs"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'mcs {file_name_ext}'
    p = os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
    errors =""
    for i in compile_code.stderr:
        errors+=i.decode('utf-8')
    if len(errors) == 0:
        cmd="mono "+file_name+".exe"
        run_code = subprocess.run(cmd, stdout=PIPE,input=custom_input,encoding='ascii',shell=True)
        os.chdir(root_path)
        if run_code.stdout == "":
            return "Your code didn't print anything."
        return run_code.stdout
    else:
        return errors 
