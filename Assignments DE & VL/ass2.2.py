import requests
from bs4 import BeautifulSoup

# Define the URL
URL = "https://classroom.google.com/c/NzA5MjMyNTM0Nzc2"

# Send a GET request to the URL
response = requests.get(URL)

# This conditional statement checks if the request was successful. HTTP status code 200 means "OK", indicating a successful request.
if response.status_code == 200: 
# If the request was successful, this line creates a BeautifulSoup object from the response content. The 'html.parser' parameter specifies the parser to use for parsing the HTML.
    soup = BeautifulSoup(response.content, 'html.parser')
    
# This line extracts the text content of the <title> tag from the parsed HTML.  
    title = soup.title.text
    print(f"The title of the page is: {title}")
    
# This prints the total number of links found on the page.
    link = soup.find_all('a')
    print(f"\nNumber of links found: {len(link)}")
    
    h1_elements = soup.find_all('h1')
    
#     print("First few H1 elements: ")
#     for i, h1 in enumerate(h1_elements[:5],1):
#         print(f"{i}.{h1}")
#         print()
#         print(f"{i},{h1.text.strip()}")
# else:
#     print(f"Failed to retrive the webpage. Status Code: {response.status_code}")



#This loop prints the first five links along with their href (URL) and text content. The enumerate() function is used to add numbering to the links, and links[:5] limits the output to the first five links.
    print("\nFirst few links:")
    for i, link in enumerate(link[:5], 1):  
        print(f"{i}. {link.get('href')} - {link.text.strip()}")
else:
#If the request wasn't successful, this block prints an error message with the status code.
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

