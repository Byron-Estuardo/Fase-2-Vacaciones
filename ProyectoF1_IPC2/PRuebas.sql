create database xd;
use xd;
create table ClienteIndividual(
 IdClienteIn Int not null auto_increment,
 CUI bigint not null unique,
 NIT bigint not null,
 PNombre varchar(100) not null,
 SNombre varchar(100),
 PApellido varchar(100) not null,
 SApellido varchar(100),
 FNacimiento date not null,
 CorreoE varchar(100) not null,
 NTelefonico INT,
 tipo_usuario varchar(20) not null,
 primary key (IdClienteIn)
 );

 create table ClienteEmpresarial(
 IdClienteEm Int not null primary key auto_increment,
 CUIRL BIGINT not null unique,
 NombreEmpresa varchar(50) not null,
 NombreComercial varchar(50) not null,
 PNombreRL varchar(50) not null,
 SNombreRL varchar(50),
 PApellidoRL varchar(50) not null,
 SApellidoRL varchar(50),
 Ubicacion varchar(300),
 NTelefonico INT,
 tipo_usuario varchar(12),
 Tipo_Empresa varchar(50)
 );

 create table Cliente(
 idCliente INT not null auto_increment,
 CodigoIngreso varchar(100) not null unique,
 ClaveA varchar(50) not null,
 tipo_usuario varchar(20) not null,
 IdClienteIn INT unique,
 IdClienteEm INT unique,
 PRIMARY KEY(idCliente, CodigoIngreso),
 foreign key(IdClienteIn) references ClienteIndividual(IdClienteIn),
 foreign key(IdClienteEm) references ClienteEmpresarial(IdClienteEm)
 );
alter table Cuenta auto_increment = 10000;

 create table Cuenta(
 CodigoCuenta bigint not null primary key auto_increment,
 Saldo float not null,
 Estado varchar(30) not null,
 TipoMoneda varchar(50) not null,
 TipoCuenta varchar(100) not null,
 PreAuto boolean not null,
 Interes varchar(50),
 Tiempo Int,
 idCliente Int not null,
 CodigoChe Int,
 foreign key(idCliente) references Cliente(idCliente)
 
 );
 alter table Cuenta auto_increment = 10000;
 alter table Cuenta modify PreAuto varchar(100);

create table Deposito(
 NoDeposito Int not null primary key auto_increment,
 monto bigint not null,
 Descripcion varchar(200),
 CodigoCuenta bigint,
 foreign key(CodigoCuenta) references Cuenta(CodigoCuenta)
);

create table Chequera(
 CodigoChe INT not null primary key	auto_increment,
 DispoCheque INT not null,
 CodigoCuenta bigint,
 foreign key(CodigoCuenta) references Cuenta(CodigoCuenta)
);

create table  cheque(
 Correlativo INT not null primary key,
 PNombre varchar(100) not null,
 SNombre varchar(100),
 PApellido varchar(100) not null,
 SApellido varchar(100),
 Monto float not null,
 EstadoCobro varchar(100) not null,
 EstadoAuto varchar(100) not null,
 CodigoChe INT,
 CodigoCuenta bigint,
 foreign key(CodigoCuenta) references Cuenta(CodigoCuenta),
 foreign key(CodigoChe) references Chequera(CodigoChe)
);

create table Trans(
 CodigoTransaccion INT not null primary key auto_increment,
 Cuenta bigint not null,
 Monto float not null,
 Fecha date not null,
 Descripcion varchar(200),
 CodigoCuenta bigint,
 foreign key(CodigoCuenta) references Cuenta(CodigoCuenta)
);

create table agregada(
 CodigoCuenta bigint not null,
 idCliente Int not null,
 foreign key(idCliente) references Cliente(idCliente),
 foreign key(CodigoCuenta) references Cuenta(CodigoCuenta)
 );
 
 create table  PreAuto(
 CodigoAuto Int not null primary key auto_increment,
 Correlativo INT not null,
 CuentaDestino bigint not null,
 PNombre varchar(100) not null,
 SNombre varchar(100),
 PApellido varchar(100) not null,
 SApellido varchar(100),
 Monto float  not null,
 CodigoChe INT,
 foreign key(CodigoChe) references Chequera(CodigoChe)
);
 
create table CambioC(
 CodigoCambio Int not null primary key auto_increment,
 FechaCambio date not null,
 Correlativo int not null,
 CodigoAuto INT,
 
 foreign key(Correlativo) references cheque(Correlativo),
 foreign key(CodigoAuto) references PreAuto(CodigoAuto)
);

 insert into ClienteEmpresarial(CUIRL, NombreEmpresa, NombreComercial, PNombreRL, SNombreRL, PApellidoRL, SApellidoRL, Ubicacion,NTelefonico, tipo_usuario, Tipo_Empresa) values(4889652230101, 'Paybes', 'Paybes S.A', 'Aida', 'Leticia', 'Caal', 'Catún', '2da calle-32 colonia santa rita 1', 54922157, 'Empresarial', 'Sociedad Anonima');
  insert into ClienteEmpresarial(CUIRL, NombreEmpresa, NombreComercial, PNombreRL, SNombreRL, PApellidoRL, SApellidoRL, Ubicacion,NTelefonico, tipo_usuario, Tipo_Empresa) values(5008572230101, 'La Torre', 'Alimentos S.A', 'Jose', 'Antonio', 'Hernandez', 'Paz', 'No Importa', 69698585, 'Empresarial', 'Sociedad Anonima');
select * from ClienteEmpresarial;


 insert into ClienteIndividual(CUI, NIT, PNombre, SNombre, PApellido, SApellido, FNacimiento, CorreoE, NTelefonico, tipo_usuario)values(3006439930101, 2883029-6, 'Byron', 'Estuardo', 'Caal','Catún', '2000/11/30', 'bcatun2015ig@gmail.com',54922157,'Individual');
 insert into ClienteIndividual(CUI, NIT, PNombre, SNombre, PApellido, SApellido, FNacimiento, CorreoE, NTelefonico, tipo_usuario)values(3009489633101, 3678028-9, 'Maria', 'Jose', 'Hernandez','de la Roca', '1999/11/14', 'mdelaroca@gmail.com',54835824,'Individual');
 insert into ClienteIndividual(CUI, NIT, PNombre, SNombre, PApellido, SApellido, FNacimiento, CorreoE, NTelefonico, tipo_usuario)values(2005989930101, 3001560-8, 'Ana', 'Lucia', 'Hernandez','Gonzalez', '2000/09/05', 'perritodepre@gmail.com',48566324,'Individual');
 select * from ClienteIndividual;
 select IdClienteIn from ClienteIndividual where CUI = 1 and Nit = 1 and PNombre = '' and SNombre = '';
delete from ClienteIndividual;
 
 insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario) values ('Admin', 'Admin', 'Administrador');
 select idCliente from Cliente where CodigoIngreso = and ClaveA = ;
 select IdClienteIn from ClienteIndividual where CUI = 3006439930101;
 insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteIn) values ('curious1924', 'byron14112305', 'Individual', 1);
 select * from Cliente;
 select CodigoIngreso from Cliente where tipo_usuario != 'Administrador' and Estado ;
 
 select idCliente ,CodigoIngreso from Cliente where tipo_usuario != 'Administrador';
 
 select idCliente from Cliente where tipo_usuario != 'Administrador';
 select idCliente, tipo_usuario from Cliente where CodigoIngreso = 'curious1924' and ClaveA = 'byron14112305';
select * from Cuenta where idCliente = 1 ;
select * from Cuenta;
select CodigoCuenta from Cuenta where CodigoChe = 0;

insert into Cuenta(Saldo, Estado, TipoMoneda, TipoCuenta, PreAuto, idCliente, CodigoChe) values (0, 'Activo', '$', 'Monetaria', 'No', 3, 0);