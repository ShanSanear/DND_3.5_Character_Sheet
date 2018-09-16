import pytest

from Character.Spells.remembered_spells import *
from Character.Spells.spell_book import SpellBook


class TestRememberedSpells:
    def test_init(self):
        sb = SpellBook()
        rs = RememberedSpells(sb)
        rs.remembered[0] = {}

    def test_added_spell(self):
        sb = SpellBook()
        sb.add_spell("Fireball", "Fireball_Desc", 3)
        rs = RememberedSpells(sb)
        rs.remember("Fireball")
        assert rs.remembered[3] == {"Fireball": {"Description": "Fireball_Desc", "level": 3}}

    def test_removed_spell(self):
        sb = SpellBook()
        sb.add_spell("Fireball", "Fireball_Desc", 3)
        rs = RememberedSpells(sb)
        rs.remember("Fireball")
        assert rs.remembered[3] == {"Fireball": {"Description": "Fireball_Desc", "level": 3}}
        rs.forget("Fireball")
        assert rs.remembered[3] == {}

    def test_incorrect_add(self):
        sb = SpellBook()
        rs = RememberedSpells(sb)
        with pytest.raises(SpellNotInSpellBook):
            rs.remember("Fireball")

    def test_incorrect_forget(self):
        sb = SpellBook()
        rs = RememberedSpells(sb)
        with pytest.raises(SpellNotRemembered):
            rs.forget("Fireball")

