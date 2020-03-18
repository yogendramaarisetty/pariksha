#Windows specific api
import subprocess,os ,time, platform
from subprocess import run, PIPE,STDOUT,Popen
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
compile_command = {}
run_command = {}
file_name_ext = {}
code_file_path = {}

def compile_run(language,code,custom_input,request,candidate):
    file_name = str(request.user.id)+request.user.username+str(candidate.id)
    path = os.path.join(BASE_DIR,'code_files')
    
    code_file_path = {
        'C' : 'c_codes',
        'C++': 'cpp_codes',
        'Java': 'java_codes',
        'Python': 'python_codes',
        'C#':'csharp_codes',
        }
    if platform.system() == 'Windows':
        file_name_ext = {
        'C' : f'{file_name}.c',
        'C++': f'{file_name}.cpp',
        'Java': 'MyClass.java',
        'Python': f'{file_name}.py',
        'C#':f'{file_name}.cs',
        }
        compile_command = {
        'C' : f'gcc {file_name_ext[language]}',
        'C++': f'g++ {file_name_ext[language]}',
        'Java': 'javac MyClass.java',
        'Python': f'py {file_name_ext[language]}',
        'C#':f'mcs {file_name_ext[language]}',
        }
        run_command = {
        'C' : 'a',
        'C++': 'a',
        'Java': 'java MyClass',
        'Python': f'py {file_name_ext[language]}',
        'C#': f'mcs {file_name_ext[language]}',
        }
    else:
         file_name_ext = {
          'C' : f'{file_name}.c',
          'C++': f'{file_name}.cpp',
          'Java': 'MyClass.java',
          'Python': f'{file_name}.python',
          'C#':f'{file_name}.cs',
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
    code_file.write(code)
    # code_lines = code.split("\n")
    # for line in code_lines:
    #     if language == "Python":
    #         line += "\n"
    #     code_file.write(line)
    code_file.close()
    start_time= 0
    end_time = 0
    # print("********\n",compile_command[language],"\n****\n",run_command[language],"\n******")
    if language == "Python":
        try:
            start_time = time.time()
            run_code = subprocess.run(run_command[language], stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=False, timeout=5)
            end_time = time.time()
            # print('Total time taken is ',end_time-start_time)
        except:
            end_time = time.time()
            return {'status': 'Timelimit exception','message':'your program exceeded the time limit','Timetaken':end_time - start_time}    
        
        runtime_errors = run_code.stderr
        output = run_code.stdout
        if runtime_errors!="":
            return { 'status': "Run Time Errors", 'error':runtime_errors}
        return {'status':"Successfully ran" , 'output' : output,'Timetaken':end_time-start_time}
    
    compile_code = subprocess.Popen(compile_command[language],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    compile_errors = compile_code.stderr.readlines()
    
    if len(compile_errors)==0:
        try:
            start_time = time.time()
            run_code = subprocess.run(run_command[language], stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=False, timeout=5)
            end_time = time.time()
            # print('Total time taken is ',end_time-start_time)
        except:
            end_time = time.time()
            return {'status': 'Timelimit exception','error':'your program exceeded the time limit','Timetaken':end_time-start_time}    
        
        runtime_errors = run_code.stderr
        output = run_code.stdout
        if runtime_errors!="":
            return { 'status': "Run Time Errors", 'error':runtime_errors,'Timetaken':end_time-start_time}
        return {'status':"Successfully ran" , 'output' : output,'Timetaken':end_time-start_time}
    else:
        errors=""
        for e in compile_errors:
            errors+=e.decode("utf-8")
        return {'status':"Compilation Errors", 'error':errors } 
