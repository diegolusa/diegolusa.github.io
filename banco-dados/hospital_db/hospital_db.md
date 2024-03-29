---
title: "Estudo de Caso - Hospital_Db"
excerpt: ""
tags:
 - Banco de Dados
 - SQL
 - Estudo de Caso
date: 2020-09-01 11:00:00
toc: false
order: 10
sidebar:
  nav: "db"
---



Em nossos tutoriais, utilizaremos a base de dados *sig_hospitalar_db* como estudo de caso. Trata-se de uma base que mapeia o universo de discurso de um hospital fictício. Logo temos tabelas armazenando dados de pacientes, acompanhantes, profissionais, internações, medicações e procedimentos, todas de modo simplificado, com finalidade didática, apenas. Observe, portanto, que o foco está na estrutura da base e não propriamente na fidedignidade com o mapeamento de dados reais de ambientes hospitalares.

Considerando que você já tenha realizado a instalação do servidor PostgreSQL em sua máquina, passaremos ao passo seguinte, no qual a base de dados *sig_hospitalar_db* será criada. Tal operação pode ser realizada via *psql* ou por meio da IDE de sua preferência ([PgAdmin4](https://www.pgadmin.org/download/), por exemplo). Caso opte pelo *psql*, utilize o comando `create database sig_hospitalar_db;` no terminal. 

Agora, conectado à base *sig_hospitalar_db*, proceda com a execução dos comandos abaixo na íntegra.

```sql
begin;

create domain t_nome as varchar(200) not null check(value ~'[a-zA-z]+');

create table bairro(
	id serial not null primary key,
	nome t_nome,
	cidade_id integer not null


);


insert into bairro values
		(1, 'Centro',1),
		(2, 'Sol Nascente',1),
		(3, 'São Paulo',1),
		
		(4, 'Vera Cruz',2),
		(5, 'Centro',2),
		(6, 'São Cristovão',2),

		(7, 'Centro',3),
		(8, 'Três Vendas',3),
		(9, 'Fátima',3);

create table cidade(
	id serial not null primary key,
	nome t_nome
);

insert into cidade values 
	(1,'Tapejara'),
	(2,'Passo Fundo'),
	(3,'Erechim');


create domain t_cnpj as char(14) check (value ~ '^[0-9]{14}$');
create domain t_cpf as char(11) check (value ~ '^[0-9]{11}$');

create table convenio(
	id serial not null primary key,
	razao_social t_nome,
	cnpj t_cnpj not null unique,
	descricao text
);
comment on table convenio is 'Armazena os diferentes planos de saúde utilizados pelos pacientes em suas internações';



insert into convenio values 
	(1,'UNIMED','16034061000100',null),
	(2,'IPE Saúde', '40355755000123',null),
	(3, 'Cassi','63364447000160', null);

create table diagnostico(
		id serial not null primary key,
		cid char(4) not null unique,
		nome t_nome,
		descricao text
);

comment on table diagnostico is 'Armazena dados acerca dos diagnósticos médicos';
comment on column diagnostico.cid is 'Classificação Internacional de Doenças';



insert into diagnostico(id, cid,nome) VALUES
	(1,'A000','Cólera devida a Vibrio cholerae 01, biótipo cholerae'),
	(2,'A009','Cólera não especificada'),
	(3,'B000','Eczema herpético'),
	(4,'B008','Outras formas de infecção devida ao vírus do herpes');


create table diagnostico_prescricao (
	prescricao_id integer not null,
	diagnostico_id integer not null,
	primary key(prescricao_id, diagnostico_id)
);

comment on table diagnostico_prescricao is 'Armazena os diagnósticos da prescrição';

insert into diagnostico_prescricao values
	(1,2),
	(2,1),
	(3,4),
	(4,4);

create table enfermeiro(
	pessoa_id integer not null primary key,
	coren char(7) not null check (coren ~ '^[0-9]{7}$')

);

comment on column enfermeiro.coren is 'Código de registro do enfermeiro no Conselho Regional de Enfermagem';

insert into enfermeiro values 
	(1, '0123654'),
	(2, '0251687');

create table especialidade(
	id serial not null primary key,
	nome t_nome
);

comment on table especialidade is 'Armazena as especialidades médicas, como cardiologia, pediatria, etc.';

insert into especialidade values 
	(1, 'Cardiologia'),
	(2, 'Pediatria'),
	(3, 'Otorinolaringologia'),
	(4, 'Ortopedia');

create table evolucao_internacao(
	internacao_id integer not null,
	data_hora timestamp not null default CURRENT_TIMESTAMP,
	evolucao text not null,
	enfermeiro_id integer not null,
	primary key (internacao_id, data_hora)
);

comment on table evolucao_internacao is 'Evolução é a descrição do estado do paciente. Os enfermeiros fazem várias evoluções do paciente durante a internação';

insert into evolucao_internacao values 
	(1,default,'Pariatur tempor nulla aliquip elit est proident consequat deserunt incididunt et minim. Aliquip consequat cupidatat do proident aliquip aliquip magna sit consequat anim aliqua proident. Amet mollit in consectetur ut. Sint laborum elit occaecat laboris. Consequat veniam dolor proident fugiat. Commodo qui aliqua anim veniam non velit non reprehenderit consequat dolor voluptate cillum. Tempor et qui tempor consequat.
Sunt labore veniam non duis eiusmod laboris voluptate sit dolore nisi. Incididunt eiusmod nostrud eu consequat velit ex eu adipisicing tempor tempor occaecat anim. Ex commodo nisi ullamco ex officia consectetur eu laborum. Lorem magna Lorem aliqua ullamco adipisicing sunt consectetur reprehenderit minim dolore voluptate qui quis. Voluptate anim fugiat consectetur irure commodo aliquip nisi adipisicing. Cillum adipisicing nostrud sit anim mollit aliqua do deserunt exercitation cupidatat. Officia dolor duis incididunt minim velit cillum et cillum adipisicing esse Lorem labore sunt reprehenderit.
Nisi fugiat incididunt culpa dolore ex ullamco sit et velit est sit ut. Do sint sint magna aliqua veniam sint aute velit adipisicing aute tempor sint aliquip irure. Non sunt consequat eiusmod deserunt anim. Nostrud tempor sint eiusmod pariatur officia aliqua reprehenderit. Ex reprehenderit enim Lorem proident id eiusmod id eiusmod est minim. Sunt sint et reprehenderit occaecat do aute amet.
Sit do consectetur in tempor deserunt sunt velit mollit do proident sunt ex. Excepteur aliqua fugiat ut tempor dolore nostrud consequat reprehenderit anim quis consectetur nulla proident qui. Sit dolor Lorem proident laboris aute consequat irure cillum mollit nisi fugiat duis. Est dolore qui sunt quis voluptate magna esse sint occaecat. Occaecat voluptate nulla tempor veniam pariatur consectetur sunt non elit cupidatat deserunt reprehenderit elit laboris. Lorem duis officia sit sit voluptate ea dolore.
Nostrud anim ea adipisicing cillum. Aute ipsum est dolor magna non. Consectetur aliqua esse reprehenderit qui aliquip do tempor irure. Amet est deserunt do in.',2);


insert into evolucao_internacao values 
	(2,default,'Pariatur tempor nulla aliquip elit est proident consequat deserunt incididunt et minim. Aliquip consequat cupidatat do proident aliquip aliquip magna sit consequat anim aliqua proident. Amet mollit in consectetur ut. Sint laborum elit occaecat laboris. Consequat veniam dolor proident fugiat. Commodo qui aliqua anim veniam non velit non reprehenderit consequat dolor voluptate cillum. Tempor et qui tempor consequat.
Sunt labore veniam non duis eiusmod laboris voluptate sit dolore nisi. Incididunt eiusmod nostrud eu consequat velit ex eu adipisicing tempor tempor occaecat anim. Ex commodo nisi ullamco ex officia consectetur eu laborum. Lorem magna Lorem aliqua ullamco adipisicing sunt consectetur reprehenderit minim dolore voluptate qui quis. Voluptate anim fugiat consectetur irure commodo aliquip nisi adipisicing. Cillum adipisicing nostrud sit anim mollit aliqua do deserunt exercitation cupidatat. Officia dolor duis incididunt minim velit cillum et cillum adipisicing esse Lorem labore sunt reprehenderit.
Nisi fugiat incididunt culpa dolore ex ullamco sit et velit est sit ut. Do sint sint magna aliqua veniam sint aute velit adipisicing aute tempor sint aliquip irure. Non sunt consequat eiusmod deserunt anim. Nostrud tempor sint eiusmod pariatur officia aliqua reprehenderit. Ex reprehenderit enim Lorem proident id eiusmod id eiusmod est minim. Sunt sint et reprehenderit occaecat do aute amet.
Sit do consectetur in tempor deserunt sunt velit mollit do proident sunt ex. Excepteur aliqua fugiat ut tempor dolore nostrud consequat reprehenderit anim quis consectetur nulla proident qui. Sit dolor Lorem proident laboris aute consequat irure cillum mollit nisi fugiat duis. Est dolore qui sunt quis voluptate magna esse sint occaecat. Occaecat voluptate nulla tempor veniam pariatur consectetur sunt non elit cupidatat deserunt reprehenderit elit laboris. Lorem duis officia sit sit voluptate ea dolore.
Nostrud anim ea adipisicing cillum. Aute ipsum est dolor magna non. Consectetur aliqua esse reprehenderit qui aliquip do tempor irure. Amet est deserunt do in.',1);

insert into evolucao_internacao values 
	(3,default,'Pariatur tempor nulla aliquip elit est proident consequat deserunt incididunt et minim. Aliquip consequat cupidatat do proident aliquip aliquip magna sit consequat anim aliqua proident. Amet mollit in consectetur ut. Sint laborum elit occaecat laboris. Consequat veniam dolor proident fugiat. Commodo qui aliqua anim veniam non velit non reprehenderit consequat dolor voluptate cillum. Tempor et qui tempor consequat.
Sunt labore veniam non duis eiusmod laboris voluptate sit dolore nisi. Incididunt eiusmod nostrud eu consequat velit ex eu adipisicing tempor tempor occaecat anim. Ex commodo nisi ullamco ex officia consectetur eu laborum. Lorem magna Lorem aliqua ullamco adipisicing sunt consectetur reprehenderit minim dolore voluptate qui quis. Voluptate anim fugiat consectetur irure commodo aliquip nisi adipisicing. Cillum adipisicing nostrud sit anim mollit aliqua do deserunt exercitation cupidatat. Officia dolor duis incididunt minim velit cillum et cillum adipisicing esse Lorem labore sunt reprehenderit.
Nisi fugiat incididunt culpa dolore ex ullamco sit et velit est sit ut. Do sint sint magna aliqua veniam sint aute velit adipisicing aute tempor sint aliquip irure. Non sunt consequat eiusmod deserunt anim. Nostrud tempor sint eiusmod pariatur officia aliqua reprehenderit. Ex reprehenderit enim Lorem proident id eiusmod id eiusmod est minim. Sunt sint et reprehenderit occaecat do aute amet.
Sit do consectetur in tempor deserunt sunt velit mollit do proident sunt ex. Excepteur aliqua fugiat ut tempor dolore nostrud consequat reprehenderit anim quis consectetur nulla proident qui. Sit dolor Lorem proident laboris aute consequat irure cillum mollit nisi fugiat duis. Est dolore qui sunt quis voluptate magna esse sint occaecat. Occaecat voluptate nulla tempor veniam pariatur consectetur sunt non elit cupidatat deserunt reprehenderit elit laboris. Lorem duis officia sit sit voluptate ea dolore.
Nostrud anim ea adipisicing cillum. Aute ipsum est dolor magna non. Consectetur aliqua esse reprehenderit qui aliquip do tempor irure. Amet est deserunt do in.',2);

create table funcionario(
	pessoa_id integer not null primary key,
	pis_pasep char(11) not null check (pis_pasep ~ '^[0-9]{11}$')
);

insert into funcionario values 
	(1,'83919800958'),
	(2,'84811096999'),
	(3,'31859934560'),
	(4,'12649826837'),
	(5,'94340833899');

create table internacao(
	id bigserial not null primary key,
	medico_id integer not null,
	leito_id integer not null,
	paciente_id integer not null,
	data_hora_internacao timestamp not null default CURRENT_TIMESTAMP,
	tipo_clinica char(1) not null default 'M' check (tipo_clinica in ('M','O','P','A') ),
	convenio_id integer not null,
	data_hora_alta timestamp,
	registrante_id integer not null,
	anamnese text not null
);
comment on column internacao.tipo_clinica is 'M - Médica, O - Obstétrica, C - Cirúrgica, P - Pediátrica, A - Ambulatório ';
comment on table internacao is 'Internação é o procedimento em que o paciente torna-se interno ao hospital para tratar de sua saúde';


insert into internacao(id, medico_id, leito_id,paciente_id,registrante_id, anamnese,convenio_id) values 
	(1,8,1,12,4,'Paciente queixou-se de dores abdominais intensas',1),
	(2,9,2,13,4,'Paciente apresenta febre de 39 graus',2),
	(3,10,2,12,4,'Paciente apresenta desequilibrio e síncopes frequentes',3),
	(4,11,3,14,4,'Paciente episódios de amnésia e hipersonia ',3),
	(5,8,4,15,4,'Paciente queixou-se de dores lombares intensas',1);

create table leito (
	id serial not null primary key,
	codigo varchar(3) not null unique,
	quarto_id integer not null,
	descricao text
);

insert into leito values 
(1,'A1',1,NULL), (2,'A2',1,NULL), (3,'A3',1,NULL), 
(4,'B1',2,NULL), (5,'B2',2,NULL), (6,'B3',2,NULL), 
(7,'C1',3,NULL), (8,'C2',3,NULL), (9,'C3',3,NULL), 
(10,'D1',4,NULL), (11,'D2',4,NULL), (12,'D3',4,NULL);

create table quarto (
	id serial not null primary key,
	nome varchar(20) not null unique,
	posto_id integer not null,
	tipo char(1) not null check (tipo in ('P','N')),
	numero_banheiros smallint not null
);



insert into quarto values
	(1,'A',1,'P',2),
	(2,'B',2,'P',1),
	(3,'C',3,'P',1),
	(4,'D',4,'P',3);


create table material (
	id serial not null primary key,
	nome t_nome,
	valor money not null,
	descricao text
) ;

comment on table material is 'Itens não medicamentosos utilizados no hospital';


insert into material values 
	(1,'Esparadrapo',0.56, null),
	(2,'Micropore',1.5, null),
	(3,'Adesivo', 2.5,null),
	(4,'Agulha para Sutura',3.50,null),
	(5,'Algodão',2.89,null),
	(6,'Atadura',8.56, null),
	(7,'Curativos',15.69, null),
	(8,'Bolsa Térmica', 12.5,null),
	(9,'Coletores',40,null),
	(10,'Compressas',2.98,null);





create table material_prescricao (
	prescricao_id integer not null,
	material_id integer not null,
	data_hora_lancamento timestamp not null default current_timestamp,
	quantidade numeric (20,3) not null,
	primary key (prescricao_id,material_id, data_hora_lancamento)

);

comment on table material_prescricao is 'Armazena os diferentes materiais usados na prescrição';


insert into material_prescricao values 
(1,1,default,12), (1,5,default,6),(1,10,default,5),
(2,3,default,12), (2,6,default,6),(2,9,default,5),
(3,2,default,12), (3,7,default,6),(3,8,default,5);


create table medicamento (
	id serial not null primary key,
	denominacao_generica varchar(200) not null,
	concentracao varchar(20) not null,
	forma_farmaceutica varchar(50) not null,
	descricao text
);


insert into medicamento values 
	(1,'cloreto de sódio', '3,4 mEq/mL (20%)', 'solução injetável'),
	(2,'cloridrato de amiodarona', '50 mg/mL', 'solução injetável'),
	(3,'cloridrato de amiodarona', '200 mg', 'comprimido'),
	(4,'cloridrato de clindamicina', '150 mg', 'cápsula'),
	(5,'cloridrato de clomipramina', '10 mg', 'comprimido');


create table medico (
	pessoa_id integer not null primary key,
	crm char(6) not null check (crm ~ '^[0-6]{6}')
);

insert into medico values 
(8, '000345'),(9, '000346'),(10, '000350'),(11, '000351');


create table medico_especialidade (
	medico_id integer not null,
	especialidade_id integer not null,
	primary key (medico_id, especialidade_id)
);

comment on table medico_especialidade is 'Relaciona as especialidades aos médicos';


insert into medico_especialidade values
	(8,1),(9,4),(10,2),(11,3);


create table medicamento_prescricao (
	prescricao_id integer not null,
	medicamento_id  integer not null,
	data_hora_lancamento timestamp not null default CURRENT_TIMESTAMP,
	aprazamento varchar(100) not null,
	dosagem varchar(100) not null,
	primary key(prescricao_id, medicamento_id,data_hora_lancamento)
);

comment on table medicamento_prescricao is 'Armazena os diferentes medicamentos usados na prescrição';

insert into  medicamento_prescricao values 
	(1,3,default,'6/6 horas','1 comprimido'),
	(1,4,default,'12/12 horas','1 capsula'),
	(1,2,default,'6/6 horas','10 ml');


create table paciente (
	pessoa_id integer not null primary key,
	responsavel_id integer not null,
	nome_mae t_nome,
	cartao_sus char(15) not null unique check(cartao_sus ~'^[0-9]{14}')
);

insert into paciente values 
	(12,16,'Fabiana Ana Sônia Corte Real','267584097280006'),
	(13,17,'Marcela Antônia Liz Aragão','147243223830007'),
	(14,18,'Daiane Olivia Cristiane Novaes','223139799940002'),
	(15,19,'Alana Rita Betina Brito','816428033820008');


create table pessoa (
	id serial not null primary key,
	nome t_nome,
	telefone varchar(11) not null check (telefone ~ '^[0-9]{10,11}$'),
	cpf t_cpf,
	identidade varchar(10) not null,
	rua_id integer not null,
	numero_endereco integer,
	complemento_endereco varchar(100),
	data_nascimento date not null,
	sexo char(1) not null check (sexo in ('M','F')),
	cep_endereco char(8) not null check (cep_endereco ~ '^[0-9]{8,9}$')
);



insert into pessoa values 
	(1,'Lorena Fátima Carolina Nunes','5137140997','50037489062','265780329',1,'635','','01/11/1996','F','99910020'),
	(2,'Diogo Hugo César Silva','5135356502','66911317037','238012669',2,'197','','27/02/1996','M','99810020'),
	(3,'Matheus Manoel Martin Viana','5135703717','53775328050','199665953',3,'402','','12/11/1996','M','99710020'),
	(4,'Kevin Marcos Vinicius Raimundo Vieira','5135356503','66911317037','238012669',2,'197','','27/02/1996','F','69910020'),
	(5,'Benício Alexandre André Rocha','5135356504','66911317078','238012669',2,'197','','27/02/1995','F','78910030'),
	(6,'Lorena Vitória da Silva','5135356505','66911317058','238012669',2,'197','','27/02/1994','F','76910029'),
	(7,'Andreia Mariah Rocha','5135356506','66911317034','238012669',2,'197','','27/02/1993','F','76910028'),
	(8,'Elza Mariane Sophia Bernardes','5135356507','66911317056','238012669',2,'197','','27/02/1994','F','76910027'),
	(9,'Débora Ester Adriana Rodrigues','5135356508','66911317090','238012669',2,'197','','27/02/1993','F','76910026'),
	(10,'Joana Olivia Castro','5135356510','66911317067','238012669',2,'197','','27/02/1992','F','76910025'),
	(11,'Giovana Cláudia da Silva','5135356512','66911317056','238012669',2,'197','','27/02/1991','F','76910024'),
	(12,'Lorena Vitória Jesus','5135356513','66911317040','238012669',2,'197','','27/02/1999','F','76910023'),
	(13,'Flávia Lívia Martins','5135356514','66911317039','238012669',2,'197','','27/02/1998','F','76910022'),
	(14,'Angela da Mata','5135356515','66911317041','238011669',2,'197','','27/02/1995','F','76910321'),
	(15,'Marcia Fagundes','5135356515','66911317051','238112669',2,'197','','27/02/1995','F','76912021'),
	(16,'Artur da Mata','5135356515','66911317061','231012669',2,'197','','27/02/1995','F','76911021'),
	(17,'Maiki Dellani','5135756515','66421317061','233014669',2,'197','','28/02/1995','F','76611021'),
	(18,'Fabio Dellani','5135656515','66431317061','233018669',2,'197','','28/02/1995','F','76611021'),
	(19,'Mateus Dellani','5134356515','66511317061','233019669',2,'197','','28/02/1995','F','76611021');


create table posto (
	id serial not null primary key,
	nome varchar(10) not null unique,
	descricao text
);

insert into posto values 
	(1,'P1',null),(2,'P2',null),(3,'P3',null),(4,'P4',null);


create table prescricao(
	prescricao_id serial not null primary key,
	internacao_id integer not null,
	data date not null default current_date,
	hora time not null default current_time,
	evolucao_medica text,
	unique(internacao_id, data)
);

insert into prescricao values
	(1,1,current_date-2,default,'Paciente não apresentou melhora'),
	(2,1,current_date-1,default,'Paciente não apresentou melhora'),
	(3,1,default,default,'Paciente apresentou leve melhora com a nova medicação utilizada'),
	(4,2,default,default,'Não houve melhora clínica aparente'),
	(5,3,default,default,'O procedimento realizado demonstrou normalidade nas atividades vitais básicas'),
	(6,4,default,default,'Aguarda-se resultado de exames para orientar a escolha da melhor medicação');	


create table procedimento(
	id serial not null primary key,
	nome t_nome,
	descricao text
);

comment on table procedimento is 'Intervenções médicas metódicas para fins diagnósticos, cirúrgicos, etc';

insert into procedimento values 
	(1,'Ultrassonografia'),(2,'Eletrocardiograma'),(3,'Radiografia');


create table procedimento_internacao(
	procedimento_id integer not null,
	internacao_id integer not null,
	data_hora timestamp not null default current_timestamp,
	primary key(procedimento_id, internacao_id,data_hora)
);

insert into procedimento_internacao
values (1,1,default), (2,3,default);


create table rua (
	id serial not null primary key,
	nome t_nome,
	bairro_id integer not null
);

insert into rua values 
	(1,'Rogério Nunes',1),
	(2,'Travessa Tiradentes',2),
	(3,'Raimunda Pereira Lima',3),
	(4,'Arenópolis',4),
	(5,'Rui Barbosa',5),
	(6,'Cristovão Colombo',6),
	(7,'Getúlio Vargas',7),
	(8,'Nelson Mandela',8),
	(9,'André Franco Montora',9);


alter table rua add constraint fk_rua_bairro foreign key(bairro_id) references bairro;

alter table procedimento_internacao add 
	constraint fk_procedimento_int_internacao foreign key(internacao_id) references internacao;
alter table procedimento_internacao add 
	constraint fk_procedimento_int_procedimento foreign key(procedimento_id) references procedimento;



alter table prescricao add 
	constraint fk_prescricao_internacao foreign key(internacao_id) references internacao;

alter table pessoa add constraint fk_pessoa_rua
	foreign key (rua_id) references rua;

alter table paciente add constraint fk_paciente_responsavel 
	foreign key (responsavel_id) references pessoa;


alter table paciente add constraint fk_paciente_pessoa 
	foreign key (pessoa_id) references pessoa;


alter table medicamento_prescricao add constraint fk_medicamento_pres_prescricao 
	foreign key (prescricao_id) references prescricao;

alter table medicamento_prescricao add constraint fk_medicamento_pres_medicamento
	foreign key (medicamento_id) references medicamento;
	

alter table medico_especialidade add constraint fk_medico_esp_medico foreign key (medico_id) references medico;
alter table medico_especialidade add constraint fk_medico_esp_especialidade foreign key (especialidade_id) references especialidade;


alter table medico add constraint fk_medico_pessoa foreign key (pessoa_id) references pessoa;

alter table material_prescricao add constraint fk_mat_pres_prescricao foreign key (prescricao_id) references prescricao;
alter table material_prescricao add constraint fk_mat_pres_material foreign key (material_id) references material;

alter table leito add constraint fk_leito_quarto foreign key (quarto_id) references quarto;
alter table internacao add constraint fk_internacao_medico foreign key (medico_id) references medico;
alter table internacao add constraint fk_internacao_leito foreign key (leito_id) references leito;
alter table internacao add constraint fk_internacao_paciente foreign key (paciente_id) references paciente;
alter table internacao add constraint fk_internacao_funcionario foreign key (registrante_id) references funcionario;
alter table internacao add constraint fk_internacao_convenio foreign key (convenio_id) references convenio;


alter table funcionario add constraint fk_funcionario_pessoa foreign key (pessoa_id) references pessoa;
alter table evolucao_internacao add constraint fk_evolucao_int_enfermeiro foreign key (enfermeiro_id) references enfermeiro;
alter table evolucao_internacao add constraint fk_evolucao_int_internacao foreign key (internacao_id) references internacao;
alter table enfermeiro add constraint fk_enfermeiro_pessoa foreign key (pessoa_id) references pessoa;
alter table diagnostico_prescricao add constraint fk_diag_int_prescricao foreign key (prescricao_id) references prescricao;
alter table diagnostico_prescricao add constraint fk_diag_int_diagnostico foreign key (diagnostico_id) references diagnostico;
alter table bairro add constraint fk_bairro_cidade foreign key (cidade_id) references cidade;
alter table quarto add constraint fk_quarto_posto foreign key(posto_id) references posto;


commit;
```