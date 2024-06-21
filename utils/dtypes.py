from typing import Dict, Any

# auth_packet = {'token': '$TOKEN', 'username': '$USERNAME'}
AuthPacketDataStructure = Dict[str, Dict[str, str]]

# game_packet = {'action': '$ACTION', 'data': '$DATA'}
GamePacketDataStructure = Dict[str, Dict[str, str]]

# command_packet = {'auth': auth_packet, 'gameplay': game_packet}
CommandPacketDataStructure = Dict[str, Dict[str, Dict[str, str]]]

# packet = {'ping': 'pong'}
PacketDataStructure = Dict[str, Any]
