## Word map
This python program takes ASCII map as a cli input and outputs the letters and the path that algorithm travelled into stdout:
~~~txt
Input:
- ASCII map: starts with @ , ends with x , contains: -, +, | and letters
Output:
- Collected letters
- Path as characters
~~~
#### Example
~~~txt
Input:
 @---A---+
 |
 x-B-+ C
 | |
 +---+
Expected output:
Letters ACB
Path as characters @---A---+|C|+---+|+-B-x
~~~
