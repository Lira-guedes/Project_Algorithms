from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('ABCDEF', 3) == "CBA_FED"
    assert encrypt_message('ABCDEF', 4) == "FE_DCBA"
    assert encrypt_message('123123', 9) == "321321"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('ABCDEF', 'A')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 4)
