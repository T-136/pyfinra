import pandas as pd
import json

oldEmptyData = 5

# def subLevelToRealKey(dict):

def toDataframe(IncomeStatement):
    data = {}

    lableList = []
    if "datum" in IncomeStatement.keys():
        data.update({IncomeStatement["label"]: IncomeStatement["datum"][oldEmptyData:]})
        lableList.append(IncomeStatement["label"])

    for key in IncomeStatement.keys():

        if isinstance(IncomeStatement[key], dict):
            df_temp, lableListTemp = toDataframe(IncomeStatement[key])
            data.update(df_temp)
            lableList.append(lableListTemp)
        elif key == "subLevel":
            for value in IncomeStatement[key]:
                # print(value)
                df_temp, lableListTemp = toDataframe(value)
                data.update(df_temp)
                lableList.append(lableListTemp)

    return data, lableList

def levels(l, depth = -1):
    if not isinstance(l, list):
        yield (depth)
    else:
        for sublist in l:
            yield from levels(sublist, depth + 1)




def finStatementsDictToDf(dict):
    rows = dict["rows"]
    # firstSublevel = list(rows)[4]
    IncomeStatement = rows[0]
    data, x =toDataframe(IncomeStatement)

    indntList = list(levels(x))

    df = pd.DataFrame(index=dict["columnDefs"][oldEmptyData:], data=data)
    df_transposed = df.transpose()
    df_transposed['indent']=pd.Series(indntList, index=df_transposed.index)
    df_transposed.reset_index(inplace=True)
    df_transposed.rename(columns={"index": "name"}, inplace=True)
    df_transposed.set_index(['indent', 'name'], inplace=True)
    return df_transposed




if __name__ == "__main__":
    
    with open("finIncStatement.json", "r") as file:     
        contents = file.read()

    dictionary = json.loads(contents)
    finStatementsDictToDf(dictionary)

