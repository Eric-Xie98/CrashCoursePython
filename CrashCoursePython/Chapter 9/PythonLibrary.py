## The Python Standard Library is a set of modules contained within each installation of Python. Written by other
## programmers, these modules make certain coding portions easier.

# Take for example, the OrderedDict module that makes dictionaries ordered based on the elements that were inserted first

# Even though dictionaries after Python 3.6 are now default ordered, it's better to continue using OrderedDict in order to
# avoid conflict with previous Python versions as well as communicate to human readers that the dictioanry is
# meant to be ordered.

from collections import OrderedDict

favorite_languages = OrderedDict()      ## This creates a dictionary automatically for us that is ordered

favorite_languages['eric'] = ['python', 'java', 'octave']
favorite_languages['allinn'] = ['python']
favorite_languages['nate'] = ['matlab']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages are: ")
    
    for lang in language:
        print(lang.title())

# Being familiar with a number of modules can help make coding easier when they fit the exact real world situations
# that you need to model

