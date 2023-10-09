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
  console.log("processData", {opunits, oilfields, wells });

  let result: DataNode[] = []

  opunits.forEach(opunit => {
    let op: any = {key: opunit.id, title: opunit.name}
    let filteredFields = oilfields.filter(oilf => oilf.operational_unit == op.key)
    
    if(filteredFields.length > 0) { 
      let filds: any[] = []
      filteredFields.forEach((fld: any) => {
        let fild: any = {key: Math.random()*365, id: fld.id, title: fld.name}
        let filteredWells = wells.filter(wll => wll.oilfield == fild.id)
        
        if(filteredWells.length > 0) {
          let wllls: any[] = []
          filteredWells.forEach(flld => {
            let x = {key: Math.random()*365, title: flld.name}
            wllls.push(x)
          })
          fild.children = wllls
        }
        filds.push(fild)
      });
      op.children = filds
    }
    result.push(op)
  });

  return result as DataNode[];
}
