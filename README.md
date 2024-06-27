# enigma_one 

 encode, decode, holiday inn

this is an attempt to model enigma, the classic machine

early days, hence the whiteboard-and-post-its vibe to the readme and some of the comments 



M:

- core encryption algorithm (encode/decode)
- rotor mechanism (configurable, )
- plugboard: emulating the plugboard for additional encryption permutations.
- user Interface: A secure and user-friendly interface for inputting and decrypting messages.
- Security Protocols: Robust encryption protocols to ensure data integrity and confidentiality.
- Documentation: Comprehensive documentation for users and developers.

S:

C
W



1. scherbius' OG:

- keyboard for input
- lampboard for output
- plugboard for initial substitution
- 3-5 rotors
- reflector

bletchley's exploit: no letter substituted for itself
    it would seem like a good enigma+ extension to try to fix flaw, but that would also potentially become a new flaw if it is implemeted clumsily. given the numebrs involved, 

possible components:
- Rotor class: Represents each rotor with its wiring and rotation mechanism
- Reflector class: Handles the reflection of signals
- Plugboard class: Manages the plugboard connections
- Enigma class: Combines all components and handles the encryption process
