#from setuptools import setup, find_packages
import yaml

with open('config.yaml', 'r') as f:
  config = yaml.safe_load(f)

install_path = config['installation']['install_path']
print(f"Файлы будут установлены в: {install_path}")

files = config['installation']['docs']
