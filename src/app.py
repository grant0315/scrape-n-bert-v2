import sys, getopt
import src.helpers.sys_arg_handler as sah
import src.helpers.user_input_handler as uih
import src.helpers.config_file_handler as cfh
import src.bertopic_wrapper.bert_training as bt
import src.scrapy_interface.scrapy_spider as spider

from src.helpers.cli_prompts import *


# Intro for program
def run(sys_args):
    program_intro()

    # Determine flags usage for program
    args_state = sah.handle_sys_args(sys_args)

    
    if args_state == "interactive":
        print("Running interactive")
        run_interactive()
    
    elif isinstance(args_state, dict) == True:
        print("Running with config")
        run_config(args_state["config_path"])
    
    else:
        print_no_sys_arg_state()
        
def run_interactive():
    UIH = uih.UserInputHandler() # Set first values

    if UIH.input_loop() == True: # Ensure user input is correct or change input
        scrape_and_bert(UIH.get_url(), UIH.get_css_selector(),
                        UIH.get_total_crawled_pages(), 5, UIH.get_output_directory(),
                        UIH.get_output_filename()) 
        
    BERT = bt.BertopicTraining(UIH.get_output_directory() + "/" + UIH.get_output_filename(),
                               UIH.get_output_directory(), UIH.get_output_filename())
    
    BERT.trainModel()

def run_config(path_to_config):
    # Start up config file handler, and pass in file path from sys args
    CFH = cfh.ConfigParserWrapper(path_to_config)

    # Pass info to scrape and bert
    scrape_and_bert(CFH.url, CFH.css_selectors, CFH.close_spider_page_count,
                    5, CFH.output_file_directory, CFH.output_filename)

    BERT = bt.BertopicTraining(CFH.output_file_directory + "/" + CFH.output_filename,
                             CFH.output_file_directory, CFH.output_filename)

    BERT.trainModel()

"""
Scrape and bake BABBBYYYY....
"""
def scrape_and_bert(url, css_selector, total_crawled_pages, depth_limit, out_dir, out_file):
    spider.start_scrape(url, css_selector, total_crawled_pages, depth_limit, out_dir, out_file)
