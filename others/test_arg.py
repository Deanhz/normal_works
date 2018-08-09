import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, help='work path', default='123')
args = parser.parse_args()
work_dir = args.i
print(work_dir)
print(os.environ['HOME'])
