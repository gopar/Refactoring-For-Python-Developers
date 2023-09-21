import pytest
from .before import RPGCharacter


@pytest.fixture
def character():
    return RPGCharacter(6)


def test_attack_with_sword(character):
    assert character.attack("sword") == 20


def test_attack_with_bow(character):
    assert character.attack("bow") == 15


def test_heal(character):
    character.health = 35
    assert character.heal() == 45


def test_cast_spell(character):
    assert character.cast_spell() == "Fireball"
