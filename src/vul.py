import yaml
import logging

logging.basicConfig(level=logging.INFO)

def yaml_load(filename):
    '''
    use filename variable to open a file
    load the contents into a variable with yaml and retrun it
    '''
    with open(filename, 'r') as f:
        data = yaml.load(f)
        return data

def hello_world():
    logging.info('Hello, World!')
