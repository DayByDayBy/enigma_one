# enigma_one 

#### encode, decode, idempotence inn


## modelling enigma, the classic cryptography machine

early days, hence the whiteboard-and-post-its vibe to the readme and some of the comments

plan is to make the classic function (aimihg for mid to late war, ie 3 rotors 
and 1 relfector, plugboard), and then maybe make the variants (M4, etc)

if that works fine, i also think it might be interesting to make one that 
can work outside the ALL CAPS ALPHABETICALS, and maybe explore making one 
with more rotors. the reflector problem is also on the list, 
and of course TypeX is an influence there, and tbh i think it might 
also be interesting to borrow the 'multi notch' idea, and the 'direction-dependent notch' idea

oh, and shoutout to https://enigma.hoerenberg.com/

no real influence on this project, it's just kinda cool cryptography nerd stuff i found while researching the machine that you should check out if you are interested enough in enigma to be reading this.  from their site:

_"The "Breaking German Navy Ciphers" Project was founded in 2012 by Michael Hörenberg. The goal is to break original radio messages, which were encoded with the famous German ENIGMA cipher machine. Up to now, we've succeeded in deciphering over 70 original World War II Enigma I M3 and M4 messages. Many of these messages had never been broken before, so you can read them for the first time in history..."_


M:

- core encryption algorithm (encode/decode)
- rotor mechanism (configurable, )
- plugboard: emulating the plugboard for additional encryption permutations.
- user Interface: A secure and user-friendly interface for inputting and decrypting messages.
- Security Protocols: Robust encryption protocols to ensure data integrity and confidentiality.
- Documentation: Comprehensive documentation for users and developers.

S:

C: 

W:

- complete the moscow board, i guess? got too excited geeking out about cryptopgraphy, just got stuck in 




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



-----   --------------------------------




update: 
got in a bit late, so the readme will have to wait
code is now more like i expect it to be and passing basic tests, altho i am still to write one set of them, test_enigma.py is empty atm