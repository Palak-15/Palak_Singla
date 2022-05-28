import numpy as np
import os
from PIL import Image
from glob import glob
import argparse

def parse_args():
    '''
        Command Line Parser
        Output: Arguments
    '''
    parser = argparse.ArgumentParser(description='To know when the Photograph has been clicked - Day or Night')
    parser.add_argument('--inputdir',required=True,help='Image input path')
    return parser.parse_args()
    
def foldercheck(args):
    '''
        Validator Function to check input 
        Input: Arguments for Input
    '''
    if not os.path.exists(args.inputdir):
        return False

    return True
    
def day_or_night(im_file):
    '''
        Function is to know when the Photograph has been clicked - 'Day' or 'Night'
        Input: Image File Path(string)
        Output: String
    '''
    try:
        if im_file.endswith('.png'):
            return 'Image is not in JPG FORMAT!!'
        im = Image.open(im_file)
        r,g,b = np.mean(np.array(im),axis=(0,1))
        return 'Day' if np.sqrt(0.299*(r**2) + 0.587*(g**2) + 0.114*(b**2)) > 73 else 'Night'
    except:
        return 'ERROR OCCURED IN {0}'.format(im_file) 

if __name__ == "__main__":
    args = parse_args()
    if not foldercheck(args):
        print('Images Folder not found!!')
        
    for i in glob(args.inputdir+'/*'):
        print(i,'=>',day_or_night(i))
    print('Thank You!')