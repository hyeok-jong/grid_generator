
def sanity_check(args_grids : dict):
    results = {key : type(val) == list for key, val in args_grids.items()}
    assert False not in list(results.values())
    return results

def set_baselines(python_name):
    python_name = python_name.replace('.py', '') + '.py'
    baseline = rf"""

current_time=$(date +%T)
elapsed_time=$((SECONDS - start_time))
hours=$((elapsed_time / 3600))
minutes=$(( (elapsed_time % 3600) / 60))
seconds=$((elapsed_time % 60))
current_iter=$((current_iter + 1))

echo "Current Time: $current_time"
echo "Elapsed Time: $hours hour(s) $minutes minute(s) $seconds second(s)"
echo "Progress: $current_n / $total_n"

CUDA_VISIBLE_DEVICES="0" \
python {python_name} \
"""
    return baseline

def make_one_arg(arg):
    text = rf'--{arg} "${{{arg}_i}}" '
    text += f"\ ".replace(' ', '')
    text += '\n'
    return text 

def make_arg_lines(args_grids):
    text = ''
    for i, key in enumerate(args_grids.keys()):
            text += make_one_arg(key)
    return text[:-3]

def make_for_line(arg):
    text = f'for {arg + "_i"} in "${{{arg}_s[@]}}"; do'
    text += '\n'
    return text
    

def add_space(lines : str, times = 1):
    space = '    '*times
    lines = lines.split('\n')
    lines = '\n'.join([space + l for l in lines])
    return lines

def add_vars(args_grids):
    lines = ''

    for key, val in args_grids.items():
        if type(val[0]) == str:
            val = "'" + "' '".join(val) + "'"
        else:
            val = map(str, val)
            val = " ".join(val)
        
        lines += f'{key}_s=({val})\n'
    lines += '\n'
    
    ns = [len(i) for i in args_grids.values()]
    total_n = 1
    for n in ns: total_n *= n
    
    lines += 'start_time=$SECONDS\n'
    lines += f'total_n={total_n}\n'
    lines += 'current_n=0\n\n'
    
    
    return lines




def make_sh(args_grids : dict, python_name : str = 'train', bash_name : str = 'grid_searcher.sh'):
    sanity_check(args_grids)
    bash_command = ''
    bash_name = bash_name.replace('.bash', '.sh').replace('.sh', '') + '.sh'
    bash_command += set_baselines(python_name)
    bash_command += make_arg_lines(args_grids)
    
    for arg in args_grids.keys():
        bash_command = add_space(bash_command) 
        bash_command = make_for_line(arg) + bash_command + '\ndone'
        
    bash_command = add_vars(args_grids) + bash_command
    w = open(bash_name, 'w')
    w.write(bash_command)
    w.close
    
    
    
    
    