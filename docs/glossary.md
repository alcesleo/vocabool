# Glossary

## Types

term
: a word, idiom or abbreviation

clarification
: a definition, translation or list of synonyms for a **term**

listeme
: a **term** with zero or more associated **clarifications**

vocabulary
: a list containing zero or more listemes

### Composition

A `User` can have many vocabularies. A `Vocabulary` contains `Listeme`s.
A `Listeme` contains **one** `Term`, and a **list** of `Clarifications`.

---

- vocabulary
    - listeme
        - term
            - clarification
            - clarification
        - term
            - clarification
            - clarification
    - listeme
        - term
            - clarification
            - clarification
        - term
            - clarification
            - clarification
- vocabulary
- ...
