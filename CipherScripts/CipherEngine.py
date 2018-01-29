#Place Holder Script for Cipher engine

import Caesar
import Vigenere

def main():
    baseAlpha = "abcdefghijklmnopqrstuvwxyz"
    cryptText = "klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"
    decodeKey = "sskkuullll"
    Vigenere.main(baseAlpha, decodeKey, cryptText)
    return True

if __name__ == "__main__":
    main()
