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

drop table formulario;

select * from formulario;