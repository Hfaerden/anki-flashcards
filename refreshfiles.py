import requests
from bs4 import BeautifulSoup
url = "https://www.worldcubeassociation.org/regulations/full/"

#clears files to reprint all regs and guidelines
open("regulations.csv", "w").close()
open("guidelines.csv", "w").close()
open("regs.txt", "w").close()

#updates regulations in regs.txt
nightmarelistwithalltheregs = BeautifulSoup(requests.get(url).text).get_text().split("\n")

with open("regs.txt", "a", encoding="utf-8") as f:
    for line in nightmarelistwithalltheregs:
        if (not line.startswith("For")) and ((")" in line) or ("Article" in line and line.startswith(" "))):
            f.write(line + "\n")

#Guidelines
with open("regs.txt", "r") as f:
    with open("guidelines.csv", "a") as g:
        all = f.readlines()
        for reg in all:
            if reg.startswith(" Article"):
                currentarticle = reg.split(":")[0].replace(" ", "_")
            if (reg.split(")")[0]).endswith("+"):
                justreg = reg.split(")")
                regnum = justreg.pop(0).rstrip()
                g.write(regnum+ "\t"+ "".join(justreg).rstrip() + "\t " + currentarticle + "\n")

#Regs
with open("regs.txt", "r") as f:
    with open("regulations.csv", "a") as g:
        all = f.readlines()
        for reg in all:
            if reg.startswith(" Article"):
                currentarticle = reg.split(":")[0].replace(" ", "_")
                continue
            if not (reg.split(")")[0]).endswith("+"):
                justreg = reg.split(")")
                regnum = justreg.pop(0).rstrip()
                g.write(regnum+ "\t"+ "".join(justreg).rstrip() + "\t " + currentarticle + "\n")

print("completed")