from random import randint
def opencase():
    c=0
    fl=randint(0,100_000_000)/100_000_000
    st=''
    rar=0
    skins = [['R8 revolver | Inlay','XM1014 | Blue Spruce', 'P250 | Sand dune','(Consumer grade)'],
             ['AK-47 | Olive Garden','Negev | Bulkhead', 'UMP-45 | Gunsmoke','(Industrial grade)'],
             ['SG553 | Cyberforce','AK-47 | Uncharted','Desert Eagle | Urban Rubble','(Mil-spec grade)'],
             ['AWP | Pit Viper', 'AK-47 | Slate','AUG | Torque', '(Restricted grade)'],
             ['AK-47 | Case hardened','Glock-18 | Vogue', 'SCAR-20 | Cardiac', '(Classified grade)'],
             ['AWP | Dragon Lore', 'AK-47 | Legion of Anubis','R8 Revolver | Fade', '(Covert grade)'],
             ['Karambit | Case Hardened','Kukri knife | Fade', 'Butterfly knife | Gamma Doppler', '(Special)']]
    rar=randint(1,4)
    if rar == 2:
        st = 'Stattrack '
    rar=randint(0,500)
    if rar<=299:
        rar=0
    elif rar<=399:
        rar=1
    elif rar<=449:
        rar=2
    elif rar<=479:
        rar=3
    elif rar<=493:
        rar=4
    elif rar<=498:
        rar=5
    else:
        rar=6
    print(st+skins[rar][randint(0,2)]+' ' + skins[rar][3])
    print('pattern ', str(randint(0,1000)))
    print('float ', str(fl))
print('To open a case, write opencase()')
