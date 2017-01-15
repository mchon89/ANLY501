from bs4 import BeautifulSoup
import requests
import csv
                                                                
def parse_page(html):                                           #define parse page
    csvName="Childrenkilled.csv"                                #name the csv name based on the category of data
    soup=BeautifulSoup(html, "lxml")                            #using the BeautifulSoup 
    table=soup.findAll("table")[0]                              #using the BeautifulSoup to find the first table
    csvFile=open(csvName,"a")                                   #open csvfile and append 

    playerwriter=csv.writer(csvFile)                            
    ALL_TR=table.findAll("tr")                                  #within the table, find all tablerows
    for tr in ALL_TR:                                           #coming up with the for loop
        csvRow=[]                                               #create an empty list to write text to
        tds = tr.findAll("td")                                  #using tablerow to find all table data
        for td in tds:                                          #for loop iterating tds in all found tds using tr.findall
            if td==tds[-1]:                                     #if td reaches the last td, it is said to skip because we didnt want the last tablerow
                pass
            else:
                txt=td.find(text=True)                          #otherwise,find other td
                csvRow.append(txt)                              #append texts from tds into csvRow
        playerwriter.writerow(csvRow)                           #from csvROW, write it into csv
                
def get_page(i):                                                                              #there are multiple pages within the same cateogory of data   
    url="http://www.gunviolencearchive.org/children-killed?page="+str(i)                      #url + i where i is what we put
    response=requests.get(url)                                                                #using response get 
    html = response.text.encode('utf-8')                                                      #html is obtained through response text encode
    return html
    
def scrape_pages(first, last):                                                         #the last part
    for i in range(first,last+1):                                                      #setting up where the program web-scrapes it from to. 
        html=get_page(i)                                                               #using the definition above, html is obtained through
        parse_page(html)                                                               #parse html

scrape_pages(0,18)                                                                

