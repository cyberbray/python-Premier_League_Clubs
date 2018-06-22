from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.eraudica.com/e/eve/search')


# Find the text input element by its name                       # <input id="query" type="search">
WebElement element = driver.findElement(By.name("query"));

# Enter something to search for
element.sendKeys("angry");

# Now submit the form. WebDriver will find the form for us from the element
element.submit();

