from .g711 import PcmaEncoder, PcmuEncoder
from .opus import OpusEncoder
from .vpx import VpxEncoder


def get_encoder(codec):
    if codec.name == 'opus':
        return OpusEncoder()
    elif codec.name == 'PCMU':
        return PcmuEncoder()
    elif codec.name == 'PCMA':
        return PcmaEncoder()
    elif codec.name == 'VP8':
        return VpxEncoder()
    else:
        return None