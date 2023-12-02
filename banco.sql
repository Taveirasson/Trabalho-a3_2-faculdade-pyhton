use atividade;

create table formulario(
	id int(5) auto_increment,
    diagnostico varchar(50),
    eritrocitos varchar(50),
	hemoglobina varchar(50),
    dematocrito varchar(50),
    hcm varchar(50),
    vgm varchar(50),
    chgm varchar(50),
    metarrubricitos varchar(50),
    proteina_plasmatica varchar(50),
    leucocitos varchar(30),
    leucograma varchar(30),
    segmentados varchar(30),
    bastonetes varchar(30),
    blastos varchar(30),
    metamielocitos varchar(30),
    mielocitos varchar(30),
    linfocitos varchar(30),
    monocitos varchar(30),
    eosinofilos varchar(30),
    basofilos varchar(30),
    plaquetas varchar(30),
    primary key (id)
);

create table formulario(
    id int AUTO_INCREMENT PRIMARY KEY,
    diagnostico VARCHAR(255),
    eritrocitos DECIMAL(10, 2),
    hemoglobina DECIMAL(10, 2),
    hematocrito DECIMAL(10, 2),
    hCM DECIMAL(10, 2),
    vgm DECIMAL(10, 2),
    chgm DECIMAL(10, 2),
    metarrubricitos DECIMAL(10, 2),
    proteina_Plasmatica DECIMAL(5,2),
    leucocitos DECIMAL(10, 2),
    leucograma DECIMAL(10, 2),
    segmentados DECIMAL(10, 2),
    bastonetes DECIMAL(10, 2),
    blastos DECIMAL(10,2),
    metamielocitos DECIMAL(10, 2),
    mielocitos DECIMAL(10, 2),
    linfocitos DECIMAL(10, 2),
    monocitos DECIMAL(10, 2),
    eosinofilos DECIMAL(10, 2),
    basofilos DECIMAL(10, 2),
    plaquetas DECIMAL(10, 2)
);
drop table formulario;

select * from formulario;