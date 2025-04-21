# Project Finite Automata and Rational Expressions

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Automata](https://img.shields.io/badge/Théorie_des_Langages-Formal_Languages-239120)
![License](https://img.shields.io/badge/Licence-MIT-blue.svg)

## 📝 Description

Finite automata manipulation project with capabilities for:

- Verification of properties (determinism, standardisation, completeness)

- Transformation between different normal forms
  
- Recognition of rational languages

## 🎯 Main objectives

- Read and display a PLC from a file.
  
- Check that the PLC is deterministic, standard and complete.
  
- Standardise an automaton if necessary.
  
- Determine and complete a non-deterministic automaton.
  
- Construct an equivalent minimal automaton.
  
- Test word recognition.
  
- Generate an automaton accepting the complementary language.
  
- Structure of the Project
  
1. Automata handling
   
automate.py: Definition of the Automata class and methods for handling automata.

main.py: Main interface for interacting with the program.

test_fonction.py: Automated test script for automata.

2. Data folders
   
dossier_automate/: Contains the .txt files of the PLCs to be processed.

dossier_trace/: Stores the results of PLC executions and transformations.

## Implemented functions

Reading and displaying a PLC in the form of a transition table.

Checking and transforming automata:

Detection and correction of non-standard automata.

Determining and completing automata.

Minimisation of a complete deterministic automaton.

Word recognition by the automaton.

Generation of the complementary automaton.


