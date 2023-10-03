export type OperationalUnitType = {
  id: number;
  name: string;
};

export type OilfieldType = {
  id: number;
  name: string;
  operational_unit: string;
};

export type WellType = {
  id: number;
  name: string;
  oilfield: string;
};
