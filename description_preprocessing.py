import pandas as pd
import re


def description_preprocessing(descriptions_df : pd.DataFrame) -> list:
    descriptions_df = descriptions_df['description'].str.replace('\n', ' ')

    spaced_descriptions_list = []

    # Aşağıdaki döngü hem küçük harf yapıyor hem de newline çıkarıyor 
    # tek tek yapıp fonksiyon haline getir
    new_description = ''
    for description in descriptions_df:
        index = 0

        for char in description:
            if (char.isupper() == True and index != 0 and description[index - 1].islower() == True):
                new_description = new_description + ' ' + char
            else:
                new_description = new_description + char
            index += 1

        new_description = re.sub(r'[^\w]', ' ', new_description)
        spaced_descriptions_list.append(new_description)
        new_description = ''

    # Aşağıdaki döngü spaceleri düzgün hale getiriyor.

    spaced_arranged_description_list = []
    new_description = ''
    for description in spaced_descriptions_list:
        index = 0
        for char in description:
            if(char == ' ' and index != 0 and description[index - 1] == ' '):
                pass
            else:
                new_description += char
            index += 1
    
        new_description = new_description.lower()
        
        spaced_arranged_description_list.append(new_description)
        new_description = ''

    return spaced_arranged_description_list
    