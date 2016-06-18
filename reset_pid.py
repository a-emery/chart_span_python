def user_task():
    print("""Commands:
PROCESS: process from current pid
RESET + new pid (ex. RESET 12345): set a new current pid
CURRENT: view current pid
QUIT: exit task
HELP: view commands
""")
    while True:
        task = raw_input("> ")
        if task == "PROCESS":
            process()
            continue
        if task[:5] == "RESET":
            reset(task[6:])
            continue
        if task == "CURRENT":
            current()
            continue
        if task == "QUIT":
            break
        if task == "HELP":
            user_task()
            break
        else:
            print('Invalid command, self-destruct')
            break
            
def process():
    pids = open('pids.txt', 'r').read().split('\n')
    current_pid = open('current_pid.txt', 'r').read()
    if current_pid not in pids:
        new_current_pid = raw_input('Sorry, the current pid is not in the list of pids. Please pick a new current pid: ')
        reset(new_current_pid)
    else:
        active_pids = []
        for pid in pids:
            if pid >= current_pid:
                active_pids.append(pid)
        active_pids.sort()
        for pid in active_pids:
            print('Processing pid: ' + pid)
            open('current_pid.txt', 'w').write(pid)


    
def reset(new_pid):
    open('current_pid.txt', 'w').write(new_pid)
    print('New current pid is: ' + new_pid)
    
def current():
    current_pid = open('current_pid.txt', 'r').read()
    print('The current pid is: ' + current_pid)
    

user_task()
