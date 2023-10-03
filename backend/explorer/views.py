from explorer.models import OperationalUnit, Oilfield, Well
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.response import Response
from explorer.serializers import (
    OilfieldSerializer,
    OperationalUnitSerializer,
    WellSerializer,
)


class OperationalUnitViewSet(viewsets.ModelViewSet):
    """
    Endpoints que permitem listar e editar unidade operacionais(operational units)
    """

    queryset = OperationalUnit.objects.all().order_by("id")
    serializer_class = OperationalUnitSerializer
    permission_classes = []


class OilfieldViewSet(viewsets.ModelViewSet):
    """
    Endpoints que permitem listar e editar campos(oilfields)
    """

    queryset = Oilfield.objects.all()
    serializer_class = OilfieldSerializer
    permission_classes = []


class WellViewSet(viewsets.ModelViewSet):
    """
    Endpoints que permitem listar e editar poços(wells)
    """

    queryset = Well.objects.all()
    serializer_class = WellSerializer
    permission_classes = []


@api_view(["GET"])
def challenge1(request):
    """
    Endpoint que permite listar os dados formatados da forma solicitada
    """
    opunits = OperationalUnit.objects.all()
    oilfields = Oilfield.objects.all()
    wells = Well.objects.all()

    # TODO: Aqui você tera que juntar os dados da forma solicitada.
    # O resultado será um array contendo os ids das entidades nesse formato: <tipo>/<id>, exemplo:
    # Unidade operacional: {"id": 1, "name": "Unidade 1"} -> [['opunit/1']]
    # (para unidade operacional vamos usar o nome opunit por ser mais curto)
    # Para cada nível que for entrando tem que inserir os identificadores dos níveis acima, exemplo:
    # Campo: {"id": 1, "name": "Campo 1", "operational_unit": "1"} -> [['opunit/1'], ['oilfield/1']]
    # Poço: {"id": 1, "name": "Poço 1", "oilfield": "1"} -> [['opunit/1'], ['oilfield/1'], ['well/1']].
    # Mais alguns exemplos abaixo:

    # opunits = [
    #     {"id": 1, "name": "Unidade 1"},
    #     {"id": 2, "name": "Unidade 2"},
    # ]
    # Resultado até o momento: [[["opunit/1"]],[["opunit/2"]]]

    # oilfields = [
    #     {"id": 1, "name": "Campo 1", "operational_unit": "1"},
    #     {"id": 1, "name": "Campo 2", "operational_unit": "1"},
    #     {"id": 3, "name": "Campo 3", "operational_unit": "2"},
    # ]
    # Resultado até o momento: [[["opunit/1"]],[["opunit/2"]],[["opunit/1"],["oilfield/1"]],[["opunit/1"],["oilfield/1"]],[["opunit/2"],["oilfield/3"]]]

    # wells = [
    #     {"id": 1, "name": "Poço 1", "oilfield": "1"},
    #     {"id": 2, "name": "Poço 2", "oilfield": "3"},
    #     {"id": 3, "name": "Poço 3", "oilfield": "3"},
    # ]

    # result = process_data(opunits, oilfields, wells)

    # O resultado pra esse caso seria:
    # [[["opunit/1"]],[["opunit/2"]],[["opunit/1"],["oilfield/1"]],[["opunit/1"],["oilfield/1"]],[["opunit/2"],["oilfield/3"]],[["opunit/1"],["oilfield/1"],["well/1"]],[["opunit/2"],["oilfield/3"],["well/2"]],[["opunit/2"],["oilfield/3"],["well/3"]]]

    result = process_data_challenge1(opunits, oilfields, wells)

    return Response(result)


def process_data_challenge1(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """
    # TODO: Escreva seu código aqui
    return []


@api_view(["GET"])
def challenge2(request):
    """
    Endpoint que permite listar os dados formatados da forma solicitada
    """
    opunits = OperationalUnit.objects.all()
    oilfields = Oilfield.objects.all()
    wells = Well.objects.all()

    # TODO: Nesse desafio você deve retornar os dados em uma estrutura de dados seguindo esse padrão:
    # result = [
    #     {
    #         "id": 1,
    #         "name": "Unidade operacional 1",
    #         "children": [
    #             {
    #                 "id": 4,
    #                 "name": "Campo 1",
    #                 "children": [
    #                     {"id": 6, "name": "Poço 1"},
    #                     {"id": 7, "name": "Poço 2"},
    #                 ],
    #             }
    #         ],
    #     },
    #     {
    #         "id": 2,
    #         "name": "Unidade operacional 2",
    #     },
    #     {
    #         "id": 3,
    #         "name": "Unidade operacional 3",
    #         "children": [
    #             {
    #                 "id": 5,
    #                 "name": "Campo 2",
    #             }
    #         ],
    #     },
    # ]

    # Onde os nós ficam dentro da chave children dos seus pais

    result = process_data_challenge2(opunits, oilfields, wells)

    return Response(result)


def process_data_challenge2(opunits, oilfields, wells):
    """
    Função que processa os dados para estrutura solicitada
    """
    # TODO: Escreva seu código aqui
    return []
