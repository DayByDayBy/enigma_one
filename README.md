# enigma_one 

#### encode, decode, idempotence inn


## modelling enigma, the classic cryptography machine


a model of the classic encyrption device using python, and a streamlit interface 

MVP completed, some extensions and added features yet to be added

some classic era function is not yet deployed, such as variable rotor settings (currently the first three are set to AMT, for Alan Mathison Turing), an editable/pluggable plugboard, etc 

currently running as a streamlit app on https://enigma-one.streamlit.app/



i also think it might be interesting to make it so it 
can work outside the ALL CAPS ALPHABETICALS, and maybe explore making 
more rotors. the 'reflector flaw' problem is also on the list, 
and of course TypeX is an influence there.  tbh i think it might 
also be interesting to borrow the 'multi notch' and the 
'direction-dependent notch' ideas, but that's perhaps getting 
a big ahead of myself.  heck, maybe i should also rewrite it 
all in C, golang, or something else i don't really use/should learn

oh, and shoutout to https://enigma.hoerenberg.com/

no real influence on this project, it's just kinda cool cryptography nerd stuff i found while researching the machine that you should check out if you are interested enough in enigma to be reading this.  from their site:

_"The "Breaking German Navy Ciphers" Project was founded in 2012 by Michael Hörenberg. The goal is to break original radio messages, which were encoded with the famous German ENIGMA cipher machine. Up to now, we've succeeded in deciphering over 70 original World War II Enigma I M3 and M4 messages. Many of these messages had never been broken before, so you can read them for the first time in history..."_

<!-- 
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
- Enigma class: Combines all components and handles the encryption process -->
