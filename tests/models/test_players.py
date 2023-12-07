import pytest
import logging
import secrets

from chess.models.players import Player


def test_init_player():
    """create a player"""
    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    p = Player(lastname, firstname)
    logging.warning(p)


def test_to_dict():
    """convert player to dict"""
    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    p = Player(lastname, firstname)
    logging.warning(p.to_dict())


# def test_from_dict():
#     """convert dict to player"""
#     firstname = "test" + secrets.token_hex(4)
#     lastname = "test" + secrets.token_hex(4)
#     p_dict = {
#         'firstname': firstname.capitalize(),
#         'lastname': lastname.upper(),
#     }
#
#     p = Player.from_dict(p_dict)
#     logging.warning(p)


def test_create():
    """convert dict to player"""
    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    p = Player(firstname, lastname)
    p.create()
    logging.warning(p)

