
from explorer.models import OperationalUnit, Oilfield, Well
from rest_framework import viewsets
from rest_framework.decorators import api_view
from explorer.services import process_data_challenge1, process_data_challenge2

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

    result = process_data_challenge1(opunits, oilfields, wells)

    return Response(result)

@api_view(["GET"])
def challenge2(request):
    """
    Endpoint que permite listar os dados formatados da forma solicitada
    """
    opunits = OperationalUnit.objects.all()
    oilfields = Oilfield.objects.all()
    wells = Well.objects.all()

    result = process_data_challenge2(opunits, oilfields, wells)

    return Response(result)

