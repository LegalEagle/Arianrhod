'''

ForceInline ULONG HashAPI(PCChar pszName)
{
    ULONG Hash = 0;

    while (*(PByte)pszName)
    {
        Hash = _rotl(Hash, 0x0D) ^ *(PByte)pszName++;
    }

    return Hash;
}


'''


def rol32(val, shift):
    val &= 0xFFFFFFFF
    return (val << shift) | (val >> (32 - shift))

def HashAPI(str):
    hash = 0
    for ch in str:
        hash = rol32(hash, 0xD) ^ ord(ch)

    return hash & 0xFFFFFFFF
