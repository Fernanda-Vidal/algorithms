from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message(message='message', key=15) == 'egassem'
    assert encrypt_message(message='message', key=2) == 'egass_em'
    assert encrypt_message(message='message', key=3) == 'sem_egas'

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(1, 1)

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('message', '1')
