# from bs4 import BeautifulSoup
# import requests
# import time
# import os

# print('Enter the minimum price of earbuds:')
# earbudsprice = input('=>')
# print('Enter the minimum rating from the customer:')
# earbudsreview = input('=>')



# html_text = requests.get('https://www.flipkart.com/search?q=boat%20earpods&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text
# soup = BeautifulSoup(html_text,'lxml')
# maintags = soup.find_all('div', class_ = '_4ddWXP')
# for maintag in maintags :
    
#     price = maintag.find('div',class_ = '_30jeq3').text
#     if price >= earbudsprice :
#         name = maintag.find('a',class_ = 's1Q9rs').text
#         rating = maintag.find('div',class_ = '_3LWZlK').text
       
#         if rating >= earbudsreview :
#             print(name)
#             print(price)
#             print(rating)




from bs4 import BeautifulSoup
import requests
import time
import os

print('Enter the minimum price of earbuds:')
earbudsprice = float(input('=>'))
print('Enter the minimum rating from the customer:')
earbudsreview = float(input('=>'))

html_text = requests.get('https://www.flipkart.com/search?q=boat%20earpods&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text
soup = BeautifulSoup(html_text, 'lxml')
maintags = soup.find_all('div', class_='_4ddWXP')

output_file = 'merged_output.txt'

with open(output_file, 'a', encoding='utf-8') as f:
    for index, maintag in enumerate(maintags):
        price_text = maintag.find('div', class_='_30jeq3').text
        price = float(price_text.replace('₹', '').replace(',', ''))
        if price >= earbudsprice:
            name = maintag.find('a', class_='s1Q9rs').text
            rating_element = maintag.find('div', class_='_3LWZlK')

            if rating_element is not None:
                rating = float(rating_element.text)
                if rating >= earbudsreview:
                    f.write(f"Earpods Name: {name}\n")
                    f.write(f"Earpods Price: ₹{price_text}\n")
                    f.write(f"Earpods Rating: {rating}\n")
                    f.write('\n')

print(f'Output merged into file: {output_file}')
