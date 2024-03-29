# Vigen-re-cipher---encrypting-ex2

method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution

The idea behind the Vigenère cipher, like all other polyalphabetic ciphers, is to disguise the plaintext letter frequency to interfere with a straightforward application of frequency analysis. For instance, if P is the most frequent letter in a ciphertext whose plaintext is in English, one might suspect that P corresponds to e since e is the most frequently used letter in English. However, by using the Vigenère cipher, e can be enciphered as different ciphertext letters at different points in the message, which defeats simple frequency analysis.

The primary weakness of the Vigenère cipher is the repeating nature of its key. If a cryptanalyst correctly guesses the key's length n, the cipher text can be treated as n interleaved Caesar ciphers, which can easily be broken individually. The key length may be discovered by brute force testing each possible value of n, or Kasiski examination and the Friedman test can help to determine the key length (see below: § Kasiski examination and § Friedman test).

In 1863, Friedrich Kasiski was the first to publish a successful general attack on the Vigenère cipher.[17] Earlier attacks relied on knowledge of the plaintext or the use of a recognizable word as a key. Kasiski's method had no such dependencies. Although Kasiski was the first to publish an account of the attack, it is clear that others had been aware of it. In 1854, Charles Babbage was goaded into breaking the Vigenère cipher when John Hall Brock Thwaites submitted a "new" cipher to the Journal of the Society of the Arts.[18][19] When Babbage showed that Thwaites' cipher was essentially just another recreation of the Vigenère cipher, Thwaites presented a challenge to Babbage: given an original text (from Shakespeare's The Tempest : Act 1, Scene 2) and its enciphered version, he was to find the key words that Thwaites had used to encipher the original text. Babbage soon found the key words: "two" and "combined". Babbage then enciphered the same passage from Shakespeare using different key words and challenged Thwaites to find Babbage's key words.[20] Babbage never explained the method that he used. Studies of Babbage's notes reveal that he had used the method later published by Kasiski and suggest that he had been using the method as early as 1846.[21]

The Kasiski examination, also called the Kasiski test, takes advantage of the fact that repeated words are, by chance, sometimes encrypted using the same key letters, leading to repeated groups in the ciphertext. For example, consider the following encryption using the keyword ABCD:

Key:        ABCDABCDABCDABCDABCDABCDABCD
Plaintext:  cryptoisshortforcryptography
Ciphertext: CSASTPKVSIQUTGQUCSASTPIUAQJB
There is an easily noticed repetition in the ciphertext, and so the Kasiski test will be effective.

The distance between the repetitions of CSASTP is 16. If it is assumed that the repeated segments represent the same plaintext segments, that implies that the key is 16, 8, 4, 2, or 1 characters long. (All factors of the distance are possible key lengths; a key of length one is just a simple Caesar cipher, and its cryptanalysis is much easier.) Since key lengths 2 and 1 are unrealistically short, one needs to try only lengths 16, 8 or 4. Longer messages make the test more accurate because they usually contain more repeated ciphertext segments. The following ciphertext has two segments that are repeated:

Ciphertext: VHVSSPQUCEMRVBVBBBVHVSURQGIBDUGRNICJQUCERVUAXSSR
The distance between the repetitions of VHVS is 18. If it is assumed that the repeated segments represent the same plaintext segments, that implies that the key is 18, 9, 6, 3, 2 or 1 character long. The distance between the repetitions of QUCE is 30 characters. That means that the key length could be 30, 15, 10, 6, 5, 3, 2 or 1 character long. By taking the intersection of those sets, one could safely conclude that the most likely key length is 6 since 3, 2, and 1 are unrealistically short.   
   
   
