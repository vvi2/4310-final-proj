from collections import defaultdict
import json


def generateDays():
    days = defaultdict()
    total = 0
    for j in range(2004, 2041):
        days[j] = defaultdict()
        for i in range(1, 32):
            days[j]["Jan " + str(i)] = 0
        for i in range(1, 29):
            days[j]["Feb " + str(i)] = 0
        for i in range(1, 32):
            days[j]["Mar " + str(i)] = 0
        for i in range(1, 31):
            days[j]["Apr " + str(i)] = 0
        for i in range(1, 32):
            days[j]["May " + str(i)] = 0
        for i in range(1, 31):
            days[j]["Jun " + str(i)] = 0
        for i in range(1, 32):
            days[j]["Jul " + str(i)] = 0
        for i in range(1, 32):
            days[j]["Aug " + str(i)] = 0
        for i in range(1, 31):
            days[j]["Sep " + str(i)] = 0
        for i in range(1, 32):
            days[j]["Oct " + str(i)] = 0
        for i in range(1, 31):
            days[j]["Nov " + str(i)] = 0
        for i in range(1, 32):
            days[j]["Dec " + str(i)] = 0

        for i in days[j].keys():
            ex = [
                "Jan 1",
                "Jan 2",
                "Jan 3",
                "Jan 4",
                "Jan 5",
                "Jan 6",
            ]
            if j == 2004 and i in ex:
                continue
            # day = int(i.split(" ")[1])
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            days[j][i] = round(val, 4)

            total += 1

    return days


def generateDaysReverse():
    days = defaultdict()
    total = 0
    for j in range(2004, 2041):
        days[j] = defaultdict()
        for i in range(1, 32):
            if j == 2004 and i <= 7:
                val = i
            else:
                val = (total) * 1.0 / 365.24

                if val > 1:
                    val -= int(total / 365) * 1.0

                if val < 0:
                    val += 1

                val = round(val, 4)
            total += 1
            days[j][val] = "Jan " + str(i)
        for i in range(1, 29):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Feb " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Mar " + str(i)
        for i in range(1, 31):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Apr " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "May " + str(i)
        for i in range(1, 31):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Jun " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Jul " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Aug " + str(i)
        for i in range(1, 31):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Sep " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Oct " + str(i)
        for i in range(1, 31):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Nov " + str(i)
        for i in range(1, 32):
            val = (total) * 1.0 / 365.24

            if val > 1:
                val -= int(total / 365) * 1.0

            if val < 0:
                val += 1

            val = round(val, 4)
            total += 1
            days[j][val] = "Dec " + str(i)

        # for i in days[j].keys():
        #     ex = [
        #         "Jan 1",
        #         "Jan 2",
        #         "Jan 3",
        #         "Jan 4",
        #         "Jan 5",
        #         "Jan 6",
        #     ]
        #     if j == 2004 and i in ex:
        #         continue
        #     # day = int(i.split(" ")[1])
        #     val = (total) * 1.0 / 365.24

        #     if val > 1:
        #         val -= int(total / 365) * 1.0

        #     if val < 0:
        #         val += 1

        #     days[j][i] = round(val, 4)

        #     total += 1

    return days


if __name__ == "__main__":
    json.dump(generateDays(), open("static/data/days.json", "w"))
    json.dump(generateDaysReverse(), open("static/data/daysReverse.json", "w"))
