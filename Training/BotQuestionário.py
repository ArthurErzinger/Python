import pyautogui
from time import sleep
from random import randint
pyautogui.PAUSE = 1.5
sleep(5)


#VARIÁVEIS

#PÁGINA 2
listaIdades = [376, 400, 438, 471, 501, 531, 570, 621, 650, 681, 712, 753, 785, 829]

#PÁGINA 3
genero = [291, 342]
estadoCivil = [600, 663, 725, 847]

#PÁGINA 4
comoOuviu = [284,347,412,456,522]
percepção = [711,774,840,903,967]

#PÁGINA 5
impressão = [285,346,403,470,534,588]
jaViu = [784,843]
fonteInformaçao = [309,364,438,491,552]
quaoProvavel = [603,674,744,811,882,953,1021,1088,1160,1225,1296]

#PÁGINA 6
frequencia = [159,216,274,332,405]
categoria = [622,695,749,807,869,930]

#PÁGINA 7
percepcaoGeral = [152,209,275,340,392]
nivelConhecimento = [625,688,741,800,870]

#PÁGINA 9
pag91 = [818, 934, 1045, 1163, 1276]
pag92 = [811, 929, 1039, 1156, 1274]
pag93 = [812, 933, 1047, 1164, 1276]
pag94 = [255, 311, 372, 443, 492]
pag95 = [317, 374, 437, 492, 546, 616, 670, 739, 796, 860, 920]
pag96 = [321, 378, 425, 497, 563, 624, 676, 741, 804, 868, 927]
pag97 = [318, 386, 440, 507, 557, 633, 684, 752, 805, 870, 941]
pag98 = [256, 319, 379, 422, 498, 563, 624, 679, 739, 803, 860]


#PÁGINA 11
pag111 = [817, 936, 1047, 1161, 1278]
pag112 = [797, 908, 1031, 1161, 1276]
pag113 = [232, 284, 350, 414, 473]
pag114 =[708, 765, 831, 886, 948]
pag115 =[341, 409, 463, 530, 593, 646, 711, 766, 831, 888, 954]
pag116 =[353, 416, 474, 535, 596, 656, 715, 782, 842, 899, 958]
pag117 =[366, 418, 482, 534, 601, 660, 722, 783, 845, 905, 964]
pag118 =[256, 318, 379, 439, 502, 560, 619, 678, 740, 805, 858]


#PÁGINA 13
pag131 = [818, 935, 1045, 1163, 1276]
pag132 = [820, 933, 1048, 1162, 1277]
pag133 = [820, 929, 1049, 1165, 1280]
pag134 = [339, 403, 466, 525, 584]
pag135 =[397, 450, 506, 576, 643, 694, 758, 825, 882, 943]
pag136 =[346, 402, 463, 520, 579, 642, 702, 769, 835, 887]
pag137 = [283, 348, 412, 465, 526, 584, 650, 711, 771, 834]
pag138 = [319, 374, 433, 501, 559, 618, 686, 743, 806, 867]

#PÁGINA 14
pag141 = [316,384,446]
pag142 = [667,733,789,854,922]





for i in range (90):
    pyautogui.click(x=1193, y=565)
    pyautogui.hotkey('ctrl','shift', 'n')
    pyautogui.click(x=380, y=62)
    pyautogui.typewrite('https://pucpr.co1.qualtrics.com/jfe/form/SV_24EiXeoCJmS7oqi\n')

    #PÁGINA 1
    pyautogui.click(x=753, y=285)
    pyautogui.click(x=1305, y=486)

    #PÁGINA 2
    pyautogui.click(x=638, y=275)
    pyautogui.click(x=612, y = listaIdades[randint(0, 13)])
    pyautogui.click(x=1311, y=405)


    #PÁGINA 3
    pyautogui.click(x=700, y = genero[randint(0, 1)])
    pyautogui.click(x=700, y = estadoCivil[randint(0,3)])
    pyautogui.click(x=1316, y=991)

    #PÁGINA 4 - REFAZER POSIÇÕES APÓS SCROLL
    pyautogui.scroll(-200)
    pyautogui.click(x=633, y= comoOuviu[randint(0,4)])
    pyautogui.click(x=633, y= percepção[randint(0,4)])
    pyautogui.click(x=1285, y=1003)

    #PÁGINA 5
    pyautogui.click(x=594,y=impressão[randint(0,5)])
    pyautogui.click(x=594,y=jaViu[randint(0,1)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=594,y=fonteInformaçao[randint(0,4)])
    pyautogui.click(x=quaoProvavel[randint(0,9)], y=862)
    pyautogui.click(x=1296, y=1004)

    #PÁGINA 6
    pyautogui.scroll(-200)
    pyautogui.click(x=594,y=frequencia[randint(0,4)])
    pyautogui.click(x=594,y=categoria[randint(0,5)])
    pyautogui.click(x=1294, y=1059)



    #PÁGINA 7
    pyautogui.scroll(-200)
    pyautogui.click(x=594,y=percepcaoGeral[randint(0,4)])
    pyautogui.click(x=594,y=nivelConhecimento[randint(0,4)])
    pyautogui.click(x=1311, y=1001)

    #PÁGINA 8
    pyautogui.click(x=1303, y=919)

    #PÁGINA 9
    pyautogui.click(x=pag91[randint(0,4)], y=378)
    pyautogui.click(x=pag92[randint(0,4)], y=644)
    pyautogui.click(x=pag93[randint(0,4)], y=918)
    pyautogui.scroll(-1100)
    pyautogui.click(x=674, y=pag94[randint(0,4)])
    pyautogui.scroll(-500)
    pyautogui.click(x=674, y=pag95[randint(0,10)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=674, y=pag96[randint(0,10)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=674, y=pag97[randint(0,10)])
    pyautogui.scroll(-1150)
    pyautogui.click(x=674, y=pag98[randint(0,10)])
    pyautogui.click(x=1302, y=1018)

    #PÁGINA 10
    pyautogui.click(x=1294, y=920)

    #PÁGINA 11
    pyautogui.click(x=pag111[randint(0,4)], y=411)
    pyautogui.click(x=pag112[randint(0,4)], y=682)
    pyautogui.scroll(-800)
    pyautogui.click(x=658, y=pag113[randint(0,4)])
    pyautogui.click(x=658, y=pag114[randint(0,4)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag115[randint(0,10)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag116[randint(0,10)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag117[randint(0,10)])
    pyautogui.scroll(-1150)
    pyautogui.click(x=658, y=pag118[randint(0,10)])
    pyautogui.click(x=1292, y=1011)

    #PÁGINA 12
    pyautogui.scroll(-1000)
    pyautogui.click(x=1309, y=1003)

    #PÁGINA 13
    pyautogui.click(x=pag131[randint(0,4)], y=409)
    pyautogui.click(x=pag132[randint(0,4)], y=682)
    pyautogui.click(x=pag133[randint(0,4)], y=957)
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag134[randint(0,4)])
    pyautogui.scroll(-500)
    pyautogui.click(x=658, y=pag135[randint(0,9)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag136[randint(0,9)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag137[randint(0,9)])
    pyautogui.scroll(-1000)
    pyautogui.click(x=658, y=pag138[randint(0,9)])
    pyautogui.click(x=1283, y=1003)

    #PÁGINA 14
    pyautogui.click(x=679, y=pag141[randint(0,2)])
    pyautogui.click(x=679, y=pag142[randint(0,4)])
    pyautogui.click(x=1289, y=1049)

    pyautogui.hotkey('alt','f4')

