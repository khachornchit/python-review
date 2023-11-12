# Regular Expression

```
.       Matches any single character (EG: "at" matches cat, hat, sat)
[]      Matches a single character contained in the brackets (EG: "[ch]at" matches cat, hat but not sat)
[^ ]    Matches a single character NOT contained in the bracket (EG: "[^c]at" matches hat, sat, but not cat)
^       Matches the expression if at the start of the string (EG: "^.at" matches cat, hat, sat if located at the start of the string)
$       Same as ^ but matching at the end of string instead
()      Contains sub expresions such as bodmas/bomdas
*       Matches the preceding element zero or more times (EG: "c.*" matches any word starting with c such as cat, coat, class)
```

# Option Flags
re.I    Ignore case matching
re.M    Make $ match the end of a line and ^ the start of a line
re.S    Make . (dot) match any character even the new line character
re.U    Interprets in Unicode
re.X    Ignores whitespace within the pattern
