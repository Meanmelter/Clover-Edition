from importlib.metadata import version
def CompareInstalledPackages():
    #installed = str(subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']))
    #transformer = installed.split(find('transformers'))
    #print(transformer)
    try:
        transformers = version('transformers')
    except importlib.metadata.PackageNotFoundError(name): 
        transformers = False
    try:
        colorama = version ('colorama')
    except importlib.metadata.PackageNotFoundError(name): 
        colorama = False
    try:
        prompt_toolkit = version('prompt_toolkit')
    except importlib.metadata.PackageNotFoundError(name): 
        prompt_toolkit = False
    try:
        false = version ('false')
    except version.PackageNotFoundError:
        false = False
    
    
    print(transformers, colorama, prompt_toolkit, false)
    
CompareInstalledPackages();
    