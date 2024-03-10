# Amazon-Scrapper
This is an automated Amazon Scrapper that scraps Amazon from user defined queries and stores the output as {user-query}.json files in output directory.

Design Decisions:
1.	Separation of Concerns: The codebase is divided into multiple modules to separate different concerns. The scraper.py module handles the scraping logic, the product.py module defines the Product class to model product data, and the data_saver.py module contains functionality to save extracted data into JSON files. This separation enhances code readability, maintainability, and reusability.
2.	Error Handling: Error handling is implemented in critical sections of the code, such as file operations and JSON decoding. Specific exceptions like OSError and JSONDecodeError are caught individually to provide meaningful error messages to the user. Additionally, a generic Exception block is used to catch any unexpected errors.
3.	Modularity: Each module encapsulates specific functionality, making it easier to understand and modify. The scraper.py module focuses on scraping data from Amazon, the product.py module defines the Product class, and the data_saver.py module handles data saving operations.
4.	Configuration: The scraper.py module allows customization of user agents, proxies, and headers to enhance scraping reliability and prevent blocking by websites. These configurations can be easily adjusted based on specific requirements.
Dependencies:
•	Python 3.x
•	Requests library for HTTP requests
•	BeautifulSoup library for web scraping
•	query_reader.py for reading input queries (Assumed to be provided)

How to Run the Scraper:
•	Ensure Python 3.x is installed on your system.
•	Create a Virtual Environment.
•	Install the required dependencies using pip:
pip install “requirements.txt”
•	Place the query_reader.py file in the input_file directory (assuming it's provided).
•	Execute the main.py file to start the scraping process
•	Follow the prompts to enter the input file path containing the queries.
•	The scraper will start fetching data from Amazon based on the provided queries and save the extracted data into separate JSON files.
Note: Make sure to adjust any configurations or file paths as needed based on your specific environment and requirements.
