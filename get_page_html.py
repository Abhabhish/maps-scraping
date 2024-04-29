import requests

url = "https://www.google.com/maps/contrib/111915360222789391471/photos/@28.1924513,76.854799,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPwGnDyV7a7XX9-uQsGFQu4JCIo8s9E9n-0YhKD!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPwGnDyV7a7XX9-uQsGFQu4JCIo8s9E9n-0YhKD%3Dw365-h830-k-no!7i2032!8i4624!4m3!8m2!3m1!1e1"

# Make a request to the URL
response = requests.get(url)

# Save the HTML code in a file
with open("page.html", "wb") as file:
    file.write(response.content)
