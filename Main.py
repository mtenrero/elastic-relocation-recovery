#!/usr/bin/python

import sys
import configparser
import argparse
import elasticResolver

def loadConfig():
    global config
    aparser = argparse.ArgumentParser(description='Automatic ElasticSearch Cluster FullRestart indexes Recoverer')

    aparser.add_argument('-e', '--endpoint', required=True, help='ElasticSearch host and port')
    
    config = aparser.parse_args()
    print("Config loaded")

def main():
    loadConfig()
    elasticResolver.resolveAllocation(endpoint= config.endpoint)

if __name__ == "__main__": 
    main() 