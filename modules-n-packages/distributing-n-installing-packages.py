# PyPI - Python Package Index 
# pip to install
# https://pypi.org/
#pip3.7 --help
#PyPA - Python Packaging Authority
# https://github.com/pypa/sampleproject


# tree <folder_name>
# How to create a package that is installable?
# To do this, we have to use a project called setup tools

# setup.py file

# sample : https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py

# curl -O https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py in the package folder. 

# In the setup.py, you MUST look into and update the following constructs:
    a. name 
    b. version 
    c. package_dir
    d. packages 
    e. python_requires
    f. install_requires // specifies any dependencies needed to install this 
    g. entry_points= sample = sample:main // Create a executable named <sample> and within the sample, run the <main> function 


# To build a distribution:
  It's a single file that can b pip installed // Like a zip file

2 different formats:

  a. wheel  // new version
  b. egg // old

unpacks the source code into pythoins site-package dir 

# to build a wheel, do a pip install wheel 
# Next python3.7 setup.py --help


##################

$ ls
__pycache__     setup.py        src
sumants-mbp:helpers sumantrenukarya$ pip3.7 install wheel
Collecting wheel
  Downloading https://files.pythonhosted.org/packages/8c/23/848298cccf8e40f5bbb59009b32848a4c38f4e7f3364297ab3c3e2e2cd14/wheel-0.34.2-py2.py3-none-any.whl
Installing collected packages: wheel
Successfully installed wheel-0.34.2
You are using pip version 19.0.3, however version 20.2b1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
sumants-mbp:helpers sumantrenukarya$ ls
__pycache__     setup.py        src
sumants-mbp:helpers sumantrenukarya$ python3.7 setup.py --help
Traceback (most recent call last):
  File "setup.py", line 15, in <module>
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/sumantrenukarya/SUMANT/TECH/Python-Projects/pcap/modules-n-packages/helpers/README.md'

# To resolve this error, just create a README.md file 

# Then run python3.7 setup.py --help-commands

#Extra commands:
#  bdist_wheel       create a wheel distribution

sumants-mbp:helpers sumantrenukarya$ pwd
/Users/sumantrenukarya/SUMANT/TECH/Python-Projects/pcap/modules-n-packages/helpers
sumants-mbp:helpers sumantrenukarya$ ls
README.md       __pycache__     setup.py        src
sumants-mbp:helpers sumantrenukarya$ python3.7 setup.py bdist_wheel 

####################

sumants-mbp:helpers sumantrenukarya$ python3.7 setup.py bdist_wheel 
running bdist_wheel
running build
running build_py
installing to build/bdist.macosx-10.9-x86_64/wheel
running install
running install_lib
running install_egg_info
running egg_info
creating src/helpers.egg-info
writing src/helpers.egg-info/PKG-INFO
writing dependency_links to src/helpers.egg-info/dependency_links.txt
writing entry points to src/helpers.egg-info/entry_points.txt
writing requirements to src/helpers.egg-info/requires.txt
writing top-level names to src/helpers.egg-info/top_level.txt
writing manifest file 'src/helpers.egg-info/SOURCES.txt'
reading manifest file 'src/helpers.egg-info/SOURCES.txt'
writing manifest file 'src/helpers.egg-info/SOURCES.txt'
Copying src/helpers.egg-info to build/bdist.macosx-10.9-x86_64/wheel/helpers-1.0.0-py3.7.egg-info
running install_scripts
creating build/bdist.macosx-10.9-x86_64/wheel/helpers-1.0.0.dist-info/WHEEL
creating 'dist/helpers-1.0.0-py3-none-any.whl' and adding 'build/bdist.macosx-10.9-x86_64/wheel' to it
adding 'helpers/__init__.py'
adding 'helpers/strings.py'
adding 'helpers/variables.py'
adding 'helpers-1.0.0.dist-info/METADATA'
adding 'helpers-1.0.0.dist-info/WHEEL'
adding 'helpers-1.0.0.dist-info/entry_points.txt'
adding 'helpers-1.0.0.dist-info/top_level.txt'
adding 'helpers-1.0.0.dist-info/RECORD'
removing build/bdist.macosx-10.9-x86_64/wheel
  
#### After running bdist_wheel, it will create these 2 folders:

build/ and dist/

ls
README.md       __pycache__     build           dist            setup.py        src


#####

$ cd dist/
$ ls
helpers-1.0.0-py3-none-any.whl

# The above .whl is the installable file 

#####

pip install help

sumants-mbp:modules-n-packages sumantrenukarya$ pwd
/Users/sumantrenukarya/SUMANT/TECH/Python-Projects/pcap/modules-n-packages
sumants-mbp:modules-n-packages sumantrenukarya$ ls
__pycache__                             extras_1.py                             hiding-entities.py                      modules_search_path.py
creating-n-using-packages.py            helpers                                 main.py
distributing-n-installing-packages.py   helpers_1.py                            main_1.py
sumants-mbp:modules-n-packages sumantrenukarya$ pip3.7 install helpers/dist/helpers-1.0.0-py3-none-any.whl 
Processing ./helpers/dist/helpers-1.0.0-py3-none-any.whl
Collecting peppercorn (from helpers==1.0.0)
  Downloading https://files.pythonhosted.org/packages/14/84/d8d9c3f17bda2b6f49406982546d6f6bc0fa188a43d4e3ba9169a457ee04/peppercorn-0.6-py3-none-any.whl
Installing collected packages: peppercorn, helpers
Successfully installed helpers-1.0.0 peppercorn-0.6
You are using pip version 19.0.3, however version 20.2b1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

### Now this package is installed globally 



