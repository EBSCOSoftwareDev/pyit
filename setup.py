from setuptools import setup, find_packages
import re
import sys
setup(name='pyit',
      version='0.0.3',
      description='Helpful scripts to manage Magento and Wordpress deployments and development tasks',
      url='https://github.com/EBSCOSoftwareDev/pyit',
      author='Ebsco Industries',
      author_email='PACE@ebsco.com',
      license='Apache License 2.0',
      packages=find_packages(".", exclude=["test"]),
      zip_safe=False,
      install_requires = ['pyzabbix>=0.7, <1' ]+ [])
                        #(['pywin32==218'] if re.match('^win.*', sys.platform) else []), #Windows only dependencies - Matching what cloudbase init has - to not break it


      #scripts =["mai_server/cli/mai_server_cli.py"])
