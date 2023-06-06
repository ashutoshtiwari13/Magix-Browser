"""Utils for selenium operations"""
import re
from typing import List, Optional

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from unidecode import unidecode

"""Extract Full Content"""
def is_sentence_complete(text:str)-> bool:
    return re.search(r'[.!?]\s*$', text) is not None

def get_all_text_elements(driver : WebDriver)-> List[str]:
    """Get all the text elements on the page """
    xpath = (
        "//*[not(self::script or self::style or"
        " self::noscript)][string-length(normalize-space(text())) > 0]"        
    )
    elements = driver.find_elements(By.XPATH, xpath)

    texts = [
        elements.text.strip()
        for e in elements
        if e.text.strip() and e.is_displayed() and element_completely_viewable(driver, e)
    ]

    return texts

def find_interactable_elements(driver: WebDriver)-> List[str]:
    """Finding and parsing all interactive DOM elements on the page"""
    buttons = driver.find_elements(By.XPATH,"//button")
    links = driver.find_elements(By.XPATH,"//a")

    interactive_elements = buttons + links
    interactable_output = []
    for element in interactive_elements:
        if (
            element.is_displayed()
            and element_completely_viewable(driver, element)
            and element.is_enabled()
        ):
            element_text = element.text.strip()
            if element_text and element_text not in interactable_output:
                element_text = prettify_text(element_text, 50)
                interactable_output.append(element_text)

    return interactable_output

### Prettyfing text helper function
def prettify_text(text:str, limit: Optional[int] = None)-> str:
    """Convert to ingestable text removing whitespace and converting to lower case"""
    text = re.sub(r'\s+'," ", text)
    text = text.strip().lower()
    text = unidecode(text)
    if limit:
        text = text[:limit]
    return text

### Checking for visibility helper function
def element_completely_viewable(driver: WebDriver, elem: WebElement)-> bool:
    """Check the status of visibility of an element on the page"""
    elem_left_bound = elem.location.get("x")
    elem_upper_bound = elem.location.get("y")
    elem_right_bound = elem_left_bound
    elem_bottom_bound = elem_upper_bound

    window_upper_bound = driver.execute_script("return window.pageYOffset")
    window_left_bound = driver.execute_script("return window.pageXOffset")
    window_width = driver.execute_script("return document.documentElement.clientWidth")
    window_height = driver.execute_script("return document.documentElement.clientHeight")

    window_right_bound = window_width +window_left_bound
    window_bottom_bound = window_height + window_upper_bound

    return all(
        (
            window_left_bound <= elem_left_bound,
            window_right_bound >= elem_right_bound,
            window_upper_bound <= elem_upper_bound,
            window_bottom_bound >= elem_bottom_bound,
        )
    )    

def find_parent_element_text(elem: WebElement, prettify: bool =True)-> str:
    """Find the text upto third order parent element"""
    parent_element_text = elem.text.strip()
    if parent_element_text:
        return (
            parent_element_text if not prettify else prettify_text(parent_element_text)
        )
    
    elements = elem.find_elements(By.XPATH,"./ancestor::*[position() <= 3]")
    for parent_element in elements:
        parent_element_text = parent_element.text.strip()
        if parent_element_text:
            return (
                parent_element_text
                if not prettify
                else prettify_text(parent_element_text)
            )

    return ""

def truncate_string_from_last_occurrence(string:str, character:str)-> str:
    """Truncate a string from the last occurence of a character"""
    last_occurence_index = string.rfind(character)
    if last_occurence_index != -1:
        truncated_string = string[:last_occurence_index+1]
        return truncated_string
    else:
        string







