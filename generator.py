from utils import make_sh
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--read', help = 'json filename to read', default = 'hyperparameters')
parser.add_argument('--python', help = 'python filename to run', default = 'train')
parser.add_argument('--bash', help = 'bash filename to run', default = 'grid_searcher')
args = parser.parse_args()

f = open(f'{args.read}.json')
args_grids = json.load(f)
    



make_sh(args_grids, python_name = args.python, bash_name = args.bash)