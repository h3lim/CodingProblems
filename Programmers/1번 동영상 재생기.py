def solution(video_len, pos, op_start, op_end, commands):
    for i in commands:
        if 60 * int(op_start[:2]) + int(op_start[3:]) <= 60 * int(pos[:2]) + int(pos[3:]) <= 60 * int(
                op_end[:2]) + int(op_end[3:]):
            pos = op_end
        if i == "prev":
            tmp = 60 * int(pos[:2]) + int(pos[3:]) - 10
            if tmp < 0:
                pos = "00:00"
            else:
                tmp1, tmp2 = tmp // 60, tmp % 60
                if len(str(tmp1)) == 1:
                    pos = "0" + str(tmp1) + ":"
                else:
                    pos = str(tmp1) + ":"
                if len(str(tmp2)) == 1:
                    pos += "0" + str(tmp2)
                else:
                    pos += str(tmp2)
        elif i == "next":
            tmp = 60 * int(pos[:2]) + int(pos[3:]) + 10
            if tmp > 60 * int(video_len[:2]) + int(video_len[3:]):
                pos = video_len
            else:
                tmp1, tmp2 = tmp // 60, tmp % 60
                if len(str(tmp1)) == 1:
                    pos = "0" + str(tmp1) + ":"
                else:
                    pos = str(tmp1) + ":"
                if len(str(tmp2)) == 1:
                    pos += "0" + str(tmp2)
                else:
                    pos += str(tmp2)
    if 60 * int(op_start[:2]) + int(op_start[3:]) <= 60 * int(pos[:2]) + int(pos[3:]) <= 60 * int(
            op_end[:2]) + int(op_end[3:]):
        pos = op_end
    return pos