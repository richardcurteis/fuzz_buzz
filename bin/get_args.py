#!/usr/bin/python3

import argparse

def input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-ip',
                        type=str,
                        required=False)

    parser.add_argument('-port',
                        type=int,
                        required=False)

    parser.add_argument('-path',
                        type=str,
                        required=False,
                        default='/')

    parser.add_argument('-len',
                        type=int,
                        required=False)

    parser.add_argument('-eip',
                        type=int,
                        required=False)

    parser.add_argument('-enum',
                        required=False)

    parser.add_argument('-pwn',
                        required=False)
    
    parser.add_argument('-platform',
                        type=str,
                        required=False)

    return parser.parse_args()
