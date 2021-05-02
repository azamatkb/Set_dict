#Problem000
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
a = {'besh_barmak': 130}
menu.update(a)              #сначала добавили бешпармак
menu.pop("lagman")          #удалили лагман
b = {'lagman': 135}
menu.update(b)              #добавили исправленный лагман
print(menu)
