from watchdog.observers import Observer
import os
import shutil
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(default_dir):
            i = 1
            if file != 'Abhinav' and file!='desktop.ini':
                newName = file
                split_name = file.split('.')
                no_extension = os.path.splitext(default_dir + '\\' + file)       
                extension = no_extension[1]

                #Get year and month
                current_datetime = datetime.now()
                get_year = current_datetime.year
                get_year = str(get_year)
                get_month = current_datetime.month
                get_month = str(get_month)
                get_month = month_name[get_month]
                year_folder = extension_folders[extension] + '\\' + get_year 
                
                year_folder_exists = os.path.isfile(extension_folders[extension] + '\\' + get_year)
                month_folder_exists = os.path.isfile(year_folder + '\\' + get_month)
                #print(year_folder_exists)
                #print(month_folder_exists)
                try:
                    os.mkdir(os.path.join(extension_folders[extension], get_year))
                    os.mkdir(os.path.join(year_folder, get_month))
                except FileExistsError:
                    pass   
                #os.mkdir(os.path.join(year_folder, get_month))
                #print(get_year)
                

                
                #print(extension)         
                file_exists = os.path.isfile(get_month + '\\' + newName)                               
                while file_exists:
                    i+=1
                    newName = os.path.splitext(get_month + '\\' + file)[0]+ str(i) + os.path.splitext(copied_dir + '\\' + newName)[1]
                    newName = newName.split('\\')[5]
                    #print(newName)                                                                          
                    file_exists = os.path.isfile(get_month + '\\' + newName)
                month_folder = year_folder + '\\' + get_month
                #print(month_folder)
                                                                                      
                src = default_dir + '\\' + file                
                newName = month_folder + '\\' + newName
                shutil.move(src, newName)
                
#file types

extension_folders = {
    #Audio
    '.aif' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.cda' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.mid' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.midi' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.mp3' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.mpa' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.ogg' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.wav' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.wma' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.wpl' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audio",
    '.m3u' : "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Audioo",
#Text
    '.txt' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.doc' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Word",
    '.docx' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Word",
    '.odt ' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.pdf': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\PDF",
    '.rtf': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.tex': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.wks ': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.wps': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiles",
    '.wpd': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\TextFiless",
#Video
    '.3g2': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.3gp': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.avi': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.flv': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.h264': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.m4v': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.mkv': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.mov': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.mp4': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.mpg': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.mpeg': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.rm': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.swf': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.vob': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
    '.wmv': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Video",
#Images
    '.ai': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.bmp': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Imagess",
    '.gif': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.ico': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.jpg': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.jpeg': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.png': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.ps': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.psd': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.svg': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.tif': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.tiff': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
    '.CR2': "C:\\Users\\user\\Desktop\\Abhinav\\Media\\Images",
#Internet
    '.asp': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.aspx': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.cer': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.cfm': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.cgi': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.pl': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.css': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.htm': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.js': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.jsp': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.part': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.php': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.rss': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
    '.xhtml': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Internet",
#Compressed
    '.7z': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.arj': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.deb': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.pkg': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.rar': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.rpm': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.tar.gz': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.z': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
    '.zip': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Compressed",
#Disc
    '.bin': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Disc",
    '.dmg': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Disc",
    '.iso': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Disc",
    '.toast': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Disc",
    '.vcd': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Disc",
#Data
#   '.csv': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.dat': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.db': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.dbf': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.log': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.mdb': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.sav': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.sql': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.tar': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.xml': "/Users/kalle/Desktop/kalle/Programming/Database",
#    '.json': "/Users/kalle/Desktop/kalle/Programming/Database",
#Executables
    '.apk': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.bat': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.com': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.exe': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.gadget': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.jar': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
    '.wsf': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Executables",
#Fonts
    '.fnt': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Fonts",
    '.fon': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Fonts",
    '.otf': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Fonts",
    '.ttf': "C:\\Users\\user\\Desktop\\Abhinav\\Other\\Fonts",
#Presentations
    '.key': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Presentations",
    '.odp': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Presentations",
    '.pps': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Presentations",
    '.ppt': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Presentations",
    '.pptx': "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Presentations",
#Programming    
    '.class': "C:\\Users\\user\\Desktop\\Abhinav\\Programming\\Java",    
    '.py': "C:\\Users\\user\\Desktop\\Abhinav\\Programming\\Python",   
    '.html': "C:\\Users\\user\\Desktop\\Abhinav\\Programming\\HTML",
    '.js': 'C:\\Users\\user\\Desktop\\Abhinav\\Programming\\Javascript',
    '.css': 'C:\\Users\\user\\Desktop\\Abhinav\\Programming\\CSS',
#Spreadsheets
    '.ods' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Excel",
    '.xlr' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Excel",
    '.xls' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Excel",
    '.xlsx' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Microsoft\\Excel",
#System
    '.bak' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.cab' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.cfg' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.cpl' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.cur' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.dll' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.dmp' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.drv' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.icns' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.ico' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.ini' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.lnk' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.msi' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.sys' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
    '.tmp' : "C:\\Users\\user\\Desktop\\Abhinav\\Text\\Other\\System",
}
month_name = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}    







default_dir = 'C:\\Users\\user\\Desktop'
copied_dir = 'C:\\Users\\user\\Desktop\\Abhinav'     
event_handler = MyHandler() 
observer = Observer()
observer.schedule(event_handler, default_dir , recursive = True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop
observer.join()            
