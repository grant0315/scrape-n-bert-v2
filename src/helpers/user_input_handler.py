import src.helpers.cli_prompts as cp
import src.helpers.common as com

class UserInputHandler():
    def __init__(self):
        self.set_url()
        self.set_css_selector()
        self.set_total_crawled_pages()
        self.set_output_directory()
        self.set_output_filename()

    """
    Main loop for interactive mode input. Function returns True when
    user type "X" for execute.
    """
    def input_loop(self):
        while True:
            cp.print_options() # Print available options to user

            # Get user input and pass if block
            user_in = input("Choice: ")
            print("")

            if user_in == "F":
                self.set_output_filename()
            
            elif user_in == "U":
                self.set_url()
            
            elif user_in == "C":
                self.set_css_selector()

            elif user_in == "D":
                self.set_output_directory()

            elif user_in == "T":
                self.set_total_crawled_pages()
            
            elif user_in == "S":
                self.print_user_input()
            
            elif user_in == "X":
                return True

            elif user_in == "Q":
                break

            else:
                print("Please enter a option shown above")
        
    def print_user_input(self):
        print("\n")
        print("URL: " + self.url)
        print("CSS Selector: " + self.css_selector)
        print("Total crawled pages: " + self.total_crawled_pages)
        print("Output Directory: " + self.output_directory)
        print("Output Filename: " + self.output_filename)

    # Getters and setters
    def set_url(self):
        while True: 
            user_in = input("\nURL: ")

            if com.check_if_url_is_accessible(user_in) == True:
                self.url = user_in
                break
            
            else:
                print("\nPlease input a valid URL: ")

    def set_css_selector(self):
        self.css_selector = input("CSS selector: ")

    def set_total_crawled_pages(self):
        self.total_crawled_pages = input("Total crawled pages: ")
    
    def set_output_directory(self):
        "If being ran in docker, set directory to: ./data"
        self.output_directory = input("Output directory (must already exist): ")
        
        if com.check_if_directory_exists(self.output_directory) == False:
            print("!== Must use a directory that already exists ==!")
            self.set_output_directory()

    def set_output_filename(self):
        self.output_filename = input("Output filename: ")

    def get_url(self):
        return self.url
    
    def get_css_selector(self):
        return self.css_selector

    def get_total_crawled_pages(self):
        return self.total_crawled_pages

    def get_output_directory(self):
        return self.output_directory

    def get_output_filename(self):
        return self.output_filename