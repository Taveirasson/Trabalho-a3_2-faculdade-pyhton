use atividade;

create table formulario(
	id int(5) auto_increment,
    diagnostico varchar(50),
    eritrocitos decimal(4,2),
	hemoglobina DECIMAL(5,2),
    dematocrito DECIMAL(5,2),
    hcm DECIMAL(5,2),
    vgm DECIMAL(5,2),
    chgm DECIMAL(5,2),
    metarrubricitos DECIMAL(5,2),
    proteina_plasmatica DECIMAL(5,2),
    leucocitos INT(10),
    leucograma INT(10),
    segmentados INT(10),
    bastonetes INT(10),
    blastos INT(10),
    metamielocitos INT(10),
    mielocitos INT(10),
    linfocitos INT(10),
    monocitos INT(10),
    eosinofilos INT(10),
    basofilos INT(10),
    plaquetas varchar(30)
);