class Transaction:
    def __init__(self, id, mcc, merchant_name, reference_text, category):
        self.id = id
        self.mcc = mcc
        self.merchant_name = merchant_name
        self.reference_text = reference_text
        self.category = category


def transaction_from_json(jsonObject):
    mcc = 0
    merchant_name = ""
    reference_text = ""
    category = ""

    try:
        if type(jsonObject['mcc']) is int:
            mcc = jsonObject['mcc']
    except:
        print("No MCC")

    try:
        if type(jsonObject['merchantName']) is str:
            merchant_name = jsonObject['merchantName']
    except:
        print("no merchant name")

    try:
        if type(jsonObject['referenceText']) is str:
            reference_text = jsonObject['referenceText']
    except:
        print("No reference text")

    try:
        if type(jsonObject['category']) is str:
            category = jsonObject['category']
    except:
        print("No category")

    return Transaction(
        jsonObject['id'],
        mcc,
        merchant_name,
        reference_text,
        category
    )
