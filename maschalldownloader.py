import wget

def betterSpider():
    fileName = "" #20060923
    for year in range(2000,2007):
        fileName = str(year)    
        for month in range(1,13):
            if month < 10:
                month = '0' + str(month)
            else:
                fileName = str(month)
            for day in range(1,32):
                if day < 10:
                    day = '0' + str(day)
                else:
                    day = str(day)
                print("Attempting " +str(year)+str(month)+str(day))
                try:
                    url = 'http://www.machall.com/comics/'+str(year)+str(month)+str(day)+'.jpg'
                    dLoadFile = wget.download(url)
                except:
                    errMsg = "poop"
    print("Done")
    return 0
def main():
    betterSpider()
#    fileName = 20000000
#    for fileName in range(fileName,20060923):
#        print("Attempting " + str(fileName))
#        try:
#            url = 'http://www.machall.com/comics/'+str(fileName)+'.jpg'
#            dLoadFile = wget.download(url)
#        except:
#            errMsg = "poop"
#    print("Done")

if __name__ == "__main__":
  main()