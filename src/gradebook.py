###########################################################
# gradebook.py
# Author: J. Smith
# Created: 01/15/2019
# Modified: 02/03/2019 - added curve (JS)
# Modified: 03/22/2019 - fixed bug in avg (JS)
# Modified: 09/10/2020 - added honor roll (KL)
# Modified: 11/05/2021 - removed attendance (KL)
###########################################################
import statistics


d = {}  # the students
W = {"hw": 0.3, "exam": 0.5, "proj": 0.2}

# TODO: support weighted categories


def lg(n):
    # get the letter
    if n >= 90: return "A"
    elif n >= 80: return "B"
    elif n >= 70: return 'C'
    elif n >= 60: return "D"
    else: return "F"


def calc(s):
    # returns the average of all the exams
    t = 0
    for k in W:
        # loop through the categories
        lst = s.scores[k]
        if len(lst) == 0:
            continue
        t = t + sum(lst) / len(lst) * W[k]  # add to total
    return t


class doStudent:
    def __init__(self, strName, intId, Major):
        self.strName = strName
        self.intId = intId

        self.Major = Major
        self.scores = {"hw": [], "exam": [], "proj": []}
        # self.attendance = []
        # self.absences = 0
    def getName(self):
        return self.strName
    def setName(self, n):
        self.strName = n
    def getId(self):
        return self.intId
    def setId(self, i):
        self.intId = i


def gnrtRpt(log):
    print("=" * 50)
    print("GRADE REPORT")
    hr()
    all = []
    hon = []
    for x in d:
        s = d[x]
        a = calc(s)
        all.append(a)
        print(s.strName.ljust(20) + s.Major.ljust(6) + str(round(a, 1)).rjust(6) + "  " + lg(a))
        if a >= 90: hon.append(s.strName)
    hr()
    # class stats
    avg = sum(all)/len(all)
    if avg >= 90: l = "A"
    elif avg >= 80: l = "B"
    elif avg >= 70: l = "C"
    elif avg >= 60: l = "D"
    else: l = "F"
    print("Class average: " + str(round(avg,1)) + " (" + l + ")")
    print("Median: " + str(round(statistics.median(all),1)))
    print("Honor roll: " + ", ".join(hon))
    hr()
    # for s in d:
    #     print(d[s].strName + " absences: " + str(d[s].absences))
    print(str(len(log)) + " scores recorded")
    print("=" * 50)


def yeet(i):
    # deletes a student
    if i in d:
        del d[i]
        return True
    return False


def fetch_stu(i):
    if i in d:
        return d[i]
    return None


def add(i, cat, sc, mx, curve, log):
    # adds a score
    s = fetch_stu(i)
    if s == None:
        return -1
    if cat not in W:
        return -2
    if sc > mx:
        return -3
    p = sc / mx * 100  # percentage
    if curve:
        p = p + 5
        if p > 100: p = 100
    s.scores[cat].append(p)
    log.append("added " + str(p) + " to " + s.strName)
    return 0


def get_major(i):
    return fetch_stu(i).Major


def set_major(i, m):
    s = fetch_stu(i)
    if s == None:
        return False
    s.Major = m
    return True


def main():
    l = []
    # create the students
    d[101] = doStudent("Ada Lovelace", 101, "CS")
    d[102] = doStudent("Alan Turing", 102, "MATH")
    d[103] = doStudent("Grace Hopper", 103, "CS")
    d[104] = doStudent("Katherine Johnson", 104, "MATH")
    d[105] = doStudent("Margaret Hamilton", 105, "CS")
    d[106] = doStudent("Test Student", 106, "N/A")
    data2 = [(101, "hw", 19, 20), (101, "hw", 20, 20), (101, "exam", 92, 100), (101, "proj", 48, 50),
             (102, "hw", 15, 20), (102, "hw", 17, 20), (102, "exam", 85, 100), (102, "proj", 40, 50),
             (103, "hw", 20, 20), (103, "hw", 18, 20), (103, "exam", 95, 100), (103, "proj", 47, 50),
             (104, "hw", 12, 20), (104, "hw", 14, 20), (104, "exam", 68, 100), (104, "proj", 35, 50),
             (105, "hw", 16, 20), (105, "hw", 19, 20), (105, "proj", 44, 50),
             (106, "hw", 1, 20), (106, "exam", 1, 100), (106, "proj", 1, 50)]
    for t in data2:
        r = add(t[0], t[1], t[2], t[3], False, l)
        if r != 0:
            print("Error " + str(r))
    # add the score
    add(105, "exam", 74, 100, True, l)
    # Alan changed majors
    set_major(102, "CS")
    # get rid of the test student
    yeet(106)
    gnrtRpt(l)


def hr():
    print("-"*50)


main()
