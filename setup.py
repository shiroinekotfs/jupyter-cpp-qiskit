from setuptools import setup, find_packages

setup(
      name='jupyter-cpp-qiskit',
      version='1.0.0a5',
      description='Qiskit header for C++ Jupyter kernel. Provide quantum computing services for Jupyter, written in C++.',
      author='Shiroi Neko',
      author_email='shiroineko.tfs@gmail.com',
      license='MIT',
      classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows'
      ],
      url='https://github.com/shiroinekotfs/jupyter-cpp-qiskit',
      include_package_data=True,
      install_requires = ['jupyter-cpp-kernel>=1.0.0a5'],
      data_files = [
          ("share/cpp_header", 
           ['jupyter-cpp-qiskit/qiskit.hpp']
          )
      ]
)