import argparse

def handle_sys_args(sys_args):
    arg_list = {}
    
    parser = argparse.ArgumentParser(prog="scrape-n-bert",
    description="bertopic ML model using scrapy")

    parser.add_argument("--config", type=str, dest='config_path', help="full path to .ini file")

    parser.add_argument("--interactive", action="store_true", dest="interactive", help="run scrape-n-bert in interactive mode")

    args = parser.parse_args()
    arg_list = vars(args)

    if arg_list["interactive"] == True:
        return "interactive"
    elif arg_list["config_path"] != None:
        print(arg_list)
        return arg_list
    else:
        print("Flag must be provided to run scrape-n-bert (--interactive or --config)")

def check_config_file():
    return True