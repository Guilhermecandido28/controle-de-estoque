CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imagem BLOB,
	nome CHAR ( 40 ) NOT NULL,
	sobrenome CHAR ( 40 ),
	celular INTEGER ( 20 ),
	cpf CHAR ( 14 ),
	instagram CHAR ( 40 ),
	OBS CHAR ( 100 ),
	CEP CHAR ( 9 ),
	rua CHAR ( 150 ),
	numero INTEGER ( 10 ),
	bairro CHAR ( 40 ),
	cidade CHAR ( 40 ),
	estado CHAR ( 20 ),
    valor_gasto NUMERIC ( 10, 2 ) 
);

CREATE TABLE compras (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	data_compra	DATE,
	data_entrega	DATE,
	codigo_de_barras	TEXT,
	produto	TEXT,
	fornecedor	TEXT,
	forma_de_pagamento	TEXT,
	parcelamento	TEXT,
	vencimento	TEXT,
	qtd_parcial	TEXT,
	quantidade	INTEGER,
	frete	REAL,
	desconto	REAL,
	status	TEXT,
	total	REAL
);

CREATE TABLE estoque (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT CHECK ( length( descricao ) <= 200 ),
	categoria TEXT CHECK ( length( categoria ) <= 100 ),
	marca TEXT CHECK ( length( marca ) <= 100 ),
	estoque_minimo INTEGER,
	quantidade INTEGER,
	observacoes TEXT CHECK ( length( observacoes ) <= 200 ),
	tamanho TEXT CHECK ( length( tamanho ) <= 3 ),
	fornecedor TEXT,
	cor TEXT CHECK ( length( cor ) <= 70 ),
	custo TEXT,
	venda NUMERIC,
	imagem BLOB
);

CREATE TABLE fornecedor (
	ID INTEGER PRIMARY KEY,
	nome TEXT CHECK ( length( nome ) <= 200 ),
	categoria TEXT CHECK ( length( categoria ) <= 100 ),
	cnpj TEXT CHECK ( length( cnpj ) <= 20 ),
	email TEXT,
	telefone TEXT,
	OBS TEXT CHECK ( length( OBS ) <= 200 ),
	CEP TEXT CHECK ( length( CEP ) <= 9 ),
	rua TEXT CHECK ( length( rua ) <= 100 ),
	numero TEXT,
	bairro TEXT,
	cidade TEXT,
	estado TEXT,
	lista_produtos TEXT,
    imagem BLOB 
);

CREATE TABLE venda (
    ID INTEGER PRIMARY KEY,
	data	DATE,
	produtos	TEXT,
	cliente	TEXT,
	desconto	TEXT,
	total	TEXT,
	forma_pagamento	TEXT
);