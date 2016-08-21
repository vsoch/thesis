from bs4 import BeautifulSoup, Tag
from pokemon.skills import get_ascii
from glob import glob
import subprocess
import zipfile
import shutil
import time
import sys
import os

#####################################################################################################
# HELPER FUNCTIONS
#####################################################################################################

# Python less than version 3 must import OSError
if sys.version_info[0] < 3:
    from exceptions import OSError

def move_files(input_folder,output_folder,extensions=None):
    '''move_files will move all of one particular kind of file (eg, .css) to a particular output folder.
    '''
    if extensions == None:
        extensions = ['.png','.jpg','.gif','.jpeg']
    for root, subfolders, files in os.walk(input_folder):
        for single_file in files:
            _,ext = os.path.splitext(os.path.basename(single_file))
            if ext.lower() in extensions:
                fullpath = os.path.abspath(os.path.join(root,single_file))
                shutil.copyfile(fullpath,output_folder)                


def fix_filepath(content,tag="img",attr='src',basepath="assets/img"):
    soup = BeautifulSoup(content)
    for element in soup.findAll(tag):
        element_name = img.get(path).split('/')[-1]
        element[attr] = "%s/%s" %(basepath,element_name)
    return soup.text


def clean_content(content):
    '''clean_content will parse content from html file and (eventually) clean it up a bit
    '''
    to_replaces = ["<body>","</body>","<html>","</html>"]
    for to_replace in to_replaces:
        content = content.replace(to_replace,"")
    return content

def check_install(software="htlatex"):
    '''check_install will attempt to check if software is installed with the which command
    '''    
    cmd = ['which',software]
    install_dir = run_command(cmd,error_message="Cannot find %s. Is it installed?" %(software))
    if install_dir != None:
        print("Found %s at %s" %(software.upper(),install_dir))
        return True
    else:
        return False


def write_file(output_file,content,mode='w'):
    '''write_file will write some content to an output_file
    :param output_file: the output file to write to
    :param content: the content to write to file
    '''
    filey = open(output_file,mode)
    filey.writelines(content)
    filey.close()
    return output_file


def read_file(tex_file,mode='r'):
    '''read_file will read the tex_file and ensure is utf-8
    :param tex_file: the tex file to read
    '''
    filey = open(tex_file,mode)
    content = filey.readlines()
    filey.close()
    content = ''.join(content).decode('utf-8').encode('utf-8')
    return content


def run_command(cmd,error_message=None):
    '''run_command uses subprocess to send a command to the terminal.
    :param cmd: the command to send, should be a list for subprocess
    :param error_message: an optional error message to include
    '''
    try:
        process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        output, err = process.communicate()
    except OSError as error: 
        if error.errno == os.errno.ENOENT:
            if error_message != None:
                print(error_message)
        else:
            print(err)
        return None    
    return output


def get_markdown_template(date_str,tags="english"):
    if isinstance(tags,list):
        tags = ",".join(tags)
    return """---
           layout: post
           title: Thesis
           date: %s
           tags: %s
           category: blog
           ---
           """ %(date_str,tags)


def get_index_template(main_file):
    return """<html>
               <script>
               document.location = '%s';
               </script>
           </html>
           """ %(main_file)


#####################################################################################################
# MAIN SHABANG
#####################################################################################################

# We assume the user has uploaded a zip file with thesis from Overleaf.
# The zip should have a tex file named "main," or anything other than index.html
# index.html is the redirect page for gh-pages branch to render the site

zips = glob("*.zip")
here = os.path.dirname(os.path.realpath(__file__))

def print_error(message):
    get_ascii(name="psyduck",message=message)


if len(zips) != 0:
    get_ascii(message='Welcome to the Thesis Site Generator!')
    zip_file = zips[0]
    if not os.path.exists("site"):
        os.mkdir("site")
    with zipfile.ZipFile(zip_file,"r") as zip_ref:
        zip_ref.extractall("site")
    
    os.chdir("site")
    tex = glob("*.tex")
    if len(tex) != 0:
        tex_file = tex[0]

        # ensure all utf-8
        content = read_file(tex_file)
        write_file(tex_file,content)

        # check for htlatex
        if check_install() == True:
            print_error("Generating HTML, please wait!") 
            os.system('htlatex %s "html,index=2,next,frames"' %(tex_file))
            # Generate index.html for github pages
            output_file = tex_file.replace(".tex",".html")
            index = get_index_template("site/%s" %output_file)   
            write_file("../index.html",index)
            print("Site generation complete. Push to gh-pages for finished site.")
        else:
            print_error("Please install htlatex!")  

    else:
        print_error("Cannot find .tex file in extraction!")   
        
else:
    print_error("Cannot find zip file in %s.\n Did you download it from Overleaf?" %(os.getcwd()))   
    
