DDL_QUERY_SUPER = '''

CREATE TABLE Ubicacion (
	ID_Ubicacion int auto_increment,
    Codigo_postal int,
    Pais varchar(128),
    Estado varchar(128),
    Ciudad varchar(128),
    CONSTRAINT ID_UbicacionPK PRIMARY KEY (ID_Ubicacion)
);


CREATE TABLE Cliente (
    Id_cliente varchar(20) unique,
    Nombre varchar(128),
    Segmento varchar(128),
    CONSTRAINT Id_clientePK PRIMARY KEY (Id_cliente)
);

CREATE TABLE Producto (
	ID_Product int auto_increment,
	Id_producto text,
    Categoria text,
    Subcategoria text,
    Nombre text,
    CONSTRAINT Id_productoPK PRIMARY KEY (ID_Product)
);

CREATE TABLE Fechas_orden(
	date_key int,
	full_date datetime,
    day_of_week int,
    day_num_in_month int,
    day_name varchar(50),
    weekday_flag varchar(50),
    month_name varchar(50),
    month_abbrev varchar(50),
	_year int,
    CONSTRAINT Id_dateordenPK PRIMARY KEY (date_key)
);

CREATE TABLE Fact_super (
sk_super_fact int auto_increment,
Id_orden varchar(14),
Fecha_orden int,
Id_ubicacion int,
Id_cliente varchar(20),
Id_producto int, 
Venta float,
Cantidad int,
Descuento float,
Ganancia float,
CONSTRAINT Id_ventaPK PRIMARY KEY (sk_super_fact)
);

ALTER TABLE Fact_super ADD CONSTRAINT fact_Fechas_orden
    FOREIGN KEY (Fecha_orden)
    REFERENCES Fechas_orden (date_key);
    
ALTER TABLE Fact_super ADD CONSTRAINT fact_Ubicacion
    FOREIGN KEY (Id_ubicacion)
    REFERENCES Ubicacion (ID_Ubicacion);
    
ALTER TABLE Fact_super ADD CONSTRAINT fact_cliente
    FOREIGN KEY (Id_cliente)
    REFERENCES Cliente (Id_cliente);
    
ALTER TABLE Fact_super ADD CONSTRAINT fact_producto
    FOREIGN KEY (Id_producto)
    REFERENCES Producto (ID_Product);
 '''