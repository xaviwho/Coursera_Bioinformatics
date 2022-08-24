ham_str1 = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
ham_str2 = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

def h_loop(str1, str2):
    h_distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            h_distance += 1
    return h_distance

print(h_loop(ham_str1,ham_str2))

