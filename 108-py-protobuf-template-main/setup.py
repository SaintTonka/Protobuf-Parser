from setuptools import setup
from setuptools.command.build_py import build_py
from distutils.spawn import spawn, find_executable
# import shutil

# def find_executable(executable, path=None):
#     """Find the path to an executable."""
#     return shutil.which(executable, path=path)

# def spawn(cmd, search_path=1, verbose=0, dry_run=0):
#     """Execute a command."""
#     # Note: The 'spawn' function in 'shutil' is not an exact replacement,
#     # but it can be used to execute commands. You might need to adjust
#     # the arguments or logic depending on your specific use case.
#     return shutil.which(cmd[0], path=None)  # Find the executable

class Build(build_py):
    def run(self):
        spawn([find_executable('protoc'), '--python_out=.', 'protobuf/message.proto'])
        build_py.run(self)

setup(
    name='protobuf_parser',
    version='1.0.0',
    author='R&EC SPb ETU',
    author_email='info@nicetu.spb.ru',
    url='http://nicetu.spb.ru',
    description='Разбор потока length-prefixed Protobuf сообщений на Python',
    long_description="",
    zip_safe=False,
    packages=['protobuf', 'protobuf_parser'],
    cmdclass={
        'build_py': Build
    },
)
