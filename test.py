# -*- coding: utf-8 -*-

import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('integer', type=int, help='display an integer')
# args = parser.parse_args()
#

# print(args.integer)

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--batch_steps', default=1000, type=int, help='number of training steps')

args = parser.parse_args()
print(args)
