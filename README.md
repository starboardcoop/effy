# effy
An app for calculating remuneration based on effort and personal sacrifice.

## Proposed usage

The user of **effy** should have a `data.yml` file, which includes people's names and their "standing," which is essentially their seniority. A record at the top of the file determines the multiplier for each standing level.

```
standings:
  - name: apprentice
    rate: 0.5
  - name: member
    rate: 0.75
  - name: mega-member
    rate: 1.0
people:
  - name: Jane
    standing: member
  - name: Jack
    standing: apprentice
  - name: Jesús
    standing: mega-member
```

With the data ready, run `effy calc`. **effy** will then ask for a name and this person's individual effort ratings:

```
~> People: Jane | Jack | Jesús
~> Please enter a person's name and their effort ratings, separated by spaces.
~> Add a comma to the end of each line to continue.

<~ Jane 70 75 75,
<~ Jack 85 90 80,
<~ Jesús 80 80 75

~> Jane       -> 31%
~> Jack       -> 24%
~> Jesús      -> 44%
~> Remainder  -> 1%
```
