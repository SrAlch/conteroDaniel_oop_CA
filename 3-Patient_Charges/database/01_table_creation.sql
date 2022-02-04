CREATE TABLE IF NOT EXISTS [patient](
    [patient_id] INT(11) NOT NULL,
    [first_name] VARCHAR(20) NOT NULL,
    [mid_name] VARCHAR(20),
    [last_name] VARCHAR(20) NOT NULL,
    [patient_address] VARCHAR(100) NOT NULL,
    [patient_city] VARCHAR(50) NOT NULL,
    [zip_code] VARCHAR(10) NOT NULL,
    [phone_number] VARCHAR(30) NOT NULL,
    [emrg_name] VARCHAR(20) NOT NULL,
    [ermg_phone] VARCHAR(30) NOT NULL,
    PRIMARY KEY ([patient_id])
);

CREATE TABLE IF NOT EXISTS [doctor](
    [doctor_id] INT(11) NOT NULL,
    [doctor_name] VARCHAR(20) NOT NULL,
    [last_name] VARCHAR(20) NOT NULL,
    [work_phone] VARCHAR(30) NOT NULL,
    PRIMARY KEY ([doctor_id])
);

CREATE TABLE IF NOT EXISTS [procedure](
    [procedure_name] VARCHAR(40) UNIQUE NOT NULL,
    [procedure_fee] MONEY NOT NULL,
    PRIMARY KEY ([procedure_name])
);

CREATE TABLE IF NOT EXISTS [appointment](
    [apointment_id] INT(11) NOT NULL,
    [patient_id]  INT NOT NULL,
    [doctor_id] INT NOT NULL,
    [date] DATE NOT NULL,
    [procedure_name] NVARCHAR(40) NOT NULL,
    PRIMARY KEY ([apointment_id]),
    FOREIGN KEY ([patient_id]) REFERENCES patient([patient_id]),
    FOREIGN KEY ([doctor_id]) REFERENCES doctor([doctor_id]),
    FOREIGN KEY ([procedure_name]) REFERENCES [procedure]([procedure_name])
)