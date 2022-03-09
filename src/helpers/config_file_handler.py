import configparser

class ConfigParserWrapper:
    def __init__(self, config_file_path):
        # Init configparser object, and read config file provided by user
        config = configparser.ConfigParser()
        config.read(config_file_path)

        # Set class variables to passed in config file "General Settings" parameters
        self.config_file_path = config_file_path
        self.output_filename = config["General Settings"]["OUTPUT_FILE_NAME"]
        self.output_file_directory = config["General Settings"]["OUTPUT_FILE_DIRECTORY"]
        self.url = config["General Settings"]["URL"]

        # Set class variables to passed in config file "Advertools Settings" parameters
        self.follow_links = config["Advertools Settings"]["FOLLOW_lINKS"]
        self.close_spider_page_count = config["Advertools Settings"]["CLOSESPIDER_PAGECOUNT"]
        self.concurrent_requests_per_domain = config["Advertools Settings"]["CONCURRENT_REQUESTS_PER_DOMAIN"]
        self.user_agent = config["Advertools Settings"]["USER_AGENT"]
        self.css_selectors = config["Advertools Settings"]["CSS_SELECTORS"]

        # This is where bertopic imports from config would go if we had any so far

    # End goal is to have this function create a blank config file that will allow the user to fill it out themselves
    def generateBlankConfigFile(self):
        return 0