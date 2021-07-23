import os

import parse_text_grid
#from parse_text_grid import *

def get_alignment(data_path,dictonary_path,acoustic_model_path,output_path):
    if not os.path.isdir(data_path):
        print("data path does not exist!")
        return False
    try:
        if os.path.exists(output_path):
            os.system('rm -rf {}'.format(output_path))
        cmds = "mfa align /home/hp/PycharmProjects/align/data /home/hp/PycharmProjects/align/models/english.dict /home/hp/PycharmProjects/align/models/english.zip /home/hp/PycharmProjects/align/out --clean".format(
            data_path,
            dictionary_path,
            acoustic_model_path,
            output_path)
        os.system(cmds)
    except Exception as e:
        print("Exception error occurred!")
        return False
    return True

# def text_grid(grid_filepath):
#     with open(grid_filepath,"rb") as f:
#         text=f.readlines()
#     return text
#

segments=parse_text_grid.read_sentence_TextGrid('/home/hp/PycharmProjects/align/out/data-prog-conv.TextGrid')
print(segments)

if __name__ == '__main__':
    data_path='/home/hp/PycharmProjects/align/data'
    dictionary_path='/home/hp/PycharmProjects/align/models/english.dict'
    acoustic_model_path='/home/hp/PycharmProjects/align/models/english.zip'
    output_path='/home/hp/PycharmProjects/align/out'
    get_alignment(data_path,dictionary_path,acoustic_model_path,output_path)
