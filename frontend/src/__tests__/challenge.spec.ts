import { expect, test } from "vitest";
import { processData } from "../utils/challenge";
import { OilfieldType, OperationalUnitType, WellType } from "../@types/domain";
import { DataNode } from "antd/es/tree";

test("adds 1 + 2 to equal 3", () => {
  const opunits: OperationalUnitType[] = [];
  const oilfields: OilfieldType[] = [];
  const wells: WellType[] = [];

  const result: DataNode[] = [];
  expect(processData(opunits, oilfields, wells)).toEqual(result);
});
