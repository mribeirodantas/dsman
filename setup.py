import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dsman',
     version='0.2',
     scripts=['dsman'] ,
     author="Marcel Ribeiro-Dantas",
     author_email="marcel.ribeiro-dantas@curie.fr",
     description="Data Science projects Manager",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/mribeirodantas/dsman",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
         "Operating System :: OS Independent",
     ],
 )
