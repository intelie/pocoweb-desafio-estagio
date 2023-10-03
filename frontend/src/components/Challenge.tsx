import { request } from "../utils/http";
import { OperationalUnitType, OilfieldType, WellType } from "../@types/domain";
import { useEffect, useState } from "react";

import { Col, Row, Tree } from "antd";
import { DataNode } from "antd/es/tree";

const API_HOST = import.meta.env.VITE_API_HOST;

export default function Challenge() {
  const [processedData, setProcessedData] = useState<DataNode[]>([]);
  useEffect(() => {
    async function getData() {
      /**
       * Aqui você tem todas as informações necessárias para agrupar os dados.
       * Lembrando que unidade operacional é pai de campo e campo é pai de poço.
       */
      const opunits = await request<OperationalUnitType[]>(
        `${API_HOST}operational-units`
      );
      const oilfields = await request<OilfieldType[]>(`${API_HOST}oilfields`);
      const wells = await request<WellType[]>(`${API_HOST}wells`);

      console.log({ opunits, oilfields, wells });

      /** 
       * TODO: Você deve fazer uma lógica para processar os dados e deixá-los no formato esperado
       * pelo componente Tree. Vamos avaliar a forma com que você vai processar os dados.
       * Você deve usar o componente Tree para exibir a estrutura de dados
       * Documentação do componente utilizado: https://ant.design/components/tree

        * A hierarquia dos dados é essa: unidade operacional(operational unit) -> campo(oilfield) -> poço(well)
      */

      setProcessedData([]);
    }

    getData();
  }, []);

  return (
    <Row>
      <Col span={12} offset={6}>
        <Tree treeData={processedData} />
      </Col>
    </Row>
  );
}
