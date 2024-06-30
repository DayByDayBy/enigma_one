import streamlit as st
from enigma_machine.rotor import Rotor
from enigma_machine.reflector import Reflector
from enigma_machine.plugboard import Plugboard
from enigma_machine.enigma import Enigma

st.title("_enigma")

def create_rotor_display(rotor_name, position):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    display_range = 3
    rotor_display = ''.join([f"[{alphabet[(alphabet.index(position)+i)%26]}]" if i == 0 else f" {alphabet[(alphabet.index(position)+i)%26]}" for i in range(-display_range, display_range+1)])
    st.text(f"{rotor_name} at position {rotor_display}")

rotor_options = [
    ("Rotor I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    ("Rotor II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    ("Rotor III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    ("Rotor IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    ("Rotor V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
]

initial_positions = ['A', 'M', 'T']

# Display rotor positions

create_rotor_display("Rotor I", initial_positions[0]) 
create_rotor_display("Rotor II", initial_positions[1])
create_rotor_display("Rotor III", initial_positions[2])

# Optional rotors
use_rotor_iv = st.checkbox("Use Rotor IV")
use_rotor_v = st.checkbox("Use Rotor V")

selected_rotors = rotor_options[:3]
if use_rotor_iv:
    selected_rotors.append(rotor_options[3])
    initial_positions.append('A')
if use_rotor_v:
    selected_rotors.append(rotor_options[4])
    initial_positions.append('A')

input_message = st.text_input('Enter plaintext or cipher:')
input_message = input_message.upper()

if not all(ch.isalpha() or ch.isspace() for ch in input_message): 
    st.error("Please type only spaces and/or UPPER CASE letters")
else:
    # Create a new Enigma machine for each message
    rotors = [Rotor(rotor[1], rotor[2], pos) for rotor, pos in zip(selected_rotors, initial_positions)]
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])
    
    enigma = Enigma(rotors, reflector, plugboard)
    
    # Process the message
    translated_message = enigma.process(input_message)
    
    st.text_area('Output:', value=translated_message, height=210)

# st.write(f"Current rotor positions: {''.join(initial_positions)}")

# Add a button to reset the rotor positions
# if st.button('Reset Rotor Positions'):
#     initial_positions = ['A', 'M', 'T']
#     if use_rotor_iv:
#         initial_positions.append('A')
#     if use_rotor_v:
#         initial_positions.append('A')
#     st.experimental_rerun()