#99 Из Dict добавьте в меню
#    №1   menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
a = {'besh_barmak': 130}
menu.update(a)
menu.pop("lagman")
b = {'lagman': 135}
menu.update(b)
menu.pop("borsh") 
print(menu)
