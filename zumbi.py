from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from googletrans import Translator
import time
import random
import json
import urllib.request, urllib.parse, urllib.error


class zumbi:

    def __init__(self): 
        self.driver = webdriver.Firefox(
        executable_path=r"C:/Users/Leandro/Desktop/geckodriver/geckodriver.exe"
        ) 
   
    def zumbiTradutor(self, textTranslate):
        self.textTranslate = textTranslate
        translator = Translator()
        Translate = translator.translate(textTranslate, dest='pt_br')
        return Translate.text

    def minerador(self, url): 

        self.url = url

        driver = self.driver
        driver.get(self.url) 
        # Script para scrollTo
        driver.execute_script(
            "var heightSize = document.body.offsetHeight;var bloco  = heightSize / 30;" +
            "var a = setInterval(() => {" +
            "total= bloco + 300  ;bloco = total;if(total > heightSize)" +
            "{clearInterval(a)}" +
            "window.scrollTo({top: total,behavior: 'smooth'});" +
            "}, 2000);"
            )
        time.sleep(1)

        lista = driver.find_elements_by_class_name("lister-item")
 
        contador = 0
        for nomes in lista: 

            # auto increment     
            contador += 1

            title = nomes.find_element_by_class_name("lister-item-header>a")  
            year = nomes.find_element_by_class_name("lister-item-header>span.lister-item-year")
            
            title = title.text 
            year = year.text 
            # Rating
            try:
                rating = nomes.find_element_by_class_name("ipl-rating-star__rating")
                rating = rating.text 
            except NoSuchElementException: 
                rating = 0
            # Description 
            try: 
                description = nomes.find_element_by_css_selector(".lister-item-content>p:nth-of-type(2)") 
                description = description.text 
            except NoSuchElementException: 
                description =  0
            # runtime 
            try: 
                runtime = nomes.find_element_by_css_selector(".lister-item-content>p>.runtime") 
                runtime = runtime.text 
            except NoSuchElementException: 
                runtime = 0 
            # genre 
            try: 
                genre = nomes.find_element_by_css_selector(".lister-item-content>p>.genre") 
                genre = genre.text 
            except NoSuchElementException: 
                genre = 0
            
            # certificate 
            try: 
                certificate = nomes.find_element_by_css_selector(".lister-item-content>p>.certificate") 
                certificate = certificate.text 
            except NoSuchElementException: 
                certificate = 0

            # votes 
            try: 
                votes = nomes.find_element_by_name("nv") 
                votes = votes.text 
            except NoSuchElementException: 
                votes = 0

            # gross 
            try: 
                gross = nomes.find_element_by_css_selector(".lister-item-content>p:nth-of-type(4)>span:nth-of-type(5)").get_attribute("data-value") 
            except NoSuchElementException: 
                gross = 0

            # image 
            try: 
                image = nomes.find_element_by_css_selector(".loadlate").get_attribute("src") 
            except NoSuchElementException: 
                image = 0


            # tradutor description
            description_PTbr = self.zumbiTradutor(description)
            time.sleep(1) 

            # tradutor category
            genre_PTbr = self.zumbiTradutor(genre)
            time.sleep(1)
            

            a = image.split('@')

            imageG = a[0]+ "@" +"._V1_SY1000_CR0,0,674,1000_AL_.jpg"
           
            
            minha_lista = {
                "title" : title, 
                "description" : description_PTbr,
                "certificate" : certificate,
                "year" : year, 
                "runtime" : runtime, 
                "rating" : rating,
                "genre" : genre_PTbr,
                "votes" : votes,
                "gross" : gross,
                "imageG" : imageG,
                "image" : image
                }

            # Hacker para ser trocado pela ',' dentro do json 
            with open('meu_arquivo.json', 'a') as f: 
                json.dump("~", f)

            with open('meu_arquivo.json', 'a') as f:
                json.dump(minha_lista, f)
 
           
            time.sleep(2) 

    


zangado = zumbi()
zangado.minerador("https://www.imdb.com/list/ls002448041/")