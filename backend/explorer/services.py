from explorer.serializers import (
    OilfieldSerializer,
    OperationalUnitSerializer,
    WellSerializer,
)
def process_data_challenge1(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """

    opunitsSerial = OperationalUnitSerializer(opunits, many=True)
    oilfieldsSerial = OilfieldSerializer(oilfields, many=True)
    wellsSerial = WellSerializer(wells, many=True)

    ops = opunitsSerial.data
    fields = oilfieldsSerial.data
    wellss = wellsSerial.data
    result = []
    opsResult = []
    fieldsResult = []
    wellsResult = []

    for wll in wellss:
        op = 0
        for f in fields:
            if f['id'] == wll["oilfield"]:
                op = f['id']
        wellsResult.append({"o": f'{op}', "f": f'{wll["oilfield"]}', "w": f'{wll["id"]}'})

    for fld in fields:
        fieldsResult.append({"o": f'{fld["operational_unit"]}', "f": f'{fld["id"]}'})

    for op in ops:
        opsResult.append({"o": f'{op["id"]}'})

    for oRes in opsResult:
        result.append([[f'opunit/{oRes["o"]}']])

    for fRes in fieldsResult:
        result.append([[f'opunit/{fRes["o"]}'], [f'oilfield/{fRes["f"]}']])

    for wRes in wellsResult:
        result.append([[f'opunit/{wRes["o"]}'], [f'oilfield/{wRes["f"]}'], [f'well/{wRes["w"]}']])


    return result

def process_data_challenge2(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """

    opunitsSerial = OperationalUnitSerializer(opunits, many=True)
    oilfieldsSerial = OilfieldSerializer(oilfields, many=True)
    wellsSerial = WellSerializer(wells, many=True)

    ops = opunitsSerial.data
    fields = oilfieldsSerial.data
    wellss = wellsSerial.data
    result = []


    for op in ops:
        row = {"id": f'{op["id"]}', "name": f'{op["name"]}'}
        childFild = []
        for fld in fields:
            if fld["operational_unit"] == op["id"]:
                fRow = {"id": f'{fld["id"]}', "name": f'{fld["name"]}'}
                childWell = []
                for wll in wellss:
                    if wll["oilfield"] == fld["id"]:
                        childWell.append({"id": f'{wll["id"]}', "name": f'{wll["name"]}'})
                if len(childWell) > 0:
                    fRow["children"] = childWell
                childFild.append(fRow)
        if len(childFild) > 0:
            row["children"] = childFild
        result.append(row)


    return result
