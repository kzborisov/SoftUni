from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.muse_elf import MuseElf
from project.dark_wizard import DarkWizard
from project.soul_master import SoulMaster
from project.knight import Knight
from project.dark_knight import DarkKnight
from project.blade_knight import BladeKnight

hero = Hero("Hero", 4)
elf = Elf("Elf", 1)
muse_elf = MuseElf("Muse Elf", 2)
wizard = Wizard("Wizard", 3)
dark_wizard = DarkWizard("Dark Wizard", 4)
soul_wizard = SoulMaster("Soul Wizard", 5)
knight = Knight("Knight", 6)
dark_knight = DarkKnight("Dark Knight", 7)
blade_knight = BladeKnight("Blade Knight", 8)


print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print('-----------------------------------')
print(str(muse_elf))
print(muse_elf.__class__.__bases__[0].__name__)
print(muse_elf.username)
print(muse_elf.level)
print('-----------------------------------')
print(str(wizard))
print(wizard.__class__.__bases__[0].__name__)
print(wizard.username)
print(wizard.level)
print('-----------------------------------')
print(str(dark_wizard))
print(dark_wizard.__class__.__bases__[0].__name__)
print(dark_wizard.username)
print(dark_wizard.level)
print('-----------------------------------')
print(str(soul_wizard))
print(soul_wizard.__class__.__bases__[0].__name__)
print(soul_wizard.username)
print(soul_wizard.level)
print('-----------------------------------')
print(str(knight))
print(knight.__class__.__bases__[0].__name__)
print(knight.username)
print(knight.level)
print('-----------------------------------')
print(str(dark_knight))
print(dark_knight.__class__.__bases__[0].__name__)
print(dark_knight.username)
print(dark_knight.level)
print('-----------------------------------')
print(str(blade_knight))
print(blade_knight.__class__.__bases__[0].__name__)
print(blade_knight.username)
print(blade_knight.level)
