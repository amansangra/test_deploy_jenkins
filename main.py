import cleantext

if __name__ == '__main__':
    c_text = cleantext.clean('This is A s$ample !!!!tExt3% to  cleaN566556+2+59*/133', extra_spaces=True,
                             lowercase=True,
                             numbers=True, punct=True)
    print(c_text)
    print("THIS IS MASTER")
