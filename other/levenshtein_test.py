import Levenshtein as L


def get_cer(asr_result, feature_text):
    print("\nasr_result:",asr_result, "\nfeature:   ",feature_text)
    distance = L.distance(asr_result, feature_text)
    cer = 100 *  distance/ len(feature_text)
    print("\ncer=" + str(distance) + "/" + str(len(feature_text)) + "=" + str(cer))

    return cer


def get_wer(asr_result, feature_text):
    print("\nasr_result:",asr_result, "\nfeature:   ",feature_text)
    delete_num, insert_num, replace_num = 0, 0, 0
    edittops_result = L.editops(asr_result, feature_text)
    for r in edittops_result:
        if "delete" in r:
            delete_num += 1
        if "insert" in r:
            insert_num += 1
        if "replace" in r:
            replace_num += 1
    print("\nWER = ( D + I + S ) / N")
    wer = 100 * (delete_num + insert_num + replace_num) / len(feature_text)
    print(
        "\nwer = ({}+{}+{})/{} = {}".format(
            delete_num, insert_num, replace_num, len(feature_text), wer
        )
    )

    return wer

class TestLevenshtein:
    def test_get_cer(self):
        get_cer("今天天气很好","你好今天天气很好")

    def test_get_wer(self):
        get_wer("hello","helloo")
