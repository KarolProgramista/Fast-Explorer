#Importing modules
import tkinter as tk
import os

#Setting up winodw
master = tk.Tk()

master.title = 'Fast Explorer'
master.resizable(False, False)

canvas = tk.Canvas(height=600,width=800, bg='#9ec3ff')
canvas.pack()

#Main class
class Application(object):
    def __init__(self):
        self.actualDirectory = 'c:\\'
        self.dirContent = ""
        

    def draw(self):
        MainFrame = tk.Frame(master, bg='#fff173')
        MainFrame.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.85)

        # higher frame section
        higherFrame = tk.Frame(MainFrame, bg='#42f5ad')
        higherFrame.place(relx=0.015, rely=0.02, relwidth=0.97, relheight=0.1)

        entry = tk.Entry(higherFrame)
        entry.place(relx=0, rely=0, relwidth=0.9, relheight=0.5)

        actDirLabel = tk.Label(higherFrame, text=self.actualDirectory)
        actDirLabel.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        confirmButton = tk.Button(higherFrame, text='OK', command=lambda: self.SelectOption(entry.get()))
        confirmButton.place(relx=0.9, rely=0, relwidth=0.1, relheight=0.5)

        #lower frame section
        lowerFrame = tk.Frame(master, bg='#42f5ad')
        lowerFrame.place(relx=0.063, rely=0.17, relheight=0.7, relwidth=0.875)

        contentLabel = tk.Label(lowerFrame, text=self.dirContent, anchor='nw', justify='left')
        contentLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        

    # readnig Directory content
    def readDirContent(self):
        # define dir list
        dirlist = os.listdir('.')

        
        if not len(dirlist) > 56:           
            for x in os.listdir('.'):
                # is file
                if os.path.isfile(x):
                    self.dirContent = self.dirContent + x + '\n'

                # is directory 
                elif os.path.isdir(x):
                    dirName = x + '     <DIR>'
                    self.dirContent = self.dirContent + dirName + '\n'

                # is link
                elif os.path.islink(x):
                    linkName = x + '    <LINK>'
                    self.dirContent = self.dirContent + linkName + '\n'
        else:
            # Too many files error
            self.dirContent=""
            self.dirContent=f"This folder has too many files({len(dirlist)}. Max 56. 28 per page and there are 2 pages). Some files may be missing. "
            # the same as first if
            for x in os.listdir('.'):
                if os.path.isfile(x):
                    self.dirContent = self.dirContent + x + '\n'
                    
                elif os.path.isdir(x):
                    dirName = x + '     <DIR>'
                    self.dirContent = self.dirContent + dirName + '\n'

                elif os.path.islink(x):
                    linkName = x + '    <LINK>'
                    self.dirContent = self.dirContent + linkName + '\n'
            

    # select option to do
    def SelectOption(self, answer):
        # if answer isn't none do function
        if not answer == None:

            # splitting answer
            SplitAnswer = answer.split(" ", 1)

            # cd function
            if SplitAnswer[0].lower() == 'cd':
                if os.path.isdir(SplitAnswer[1]):
                    try:
                        os.chdir(SplitAnswer[1])
                        self.dirContent=""
                        self.actualDirectory = os.getcwd()
                        self.readDirContent()
                        self.draw()
                    except PermissionError:
                        self.dirContent=""
                        self.dirContent="Access Denied"
                        self.draw()
                else:
                    self.dirContent=""
                    self.dirContent=f"There isn't folder {SplitAnswer[1]}"
                    self.draw()

                

            # type function
            elif SplitAnswer[0].lower() == 'type':
                try:
                    f = open(SplitAnswer[1])
                    self.dirContent=f.read()
                    self.draw()
                    f.close()
                except:
                    self.dirContent=f"There isn't {SplitAnswer[1]}"
                    self.draw()

            # mkdir function
            elif SplitAnswer[0].lower() == 'mkdir':
                os.mkdir(SplitAnswer[1])
                self.dirContent=""
                self.actualDirectory = os.getcwd()
                self.readDirContent()
                self.draw()


            # rmdir function
            elif SplitAnswer[0].lower() == 'rmdir':
                try:
                    os.rmdir(SplitAnswer[1])
                    self.dirContent=""
                    self.actualDirectory = os.getcwd()
                    self.readDirContent()
                    self.draw()
                except:
                    self.dirContent=f"There isn't {SplitAnswer[1]}"
                    self.draw()

            # start function(For starting programs)
            elif SplitAnswer[0].lower() == 'start':
                try:
                    os.system(SplitAnswer[1])
                    self.dirContent=""
                    self.actualDirectory = os.getcwd()
                    self.readDirContent()
                    self.draw()
                except:
                    self.dirContent=f"There isn't {SplitAnswer[1]}"
                    self.draw()     

            # clear function                   
            elif answer.lower() == 'clear':
                self.dirContent=""
                self.draw()

            # dir function
            elif answer.lower() == 'dir':
                self.dirContent=""
                self.actualDirectory = os.getcwd()
                self.readDirContent()
                self.draw()
                
            # next function(the most complicated function)
            elif answer.lower() == 'next':
                if len(os.listdir('.')) > 28:
                    self.dirContent=""
                    dirlist = os.listdir('.')
                    for i in range(0, len(dirlist)):
                        if i > 28:
                            if os.path.isfile(dirlist[i]):
                                self.dirContent = self.dirContent + dirlist[i] + '\n'
                                
                            elif os.path.isdir(dirlist[i]):
                                dirName = dirlist[i] + '     <DIR>'
                                self.dirContent = self.dirContent + dirName + '\n'

                            elif os.path.islink(dirlist[i]):
                                linkName = dirlist[i] + '    <LINK>'
                                self.dirContent = self.dirContent + linkName + '\n'
                    
                        
                            
                    self.draw()     
                            
                             
                            


                
       


# changing directory to c:\
os.chdir('c:\\')
# startig app
app = Application()
app.readDirContent()
app.draw()
# main loop
master.mainloop()
