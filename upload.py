import os
import setup
import shutil
print(f"Check if {os.getcwd()}\\__pycache__ folder exists")
if os.path.isdir(os.getcwd() + "\\__pycache__"):
    shutil.rmtree(os.getcwd() + "\\__pycache__")
    print("remove done")
print(f"Check if {os.getcwd()}\\lglib\\__pycache__ folder exists")
if os.path.isdir(os.getcwd() + "\\lglib\\__pycache__"):
    shutil.rmtree(os.getcwd() + "\\lglib\\__pycache__")
    print("remove done")
print(f"Check if {os.getcwd()}\\test\\__pycache__ folder exists")
if os.path.isdir(os.getcwd() + "\\test\\__pycache__"):
    shutil.rmtree(os.getcwd() + "\\test\\__pycache__")
    print("remove done")

setuplist = list(setup.version)

for i in range(len(setuplist)):
    try:
        setuplist[i] = int(setuplist[i])
    except ValueError:
        pass
print("Incrementing the last version number by 1")
setuplist[-1] = setuplist[-1] + 1
print("done and create a count")
count = 0
while setuplist[-1-count] == 10:
    try:
        setuplist[-1 - count] = 0
        setuplist[-1-count-2] += 1
        count += 2
    except IndexError:
        setuplist.insert(0, 1)

name = ""
for i in setuplist:
    print(f"name add setup list-{i}")
    name += str(i)
print(name)
with open(f"{os.getcwd()}\\setup.py", "r") as f:
    print(f"open {os.getcwd()}\\setup.py and start readlines")
    lines = f.readlines()
with open(f"{os.getcwd()}\\setup.py", "w") as f:
    for line in lines:
        if line.strip("\n") != f"version = \"{setup.version}\"":
            print("write done")
            f.write(line)
        else:
            print(f"rewrite done - version --> {name} <--")
            f.write(f"version = \"{name}\"\n")
'''
print("start open gui, upload gui name")
print("start marge path")
guipath = os.path.dirname(os.getcwd()) + "\\gui\\functions\\lglib.md"
print(guipath)
fname = []
for i in name:
    print(i)
    fname.append(i)
ffname = []
print(fname)
for i in fname:
    try:
        ffname.append(int(i))
    except ValueError:
        ffname.append(i)
print(ffname)
ffname[-1] -= 1
count = 0
while ffname[-1] < 0:
    if type(ffname[-1 - count]) is int:
        ffname[-1 - count] = 9
        ffname[-1 - count - 2] -= 1
        count += 2
    else:
        break
ne = ""
for i in ffname:
    ne += str(i)
with open(guipath, "r", encoding="utf-8") as file:
    print(f"open {guipath} done...")
    data = file.readlines()
    print(data, ne, "="*100)
print(ne, name)
with open(guipath, "w", encoding="utf-8") as file:
    print(f"open {guipath} done")
    for line in data:
        if line.strip("\n") != f"# lglib {ne}":
            print("is not # lglib, writed done")
            file.write(line)
        else:
            print("is # lglib, writed done")
            file.write(f"# lglib {name}\n")
'''
print(f"called cd to {os.getcwd()}")
os.system(f"cd {os.getcwd()}")
print("called packed setup.py")
os.system("python setup.py sdist bdist_wheel")
print("called twine to upload lglib")
os.system("twine upload dist/*")

import shutil

print(f"start remove {os.getcwd()}\\build")
shutil.rmtree(os.getcwd() + "\\build")
print("remove done")
print(f"start remove {os.getcwd()}\\dist")
shutil.rmtree(os.getcwd() + "\\dist")
print("remove done")
print(f"start remove {os.getcwd()}\\lglibs.egg-info")
shutil.rmtree(os.getcwd() + "\\lglib.egg-info")
print("remove done")



