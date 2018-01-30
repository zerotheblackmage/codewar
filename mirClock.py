# https://www.codewars.com/kata/clock-in-mirror/train/python

def what_is_the_time(time_in_mirror):
    t = time_in_mirror.split(':')
    range = 60 * 12
    t[0] = int(t[0]) * 60
    t[1] = int(t[1])
    cur_time = sum(t)
    res_time = range - cur_time
    conv_hou = res_time / 60
    conv_min = res_time - (60 * conv_hou)
    
    if len(str(conv_min)) == 1:
         conv_min = "0" + str(conv_min)
    if len(str(conv_hou)) == 1:
        conv_hou = "0" + str(conv_hou)
        
    conv_time = str(conv_hou) + ":" + str(conv_min)
 
    if conv_time[:2] == "00":
        conv_time = "12" + conv_time[-3:]
    if conv_time[:2] == "-1":
        conv_time = "11" + conv_time[-3:]
    return conv_time

