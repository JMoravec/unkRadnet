PRAGMA foreign_keys = ON;

CREATE TABLE AlphaEfficiency(
	AlphaCoeffID INTEGER PRIMARY KEY, 
	Coefficient FLOAT
);

CREATE TABLE BetaEfficiency(
	BetaCoeffID INTEGER PRIMARY KEY, 
	Coefficient FLOAT
);

CREATE TABLE Filter(
	FilterID INTEGER PRIMARY KEY, 
	FilterNum INTEGER UNIQUE, 
	StartDate DATETIME, 
	EndDate DATETIME, 
	SampleTime FLOAT,
	SampleVolume FLOAT,
	TimeStart FLOAT,
	AlphaCoeffID INTEGER,
	BetaCoeffID INTEGER,
	FOREIGN KEY(AlphaCoeffID) REFERENCES AlphaEfficiency(ID), 
	FOREIGN KEY(BetaCoeffID) REFERENCES BetaEfficiency(BetaCoeffID)
);

CREATE TABLE RawData(
	RawDataID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	Time INTEGER, 
	AlphaReading FLOAT, 
	BetaReading FLOAT,
	CleanFilterCount FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE Activity(
	ActivityID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	RawDataID INTEGER,
	DeltaT FLOAT, 
	AlphaAct FLOAT, 
	BetaAct FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID), 
	FOREIGN KEY(RawDataID) REFERENCES RawData(RawDataID)
);

CREATE TABLE AlphaCurve(
	AlphaCurveID INTEGER PRIMARY KEY,
	FilterID INTEGER,
	Alpha1 FLOAT,
	Alpha1Lambda FLOAT,
	Alpha2 FLOAT,
	Alpha2Lambda FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE BetaCurve(
	BetaCurveID INTEGER PRIMARY KEY,
	FilterID INTEGER,
	Beta1 FLOAT,
	Beta1Lambda FLOAT,
	Beta2 FLOAT,
	Beta2Lambda FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

