import warnings
warnings.filterwarnings("ignore")
import os, sys
import pickle
from tqdm import tqdm
from os import path


root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

cyp_base_models_path = os.path.abspath(os.path.join(root, '../../../checkpoints'))
print(cyp_base_models_path)

cyp450_models = [
        'CYP2C9_inhib',
        'CYP2C9_subs',
        'CYP2D6_inhib',
        'CYP2D6_subs',
        'CYP3A4_inhib',
        'CYP3A4_subs'
]

def load_models():

    print(f'Loading CYP450 random forest models', file=sys.stdout)

    cyp450_models_dict = {
        'CYP2C9_inhib': {},
        'CYP2C9_subs': {},
        'CYP2D6_inhib': {},
        'CYP2D6_subs': {},
        'CYP3A4_inhib': {},
        'CYP3A4_subs': {},
    }

    for model_name in tqdm(cyp450_models_dict.keys()):
        for model_number in tqdm(range(0, 64)):
            cyp450_model_path = os.path.join(cyp_base_models_path, model_name, "model_{}".format(model_number))
            if path.exists(cyp450_model_path) and os.path.getsize(cyp450_model_path) > 0:
                with open(cyp450_model_path, 'rb') as pkl_file:
                    cyp450_models_dict[model_name][f'model_{model_number}'] = pickle.load(pkl_file)
    print(f'Finished loading CYP450 model files', file=sys.stdout)
    return cyp450_models_dict
    

# cyp450_models_dict = load_models() # We are bypassing this because this function loads all ~5G worth of models into memory at the same time

def load_single_model(model_name, model_number):
    cyp450_model_path = os.path.join(cyp_base_models_path, model_name, "model_{}".format(model_number))
    if path.exists(cyp450_model_path) and os.path.getsize(cyp450_model_path) > 0:
        with open(cyp450_model_path, 'rb') as pkl_file:
            return pickle.load(pkl_file)
    else:
        return None
