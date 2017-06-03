from cx_Freeze import setup, Executable

includefiles = ['settings.json', 'phjs.exe']

setup(
    name="Bot Xapo",
    version="0.1",
    executables = [Executable("main.py")],
    author='Felipe Mansilla',
    author_email='devfelipe.mansilla@gmail.com',
    options = {'build_exe': {'include_files':includefiles}}, 
 )

