from dataclasses import dataclass, field
import json

from .dtypes import (
  AuthPacketDataStructure,
  GamePacketDataStructure,
  CommandPacketDataStructure,
  PacketDataStructure,
)


@dataclass
class Packet:
  category: str = field(init=False, default='Packet')
  data: PacketDataStructure

  def __str__(self) -> str:
    return str(self.data)

  def __bytes__(self) -> bytes:
    return str(self.data).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}()'


@dataclass
class AuthPacket(Packet):
  category: str = field(init=False, default='AuthPacket')
  data: AuthPacketDataStructure

  def __str__(self) -> str:
    return str(self.data)

  def __bytes__(self) -> bytes:
    return str(self.data).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}({self.data})'

  @classmethod
  def from_bytes(cls, data: bytes) -> 'AuthPacket':
    decoded_data = json.loads(data.decode('utf-8'))
    return cls(data=AuthPacketDataStructure(**decoded_data))


@dataclass
class GamePacket(Packet):
  category: str = field(init=False, default='GamePacket')
  data: GamePacketDataStructure

  def __str__(self) -> str:
    return str(self.data)

  def __bytes__(self) -> bytes:
    return str(self.data).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}({self.data})'

  @classmethod
  def from_bytes(cls, data: bytes) -> 'GamePacket':
    decoded_data = json.loads(data.decode('utf-8'))
    return cls(data=GamePacketDataStructure(**decoded_data))


@dataclass
class CommandPacket(Packet):
  category: str = field(init=False, default='CommandPacket')
  data: CommandPacketDataStructure

  def __post_init__(self):
    self.auth = self.data.get('AUTH', {})
    self.game = self.data.get('GAME', {})

  def __str__(self) -> str:
    return str({'AUTH': self.auth, 'GAME': self.game})

  def __bytes__(self) -> bytes:
    return str({'AUTH': self.auth, 'GAME': self.game}).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}(AUTH={repr(self.auth)}, GAME={repr(self.game)})'
