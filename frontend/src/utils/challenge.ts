import { DataNode } from "antd/es/tree";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";

/**
 * Função que processa os dados para o formato solicitado
 */
export function processData(
  opunits: OperationalUnitType[],
  oilfields: OilfieldType[],
  wells: WellType[]
) {
  console.log("processData", {
    opunits,
    oilfields,
    wells,
  });

  return [] as DataNode[];
}
