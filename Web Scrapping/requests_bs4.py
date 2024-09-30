import requests
from bs4 import BeautifulSoup


URL = "https://classroom.google.com/c/NzA5MjMyNTM0Nzc2"

response = requests.get(URL)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract and print the title of the page
    title = soup.title.text if soup.title else "No title found"
    print(f"The title of the page is: {title}")
    
    #Find all the links
    links = soup.find_all('a')
    
    # Print the total number of links found on the page
    print(f"\nNumber of links found: {len(links)}")
    
    # Print the first few links along with their href (URL) and text content
    print("\nFirst few links:")
    for i, link in enumerate(links[:5], 1):  
        href = link.get('href', 'No href found')  # Default message if href is not found
        link_text = link.text.strip()  # Default message if text is empty
        print(f"{i}. {href} - {link_text}")
else:
    # Print an error message if the request wasn't successful
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")