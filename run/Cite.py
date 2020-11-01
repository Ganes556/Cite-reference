# article parse module
from urllib.parse import urlparse
from newspaper import Article

# tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox

# dates  module
from babel.dates import format_date
from datetime import date

def autofillCite():
        
    # nyaring url menggunakan url
    urlText = urlMenu.get()
    urlParse = urlparse(urlText)

    # nyaring menggunakan Article
    article = Article(urlText)
    article.download()  
    article.parse()
    
    # auto fill
    pageTitle.set(article.title)
    websiteTitle.set(urlParse.hostname)
    urlCite.set(urlText)

    # dated access
    dateAcess = format_date(date.today(),format="long",locale="in").split(" ")
    todayDay.set(dateAcess[0])
    todayMonth.set(dateAcess[1])
    todayYear.set(dateAcess[2])

    # authors published month,day,year
    publishedDate = format_date(article.publish_date,format="long",locale="in").split(" ")
    publishedDay.set(publishedDate[0])
    publishedMonth.set(publishedDate[1])
    publishedYear.set(publishedDate[2])

    # fill author
    for x in range(len(article.authors)):
        author = article.authors[x].split(" ")
        first.set(author[0:len(author)-1])
        last.set(author[-1])
        

def manualCiteMenu(auto = False):
    refresh(size = "600x400")
    try:
        # check if click auto
        if auto:
            autofillCite()

    except Exception as e :
            messagebox.showerror("error",e)
# menu authors

    labelAuthors = Label(root,text="Authors  :",bg="brown4",fg="chocolate1",font=("arial",11,"bold"))
    labelAuthors.grid(row=0,column=0,pady=6,padx=10)

    # first name
    labelFirstName = Label(root,text="First Name : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelFirstName.grid(row=1,column=1,pady=6)

    
    entryFirst = Entry(root,bd=4,width=15,textvariable=first,fg="chocolate2",font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryFirst.grid(row=1,column=2,pady=6)

    # last name
    labelLastName = Label(root,text="Last Name : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelLastName.grid(row=1,column=3,pady=6)

    entryLast = Entry(root,bd=4,width=15,fg="chocolate2",textvariable=last,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryLast.grid(row=1,column=4,pady=6)

# menu website

    labelWebsite = Label(root,text="Website  :",bg="brown4",fg="chocolate1",font=("arial",11,"bold"))
    labelWebsite.grid(row=2,column=0,pady=10)



    # Dated Published
    # tambahkan entry lagi buat tahun,bulan. sama seperti date access
    labelPublished = Label(root,text="Published Date : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelPublished.grid(row=3,column=1,pady=6)


    entryPublishedDay = Entry(root,bd=4,width=11,fg="chocolate2",textvariable=publishedDay,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryPublishedDay.grid(row=3,column=2)

    entryPublishedMonth = Entry(root,bd=4,width=18,fg="chocolate2",textvariable=publishedMonth,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryPublishedMonth.grid(row=3,column=3)

    entryPublishedYear = Entry(root,bd=4,width=11,fg="chocolate2",textvariable=publishedYear,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryPublishedYear.grid(row=3,column=4) 
    
    

    # Page Title
    labelPageTitle = Label(root,text="Page Title         : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelPageTitle.grid(row=4,column=1,pady=6)


    entryPageTitle = Entry(root,bd=4,width=47,fg="chocolate2",textvariable=pageTitle,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryPageTitle.grid(row=4,column=2,pady=6,padx=10,columnspan=8)

    #  Website title
    labelWebsiteTitle = Label(root,text="Website Title     : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelWebsiteTitle.grid(row=5,column=1,pady=6)


    entryWebsiteTitle = Entry(root,bd=4,width=47,fg="chocolate2",textvariable=websiteTitle,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryWebsiteTitle.grid(row=5,column=2,pady=6,padx=10,columnspan=8)

    # URL 
    labelURL = Label(root,text="URL                   : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelURL.grid(row=6,column=1,pady=6)


    entryURL = Entry(root,bd=4,width=47,fg="chocolate2",textvariable=urlCite,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryURL.grid(row=6,column=2,pady=6,padx=10,columnspan=8)  

# perbaiki masukan hanya bisa sesai dengan date
# isikan placeolder di setiap datenya

    # Date access
    labelAccessDate = Label(root,text="Access Date       : ",bg="brown4",fg="chocolate1",font=("arial",10,"bold"))
    labelAccessDate.grid(row=7,column=1,pady=6)
    

    entryDay = Entry(root,bd=4,width=11,fg="chocolate2",textvariable=todayDay,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryDay.grid(row=7,column=2)

    entryMonth = Entry(root,bd=4,width=18,fg="chocolate2",textvariable=todayMonth,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryMonth.grid(row=7,column=3)

    entryYear = Entry(root,bd=4,width=11,fg="chocolate2",textvariable=todayYear,font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryYear.grid(row=7,column=4)  

    # adding placeholder if manual mode
    if not auto:
        dateEntrys = {
                        "Day" : [entryPublishedDay,entryDay],
                        "Month" : [entryPublishedMonth,entryMonth],
                        "Year" : [entryPublishedYear,entryYear]
                    }
        placeholder(**dateEntrys)
    
    # excute button
    citeButton = Button(root,text="Cite",width=10,bg="cornsilk3",activebackground="cornsilk3",command=cite) 
    citeButton.grid(row=8,column=2,columnspan=2,pady=50)

    backButton = Button(root,text=" << ",width=5,bg="cornsilk3",activebackground="cornsilk3",command=main) 
    backButton.grid(row=8,column=1,pady=50)

def cite():
    rootCite = tk.Tk()
    rootCite.title("Cite MLA")
    rootCite.resizable(False,False)

    judulArticle     = pageTitle.get()
    namaWebsite      = websiteTitle.get()
    tanggalPublished = f"{publishedDay.get()} {publishedMonth.get()} {publishedYear.get()}. "
    tanggalLihat     = f"{todayDay.get()} {todayMonth.get()} {todayYear.get()}. "
    urlLengkap       = urlCite.get()
    if tanggalPublished == tanggalLihat:
        tanggalPublished = ""
    hasilCite = f'"{judulArticle}". {namaWebsite}. {tanggalPublished}{tanggalLihat}{urlLengkap}'
    hasil = Text(rootCite, height=5, borderwidth=0)
    hasil.insert("1.0",hasilCite)
    hasil.grid(row=0,column=0)
################################ PLACEHOLDER FIELD ##############################################
def placeholder(**entrys):    
    # insert placeholder each entry
    for key,entry in entrys.items():
        for indexEntry in range(len(entry)):
            entry[indexEntry].insert(0,key)

    # delete placeholder when FocusIn
    entrys["Day"][0].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Day"][0])))
    entrys["Day"][1].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Day"][1])))

    entrys["Month"][0].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Month"][0])))
    entrys["Month"][1].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Month"][1])))
    
    entrys["Year"][0].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Year"][0])))
    entrys["Year"][1].bind("<FocusIn>",(lambda clear: clearPlaceholder(entrys["Year"][1])))
        
    
    
def clearPlaceholder(entry):
    entry.delete(0,END)


################################################################################################

def refresh(size = "650x100"):
    children = root.winfo_children()
    for i in range(len(children)):
        children[i].destroy()
    root.geometry(size)
    root.update()
    

def main():
    
    refresh()
    labelUrl = Label(root,text="URL : ",bg="brown4",fg="chocolate1",font=("arial",11,"bold"))
    labelUrl.grid(row=0,column=0,pady=6,padx=10)

    entryUrl = Entry(root,bd=4,width=70,textvariable=urlMenu,fg="chocolate2",font=("arial",10,"italic","bold"),bg="cornsilk3")
    entryUrl.grid(row=0,column=1,pady=6,padx=10,columnspan=6)

    AutoUrlButton = Button(root,text="Auto Cite",width=30,bg="cornsilk3",activebackground="cornsilk3",command= lambda: manualCiteMenu(auto=True)) 
    AutoUrlButton.grid(row=2,column=2,pady=6,padx=10,columnspan=2)

    ManualCiteButton = Button(root,text="Manualy Cite",width=30,bg="cornsilk3",activebackground="cornsilk3",command=manualCiteMenu) 
    ManualCiteButton.grid(row=2,column=4,pady=6,padx=10,columnspan=2)    

    

# main running
# if __name__ == "__main__":

# declare object and set
root = tk.Tk()   
# size
root.geometry("600x100")
root.resizable(False,False)
# background
root.config(background="brown4")

# title of pop up
root.title("Cite Website")

# variable declare
# authors name
first = StringVar()
last = StringVar()
# header website
pageTitle = StringVar()
websiteTitle = StringVar()
# Published date
publishedDay = StringVar()
publishedMonth = StringVar()
publishedYear = StringVar()
# url
urlMenu = StringVar()
urlCite = StringVar()
# dated access to website
todayDay = StringVar()
todayMonth = StringVar()
todayYear = StringVar()

# running 
main()
root.mainloop()