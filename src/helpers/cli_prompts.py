def program_intro():
    print("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒")
    print("SCRAPE-N-BERT")

def print_options():
    print("\n =============== OPTIONS =============== ")
    print("change [C]SS selectors, change [F]ilename, change [U]RL, change [D]irectory,")
    print("[T]otal crawled pages, [S]how current query, e[X]ecute query")
    print(" ======================================= ")

def print_no_sys_arg_state():
    print("!== No system arguments were provided ==!")
    print("!== Something is broke ==!")

def print_insufficient_resources():
    print("\n=== Out of GPU memory in order for cuda to work properly ===\n")