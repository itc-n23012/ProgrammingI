vote_box = []
label = "票"


def vote():
    print("投票します")
    vote_box.append(label)


def reset_box():
    print("箱を空にします")
    vote_box.clear()


def check_box():
    print("票の数は{}です".format(len(vote_box)), end=" ")
