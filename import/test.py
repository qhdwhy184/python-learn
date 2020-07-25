
from importlib._bootstrap_external import _NamespacePath

print('before import')
# from pkg.lib import LIB_NAME
import pkg
# print('pkg.__file__:{}'.format(pkg.__file__))
# from pkg.sub import lib
import pkg.sub.lib
print('after import, LIB_NAME:{}'.format(pkg.sub.lib.LIB_NAME))
print('pkg.sub.lib.__file__:{}'.format(pkg.sub.lib.__file__))
print('pkg.sub:{}'.format(pkg.sub))
print('dir pkg:{}'.format(dir(pkg)))
print('pkg.__path__:{}'.format(pkg.__path__))
it = iter(pkg.sub.__path__)
print(next(it))
it = iter(pkg.__path__)
print(next(it))
print(pkg.__path__._path[0] == '/Users/yuanhuiw/PersonalGitSource/pythonlearn/import/pkg')
print(pkg.__path__)
print(pkg.sub.__path__)
