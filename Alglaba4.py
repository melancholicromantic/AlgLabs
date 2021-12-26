import tkinter as tk
import random
import time
#######################
n = 0
mass = []
mass1 = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]
och = []
vers = []
for i in range(n):
    vers.append(i + 1)
obrab = []

#############################
root = tk.Tk()
root['bg'] = 'black'
root.title('Ха')
visver = []
#root.wm_attributes('-alpha', 0.7)
root.geometry('1500x800')

root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=800, width=1500, bg='black')
canvas.pack()
canvas.update()

frame = tk.Frame(root, bg = 'white')
frame.place(relwidth=0.4, relheight=0.3)
fio = tk.Label(frame, text='Вахитов Тимур Фаилович, ПРО-228', bg='white', font='Times 16').place(x=0, y=0)
v1 = tk.Label(frame, text="Вершина 1", bg='white', font='Times 12').place(x=0, y=28)
v2 = tk.Label(frame, text="Вершина 2", bg='white', font='Times 12').place(x=0, y=74)
polev1 = tk.Entry(frame, bg='white')
polev1.place(x=0, y=50)
polev2 = tk.Entry(frame, bg='white')
polev2.place(x=0, y=96)
vr1 = []
vr2 = []
kolvouzlov = 0
coordinatos = []
def cuzel():
    global n, vr1, vr2, mass, coordinatos
    vr1 = int(polev1.get()) - 1
    vr2 = int(polev2.get()) - 1
    try:
        if visver[vr1][0] > visver[vr2][0]:
            x1 = visver[vr1][0] - 10
            x2 = visver[vr2][0] + 10
        else:
            x1 = visver[vr1][0] + 10
            x2 = visver[vr2][0] - 10
        if visver[vr1][1] > visver[vr2][1]:
            y1 = visver[vr1][1] - 10
            y2 = visver[vr2][1] + 10
        else:
            y1 = visver[vr1][1] + 10
            y2 = visver[vr2][1] - 10
        canvas.create_line(x1, y1, x2, y2, width=5, fill='green')
        coordinatos.append([vr1, vr2])
        canvas.update()
        mass[vr1][vr2] = 1
        mass[vr2][vr1] = 1
    except:
        pass
def ster():
    global mass, n, kolvouzlov, visver, pokraska
    canvas.delete('all')
    mass.clear()
    obrab.clear()
    visver.clear()
    n = 0
    kolvouzlov = 0
    visver.clear()
    pokraska.clear()
btn = tk.Button(frame, text='Создать связь', bg='green', command=cuzel, font='Times 12')
btn.place(x=0, y=150)
rem = tk.Button(frame, text='Стереть всё', command=ster, bg='green', font='Times 12')
rem.place(x=120, y=190)

pokraska = []

def crv(event):
    global n, mass, pokraska
    vers.append(n)
    x = event.x
    y = event.y
    if (x > 700) or (y > 300):
        n += 1
        for i in range(n):
            try:
                mass[i].append(0)
            except:
                mass.append([])
                for j in range(n):
                    mass[-1].append(0)
        for i in range(n):
            try:
                print(mass[0][i], end=' ')
            except:
                pass
        print('\n')
        pv = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="green", width=2)
        pokraska.append(pv)
        canvas.create_text(x, y, text=str(n), fill='white', font=('Times', 14))
        visver.append([x, y])
        vers.append(n)
        canvas.update()
root.bind('<Button-1>', crv)

###############################################
polevts = tk.Entry(frame, bg='white')
polevts.place(x=150, y=50)

tasamaya = 0
def choice():
    canvas.create_rectangle(0, 280, 300, 320, fill='black')
    global tasamaya
    tasamaya = int(polevts.get())
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            print(mass[i][j], end=' ')
        print('\n')
    cyc(tasamaya)
visitedver = 1
visited = []
def svas(u, visited):
    global n, mass, visitedver
    visited[u] = True
    for v in range(n):
        for i in range(n):
            if mass[u][v] == 1:
                if not visited[v]:
                    visitedver += svas(v, visited)
    return visitedver
infa = canvas.create_text(120, 300, text='', fill='white', font=('Times', 14))
def cyc(v):
    canvas.create_rectangle(0, 240, 300, 300, fill='black')
    global mass, obrab, och, n, visitedver
    visited = []
    conn = 0
    for i in range(n):
        visited.append(False)
    if svas(0, visited) < n:
        canvas.create_text(120, 300, text='Граф несвязный', fill='white', font=('Times', 14))
        canvas.update()
    else:
        for i in range(n):
            canvas.itemconfig(pokraska[i], fill='green')
        for i in range(n):
            for j in range(i + 1, n):
                if mass[i][j] == 1:
                    if visver[i][0] > visver[j][0]:
                        x1 = visver[i][0] - 10
                        x2 = visver[j][0] + 10
                    else:
                        x1 = visver[i][0] + 10
                        x2 = visver[j][0] - 10
                    if visver[i][1] > visver[j][1]:
                        y1 = visver[i][1] - 10
                        y2 = visver[j][1] + 10
                    else:
                        y1 = visver[i][1] + 10
                        y2 = visver[j][1] - 10
                    canvas.create_line(x1, y1, x2, y2, width=5, fill='green')
        out = ''
        uz1 = [1, 2]
        uz2 = [1, 2]
        obrab.append(v)
        och.append([1])
        canvas.itemconfig(pokraska[v - 1], fill='red')
        uz1 = visver[v - 1]
        canvas.update()
        time.sleep(0.5)
        st = 0
        predok = 0
        for i in range(len(mass)):
            if mass[v - 1][i] == 1:
                och[0].append(i + 1)
        predok = v - 1
        metka = 1
        while (len(obrab) != n):
            predudalen = 0
            try:
                st = och[0].pop(1)
            except:
                och.pop(0)
                uz1 = visver[och[0][0] - 1]
                metka = 0
            while (st in obrab) and (len(och) != 0):
                if len(och[0]) < 2:
                    och.pop(0)
                    predudalen = 1
                else:
                    st = och[0].pop(1)
            if predudalen == 1:
                uz1 = visver[och[0][0] - 1]
            if (len(och[0]) < 1) and (metka != 1):
                och.pop(0)
                uz1 = visver[och[0][0] - 1]
            obrab.append(st)
            uz2 = visver[st - 1]
            canvas.itemconfig(pokraska[st - 1], fill='red')
            for i in range(n):
                for j in range(n):
                    if mass[visver.index(uz1)][visver.index(uz2)] == 1:
                        if uz1[0] > uz2[0]:
                            x1 = uz1[0] - 10
                            x2 = uz2[0] + 10
                        else:
                            x1 = uz1[0] + 10
                            x2 = uz2[0] - 10
                        if uz1[1] > uz2[1]:
                            y1 = uz1[1] - 10
                            y2 = uz2[1] + 10
                        else:
                            y1 = uz1[1] + 10
                            y2 = uz2[1] - 10
                        canvas.create_line(x1, y1, x2, y2, width=5, fill='red')
            canvas.update()
            time.sleep(1)
            try:
                och.append([])
                och[-1].append(st)
                for i in range(n):
                    if (mass[st - 1][i] == 1) and (i + 1 not in obrab):
                        och[-1].append(i + 1)
                if len(och[-1] == 0):
                    och.pop(-1)
            except:
                pass
        for u in range(n):
            out = out + ' ' + str(obrab[u])
        canvas.create_text(120, 300, text=out, fill='white', font=('Times', 14))
    obrab.clear()
    och.clear()
    canvas.update()
    visited.clear()
    visitedver = 1

pusk = tk.Button(frame, text='Поиск в ширину', command = choice, bg='green', font='Times 12')
pusk.place(x=150, y=100)

################Laba 5################
stek = []

def ve():
    v = int(polevts.get())
    newc(v)
def newc(v):
    canvas.create_rectangle(0, 240, 300, 320, fill='black')
    global n, mass, stek, visitedver
    global polevts
    for i in range(n):
        canvas.itemconfig(pokraska[i], fill='green')
    for i in range(n):
        for j in range(i + 1, n):
            if mass[i][j] == 1:
                if visver[i][0] > visver[j][0]:
                    x1 = visver[i][0] - 10
                    x2 = visver[j][0] + 10
                else:
                    x1 = visver[i][0] + 10
                    x2 = visver[j][0] - 10
                if visver[i][1] > visver[j][1]:
                    y1 = visver[i][1] - 10
                    y2 = visver[j][1] + 10
                else:
                    y1 = visver[i][1] + 10
                    y2 = visver[j][1] - 10
                canvas.create_line(x1, y1, x2, y2, width=5, fill='green')
    canvas.update()
    time.sleep(1)
    ce = []
    uz1 = [1, 2]
    uz2 = [1, 2]
    current = 0
    rebra = 0
    emass = []
    for i in range(n):
        emass.append([])
        for j in range(n):
            emass[i].append(mass[i][j])
    for i in range(n):
        for j in range(n):
            if emass[i][j] == 1:
                rebra += 1
    rebra //= 2
    current = v - 1
    stek.append(current)
    netu = 0
    lr = 0
    flaghok = 0
    for i in range(n):
        for j in range(n):
            if mass[i][j] == 1:
                lr += 1
        if lr % 2 == 1:
            flaghok = 1
            break
        lr = 0
    visited = []
    conn = 0
    for i in range(n):
        visited.append(False)
    if svas(0, visited) < n:
        flaghok = 1
    if flaghok == 0:
        while rebra != 0:
            netu = 0
            while netu == 0:
                netu = 1
                for i in range(n):
                    if emass[current][i] == 1:
                        emass[current][i] = 0
                        emass[i][current] = 0
                        current = i
                        stek.append(current)
                        rebra -= 1
                        netu = 0
                        break
            ce.append(stek.pop(-1))
            current = stek[-1]
        for i in range(len(stek)):
            ce.append(stek[len(stek) - i - 1])
        for reb in range(len(ce) - 1):
            canvas.itemconfig(pokraska[ce[reb]], fill='red')
            canvas.update()
            time.sleep(0.5)
            uz1 = visver[ce[reb]]
            uz2 = visver[ce[reb + 1]]
            if uz1[0] > uz2[0]:
                x1 = uz1[0] - 10
                x2 = uz2[0] + 10
            else:
                x1 = uz1[0] + 10
                x2 = uz2[0] - 10
            if uz1[1] > uz2[1]:
                y1 = uz1[1] - 10
                y2 = uz2[1] + 10
            else:
                y1 = uz1[1] + 10
                y2 = uz2[1] - 10
            canvas.create_line(x1, y1, x2, y2, width=5, fill='red')
            canvas.update()
            time.sleep(1)
    else:
        canvas.create_text(120, 300, text='Эйлерова цикла нет', fill='white', font=('Times', 14))
    canvas.update()
    stek.clear()
    ce.clear()
    emass.clear()
    visitedver = 1


eiler = tk.Button(frame, text='Нахождение Эйлерова цикла', command = ve, bg='green', font='Times 12')
eiler.place(x=225, y=200)
root.mainloop()

print('op')
