import os


os.system("curl https://www.toyota-ct.ac.jp/ > test8.html")

f = open("test8.html",'r')

markdown = open("test.md",'w')


#print(f.read() )


markdown.write(f.read() )


markdown.close()
f.close()

os.system("git add .")

os.system("git commit -m {update}")

os.system("git push")