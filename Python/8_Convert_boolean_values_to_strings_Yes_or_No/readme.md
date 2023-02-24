## Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

## Варианты

```
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
```

```
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
```
