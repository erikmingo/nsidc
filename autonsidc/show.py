import os
import shutil

os.remove("nutch-site.xml")
shutil.copyfile("spine.xml", "nutch-site.xml")


def generatenutchsite(fetch, queue, mode):
    text = "<property> \n <name>fetcher.threads.fetch</name> \n <value>%s</value> \n </property> \n  <property> \n <name>fetcher.threads.per.queue</name> \n <value>%s</value> \n </property> \n <property> \n <name>fetcher.queue.mode</name> \n <value>%s</value> \n </property> \n </configuration>" % (fetch, queue, mode)

    with open("nutch-site.xml", "a") as f:
        f.write(text)


def maketimetable(fetch, que, mode):
    filename = "runtimes.txt"
    try:
        os.stat("fetch%s_que%s_mode%s" %(fetch, que, mode))
    except:
        os.mkdir("fetch%s_que%s_mode%s" %(fetch, que, mode))
    path ="fetch%s_que%s_mode%s/%s" % (fetch, que, mode, filename)

    os.remove("times.txt")
    os.system('bash time.bash')

    readfile = open("times.txt")
    line = readfile.readline()
    readfile.close()

    with open(path, "a") as f:
        f.write(line)







generatenutchsite(2, 2, "didthiswork")
maketimetable(2, 2, "byHost")











