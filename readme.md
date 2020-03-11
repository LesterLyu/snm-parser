## SNM Grammar Specification

### Install [Lark](https://github.com/lark-parser/lark)
```
$ pip install lark-parser
```

### Operator Precedence (High to Low)
- `+`, `-` Unary plus and minus
  - `-1`
  - `--+100` -> `100`
  - `++++100` -> `100`
  - `---100` -> `-100`
- `in` -> list operation
  - `"abc" in ["abc", "def"]` -> `true`
  - `1 in [1, 2, 3,]` -> `true`
  - `[1, 2] in [1, 2, 4, 6]` -> `true`
  - `[0, 2] in [1, 2, 3]` -> `false`
  - `!1 in [true, false]` -> `false`
    - `1 in [true, false]` is evaluated first!
- `!` Logical not
  - `!false` -> `true`
  - `!100` -> `false`
  - `!0` -> `true`
- `*`, `/`, `%` Multiplication, division, and remainder
- `+`, `-` Addition and subtraction
- `<`, `<=`, `>`, `>=`	Relational operators <, ≤, >, ≥
- `==`, `!=` Relational = and ≠ respectively
- `&&` Logical AND
- `||` Logical OR

### Data Types
- String: `"string"`
- Number: `123`, `-123`
- Boolean: `true`, `false`
- Array: `[1, 3, "hello", [123, 456], true, false]`
  - An array can contain any data types
- Field: 
  - e.g. `age`, `AGE`, `age_01`, `i_am_a_field`
  - Field name should contain only numbers, letters and underline _
  - **No special characters** are allowed :point_left:
