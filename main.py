import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import argparse
from rag.indexing import build_index
from rag.cli import run

parser = argparse.ArgumentParser()
parser.add_argument("--index", action="store_true")
args = parser.parse_args()

if args.index:
    build_index()
else:
    run()
