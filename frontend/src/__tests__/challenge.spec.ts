import { expect, test } from "vitest";
import { processData } from "../utils/challenge";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";
import { DataNode } from "antd/es/tree";

test(">>>>Change this name", () => {
  const opunits: OperationalUnitType[] = [];
  const oilfields: OilfieldType[] = [];
  const wells: WellType[] = [];

  const result: DataNode[] = [];
  expect(processData(opunits, oilfields, wells)).toEqual(result);
});
