from dataclasses import dataclass, field

from .dtypes import (
  AuthPacketStructure,
  GamePacketStructure,
  CommandPacketStruct,
)


@dataclass
class Packet:
  category: str = field(init=False, default='Packet')
  data: dict = field(default_factory=dict)

  def __str__(self) -> str:
    return ''

  def __repr__(self) -> str:
    return f'{self.category}()'


@dataclass
class AuthPacket(Packet):
  category: str = field(init=False, default='AuthPacket')
  data: AuthPacketStructure

  def __str__(self) -> str:
    return self.data

  def __bytes__(self) -> bytes:
    return str(self.data).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}({self.data})'


@dataclass
class GamePacket(Packet):
  category: str = field(init=False, default='GamePacket')
  data: GamePacketStructure

  def __str__(self) -> str:
    return self.data

  def __bytes__(self) -> bytes:
    return str(self.data).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}({self.data})'


@dataclass
class CommandPacket(Packet):
  category: str = field(init=False, default='CommandPacket')
  data: CommandPacketStruct

  def __post_init__(self):
    self.auth = self.data.get('AUTH', {})
    self.game = self.data.get('GAME', {})
    self.auth_data = self.auth if self.auth else {}
    self.game_data = self.game if self.game else {}

  def __str__(self) -> str:
    return str({'AUTH': self.auth_data, 'AUTH': self.game_data})

  def __bytes__(self) -> bytes:
    return str(self).encode('utf-8')

  def __repr__(self) -> str:
    return f'{self.category}(AUTH={repr(self.auth)}, GAME={repr(self.game)})'
