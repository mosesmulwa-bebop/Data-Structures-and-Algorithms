# Description of the caesar cypher

This is a simple cryptography algorithm used to encrypt and decrypt 
text.
Encryption: <br>
Shift each letter some places to the right. E.g, if the shift chosen is 3,
A becomes D, B becomes E and so on.
The final letters X,Y and Z wrap around the alphabet. That is, X becomes A , 
Y becomes B e.t.c

Decryption: <br>
Shift each letter to the left. D becomes A e.t.c

### Implementation in python
Notation: <br>
i = current element
r = shift

We can use the implementation (i+r) mod 26 for encryption
and (i-r) mod 26 for decryption

Here, we have a list of letters, A-Z , with A being indexed 0, B 1 e.t.c

E.g to shift A to D (assuming shift of 3) <br>
Current index - 0, r = 3    <br>
(0+3) mod 26 = 3 , thus we display index 3 which is D

The same can be achieved when decrypting.

In python, the command ord('A') gives the integer unicode form of A <br>
The command chr(c) gives the character string of integer c

To create a list with all our alphabets in order.
We can use the command ord(k) - ord('A'). <br>
Here k is our current character. E.g if our current character is B <br>
Then it will be ord('B') - ord('A') which is 1.

We can use this integer to undo our command by writing chr( integer + ord('A'))<br>
e.g for 1, chr(1+ord('A')) which is B.

### Creating the class
To save on time on encrypting and decrypting, we can create an encoded and decoded list 
and simply match the indexes. Let's see it in practice, <br>
encoded = ['D', 'E', 'F', 'G'......] <br>
decoded = ['A', 'B', 'C', 'D'......] <br>

E.g to encode A, we get its index (0 in this case), check index 0 in the encoded
list, which is D and then replace A with D.

Recall, the encoded list was creating using the chr and ord commands described above.







