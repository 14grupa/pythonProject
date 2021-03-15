from PIL import Image
import random
import math


def generate_voronoi_diagram(width, height, num_cells):
    print ("Ievadiet punktu koordinātes. Katra koordināte jābūt vesels skaitlis intevālā no 0 līdz 500")
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size

    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        got_x = False
        got_y = False
        strx = "Punkta numurs: " + str(i+1) + ", punkta x-koordināte:"
        stry = "Punkta numurs: " + str(i+1) + ", punkta y-koordināte:"
        try:
            x1 = int(input(strx))
        except:
            got_x = False
            x1 = -1
        while not got_x:


            if (x1 < 0) or (x1 > 500):
                try:
                    x1 = int(input("Ievades kļūda. Mēģiniet vēlreiz:"))
                except:
                    got_x = False
                    x1 = -1

            else:
                got_x = True
        try:
            y1 = int(input(stry))
        except:
            got_x = False
            y1 = -1
        while not got_y:

            if (y1 < 0) or (y1 > 500):
                try:
                    y1 = int(input("Ievades kļūda. Mēģiniet vēlreiz:"))
                except:
                    got_y = False
                    y1 = -1

            else:
                got_y = True
        nx.append(x1)
        ny.append(y1)

        nr.append(random.randrange(256))
        ng.append(random.randrange(256))
        nb.append(random.randrange(256))
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx - 1, imgy - 1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("VoronoiDiagram.png", "PNG")
    image.show()
num_got = False
try:
    num_cells = int(input("Ievadiet punktu skaitu:"))

    num_got = True
except:
    while not num_got:

        try:
            num_cells = int(input("Ievades kļūda. Mēģiniet vēlreiz:"))

            num_got = True
        except:
            got_num = False

if (num_cells >= 0):
    generate_voronoi_diagram(500, 500, num_cells)
else:
    print("Ievades kļūda. Punktu skaits jābūt pozitīvs vesels skaitlis")