#   Usage: post_gen.py <post title> 


import time
from datetime import date
import sys

debug = "FALSE"
post_dir = "../_posts/"
file_type = ".markdown"
post_title = ""
post_fileTitle = ""

#def write_template(post_newfile):
def write_template(post_file):
    std_template = ("---\n"                         + \
            "layout: post\n"                        + \
            "title: \"%s\"\n" % (post_title)        + \
            "date: %s\n"                            + \
            "categories: general\n"                 + \
            "---\n") % (time.strftime("%Y-%m-%d %H:%M:%S %z"))
    if (debug is "TRUE"): print std_template
    post_file.write(std_template);

def run():
    post_str = post_dir + str(date.today()) + "-" + post_fileTitle + file_type;

    if (debug is "TRUE"): print post_str; 
    
    post_file = open(post_str,'w');
    write_template(post_file);
    post_file.close();

if (__name__ == "__main__"):
    post_title = ' '.join(sys.argv[1:]);
    post_fileTitle =  '-'.join(sys.argv[1:]); 
    run();
