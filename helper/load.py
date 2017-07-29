import zipimport

importer = zipimport.zipimporter('numpy.zip')
print importer.load_module('numpy.array')