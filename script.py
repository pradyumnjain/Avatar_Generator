import sys
import os
from cartoonize import cartoon
import network 
import guided_filter 
from seg import DeepLabModel
from seg import run_visualization


"""
    Background Removal
"""
inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]
name= outputFilePath
outputFilePath= "test_code/test_images/"+outputFilePath

if inputFilePath is None or outputFilePath is None:
  print("Bad parameters. Please specify input file path and output file path")
  exit()

modelType = "xception_model"


MODEL = DeepLabModel(modelType)
print('model loaded successfully : ' + modelType)

run_visualization(inputFilePath, outputFilePath, MODEL)


"""
    Cartoonifying
"""

model_path = 'test_code/saved_models'
load_folder = 'test_code/test_images'
save_folder = 'test_code/cartoonized_images'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
cartoon(load_folder, save_folder, model_path,name)