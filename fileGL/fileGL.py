import os
import os.path,time
import shutil
import datetime
from pathlib import Path


class fileGL:
    '''
    class file_manager:
            this class contains different set of methods for 
            organising the file based on different parameters
            such as name,date and file type.
            
            Also in future ,exclusive organiser for music and programming files will be added.
    '''
    
    files=[]
    organise_type="File-format"
    source_path=""
    destination_path=""
    os_platform="windows"
    types=dict()
    
    def format_available(self):
        '''
        _format_available()
        this function create a list for different types of file with the possible extension
        
        Types of files for sorting:
            music,videos,pictures,excel,pdfs,documents,archive,executable,programming,prog_others(other program files)
            
        '''
        
#         filetype_label=['music','videos','pictures','excel','pdfs','documents','slides','archive','executable','programming','prog_others']
#           file_list=[music,videos,pictures,excel,pdfs,documents,slides,archive,executable,programming,prog_others]      
        #file_type=[list of file extensions]
    
        global types
        types={
            'music':['3gp','mp3','ogg','amr'],
            'videos':['webm','mkv','flv','ogv','mp4','mpg','flv'],
            'pictures':['png','jpg','jpeg','bmp','webp','tiff','gif','sng','psd'],
            'excel':['csv','xls','xlsx','xlsv'],
           ' pdfs':['pdf','epub','chm','jdvu'],
            'documents':['txt','doc','docx','docm','rtf','odt','md'],
            'slides':['ppt','pptx','ppsm','pptm','ppsx'],
            'archive':['zip','rar','tar','7z','war'],
            'executable':['jar','exe'],
            'programming':['c','cpp','java','py','xml','json','html','css','js',
                     'php','asp','m','pl','rb','r','go','ipynb','f','jl','vh','vh'],
            'prog_others':['class','h','H','db','yaml','iml',],
        }
        
        
    
    def is_common_words(self,word):
        '''
            common_words():
                this functions creates a list of frequently used words 
                in english.For name based organising,if these words 
                present in the file name ,then they will me eliminated.
                
        '''
        
        frequent_words=('copy','of','and','a','to','in','is','your','that','it','he','was',
                      'for','on','are','as','with','there','use','an','each','which','do',
                      'how','if','will','up','other','about','out','many','some','make',
                      'like','him','into','time','look','two','more','write','go','see',
                      'number','no','way','at','be','this','have','from','or','one','had',
                      'by','word','but','not','what','all','were','when','my','than','first',
                      'been','call','who','its','now','find','long','down','day','get','come','made','may')
        
        return (word in frequent_words)
        
    def folder_manager(self,path):
        '''
        folder_manager(path):
                    this function checks for the existence of passed folder (path) 
                    if it doesnt exists ,it will create one 
                    if it exists, it will use the same
        
        '''
        if not os.path.exists(path):
            os.mkdir(path)
            
            
    def history_writer(self):
        '''
        history_writer(path=" ")
    
            To keep track of when the program has been executed ,
            this function creates/appends a history file which
            contains the files organise ,date and time ,how it is
            organised and the no of files.
            
        '''
        
        text="\n"
        global files,source_path,destination_path
        global organise_type,os_platform
        os_platform="windows"
        
        with open(os.path.join(source_path,"file_manager history.txt"),"a+") as history:
        
            text+='\n'+datetime.datetime.now().strftime("%a: %d-%m-%y  %H:%M:%S")
            text+='\n'+'Source Path: '+str(source_path)
            text+='\n'+'Destination Path: '+str(destination_path)
            text+='\n'+'No.of Files organised:'+str(len(files))
            text+='\n'+'Type: Based on-'+organise_type
            text+='\n'+'OS-platform: '+os_platform
            text+='\n----------------------------------------------------------------------------'
            text+='\n'+'\n'.join(os.listdir(source_path))
            text+='\n----------------------------------------------------------------------------'
            text+='\n----------------------------------------------------------------------------'
            history.write(text)
           # list()
    def join_path(self,file):
        '''
        join_path(file):
            joins file source_path and file name
        '''
        return source_path/file
    
    
   
        
    def list_files(self):
        '''
            list_files(path):
                This function creates the list of files in the given path.
                this function will initialize the global variable files with
                the list of files,after eliminating the folders.
                
                If the path length is less than 1 ,it will generate list with
                current directory.
        
        '''
        
        global source_path,files
        
        if len(str(source_path))<1:
            print("Warning:Please run get_path() method to initialize source & destination path.") 
            choice=input("Do you want to continue with current Directory?[Yes or No]:")
            if choice=='Yes' or choice=='yes':
                files=list(filter(os.path.isfile,os.listdir()))
            else:
                print("Exiting Program !!")
                quit()
        else:
            files=list(map(self.join_path,os.listdir(source_path)))
            files=list(map(os.path.basename,filter(os.path.isfile,files)))
        # filter function filter the list (eliminates folders) and return only files    
        
        
    def get_path(self,source=True,destination=False):
        '''
        get_path(self,source=True,destination=False):
            to get source and destination path from user
        
        '''
        global source_path,destination_path
        
        if source:
            source_path=Path(input("Please ,enter Source Path:"))
        if destination:
            destination_path=Path(input("Please,enter Destination path:"))
        else:
            destination_path=source_path
            
#     def run_preliminaries():
#         '''
#         run_preliminaries():
#               this function runs all the required functions which has to be executed before 
#               the given function executes
#         '''
        
        
    def datewise_organiser(self,history=False):
        '''
            datewise_organise():
                this function is used for organising files based on creation time.
                
                optional parameter:
                history=False :to generate the organizing history as a text file 
                
        
        '''
        global organise_type,files,source_path,destination_path
        
        organise_type="Date-wise"
        self.list_files()
        
        if history:
            self.history_writer()
       
        
        for file in files:            
           # if file.endswith(".pynb"):continue
            file_time=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(source_path,file))).strftime('%a %d-%m-%Y')
#             print(os.path.join(destination_path,file_time))
            self.folder_manager(os.path.join(destination_path,file_time))
#             print(os.path.join(source_path,file)," -",os.path.join(destination_path,file_time))
            shutil.move(os.path.join(source_path,file),os.path.join(destination_path,file_time))
        
            
    def typewise_organiser(self,history=False):
        '''
            typewise_organise():
                this function is used for organising files based on file format.
                
                optional parameter:
                history=False :to generate the organizing history as a text file 
                
        
        '''
        global organise_type,files,source_path,destination_path,types
        
        organise_type="File-format wise"
        self.list_files()
        
        if history:
            self.history_writer()
        
        
        self.format_available()
        for file in files:
            extension=file.split(".")[-1]
        # print(extension,end=" ") # to know what types of files has been moved
            for key,values in types.items():
                for value in values:
                    if extension==value:
                        self.folder_manager(os.path.join(destination_path,key))                
                        shutil.move(os.path.join(source_path,file),os.path.join(destination_path,key))
       
            
            
    def name_match(self,file,name):
        '''
            name_match(file,name):
                This function checks for the splitted user input is present in the listed 
                file name
                
        '''
        for sub_name in name.split():
            if file.find(sub_name)!=-1:
                return True
        return False
            
    def namewise_organiser(self,history=False):
        '''
            namewise_organise():
                this function is used for organising files based on name entered by the 
                user input list.
                
                optional parameter:
                history=False :to generate the organizing history as a text file 
                
        
        '''
        global organise_type,files,source_path,destination_path
        
        organise_type="Name-based on user input"
        self.list_files()
        
        if history:
            self.history_writer()
            
        
        file_names=list(input("Enter list of files names to separated by comma").split(',')) 
        for file in files:    
#             if file.endswith(".ipynb"):continue 
            flag=False
            for name in file_names:
                if file.find(name)!=-1:
                    self.folder_manager(os.path.join(destination_path,name))
                    shutil.move(os.path.join(source_path,file),os.path.join(destination_path,name))
                    flag=True
                    break
                elif self.name_match(file,name):
                    self.folder_manager(os.path.join(destination_path,name))
                    shutil.move(os.path.join(source_path,file),os.path.join(destination_path,name))
                    flag=True
                    break
        
            if not flag:
                self.folder_manager(os.path.join(destination_path,"others"))
                shutil.move(os.path.join(source_path,file),os.path.join(destination_path,"others"))
f=fileGL()
def typewise(history):
    global f
    f.typewise_organiser(history)
def namewise(history):
    global f
    f.namewise_organiser(history)
def datewise(history):
    global f
    f.datewise_organiser(history)
def working_path(src=True,dest=False):
    global f
    f.get_path(src,dest)